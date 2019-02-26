from app import app
from flask import Flask, render_template, request
from simple_salesforce import Salesforce
from dotenv import get_key, find_dotenv
import requests
import os
import logging
import argparse
import sys
import codecs


@app.route('/')
def start():
    token_v = get_sfdc_token()
    print(get_key(find_dotenv(),"Local_Dropbox_Folder"))
    return render_template('index.html', token = token_v)

@app.route('/', methods=('GET', 'POST'))
def form_submit():
    if request.method == 'POST':
        user_v = request.form['email']
        passwd_v = request.form['password']
        case_v = request.form['caseNumber']
        token_v = get_sfdc_token()
        storage_v = get_key(find_dotenv(),"Local_Dropbox_Folder")

        # check the case number is valid
        case_v = check_case_number(case_v)
        try:
            len(case_v)
        except:
            error = "Invalid case number"
            return render_template('index-error.html', error = error, token = token_v)

        # check SFDC credentials are valid
        salesforce_check = sfdc_authorization(user_v, passwd_v, token_v)
        if salesforce_check == 1:
            pass
        else:
            error = "Failed to connect to SFDC"
            return render_template('index-error.html', error = error, token = token_v)

        new_dir = "{}\\\\{}".format(storage_v, case_v)

        dropbox_baseURL = get_key(find_dotenv(),"Dropbox_URL")
        dropbox_URL = "{}/{}".format(dropbox_baseURL,case_v)

        download_attachments_on_case(user_v, passwd_v, case_v, token_v,
            storage_v, new_dir)
        download_attachment_email(user_v, passwd_v, case_v, token_v,
            storage_v, new_dir)
        file_length = cleanup(new_dir)

        if file_length > 0:
            return render_template("result.html", caseNumber = case_v,
                new_dir = dropbox_URL, files = file_length, token = token_v)
        else:
            error = "No photos to upload"
            return render_template('index-error.html', error = error, token = token_v)

def check_case_number(case_v):
    # check the case is prepended with two zeroes
    if len(case_v) == 6:
        case_v = '00'+case_v
        print("Case# check: Added 00 to the case number {}\n".format(case_v))
    elif len(case_v) > 8 or len(case_v)< 6:
        print("Case# check: This should error {}\n".format(case_v))
        case_v = None
    else:
        print("Case number check: This case number is {}\n".format(case_v))
        pass

    return case_v

def get_sfdc_token():
    token_v = get_key(find_dotenv(),"SFDC_Token")
    return token_v

def sfdc_authorization(user_v, passwd_v, token_v):
    session = requests.Session()
    try:
        sf = Salesforce(username = user_v,
                        password = passwd_v,
                        security_token = token_v,
                        session = session)
        error = 1
    except:
        logging.error("Failed to connect SFDC")
        error = "Failed to connect to SFDC"

    return error


def download_attachments_on_case(user_v, passwd_v, case_v, token_v,
        storage_v, new_dir):
    session = requests.Session()

    print(len(case_v),case_v)
    print(new_dir)

    #new_dir = "{}\{}".format(storage_v, case_v)
    logging.info("New Directory is {}".format(new_dir))

    if not os.path.exists(new_dir):
        #check this line - is it needed?
        print(os.path.exists(new_dir))
        new_dir = "{}\{}".format(storage_v, case_v)
        os.mkdir(new_dir)
        logging.debug("Storage path doesn't exist - folder {} created".format(case_v))

    if not os.path.isdir(storage_v):
        logging.error("ERROR: Storage path must be a directory")
        sys.exit(1)

    logging.basicConfig(level = logging.DEBUG,
                        format = '%(asctime)s - %(levelname)s - %(message)s',
                        filemode = 'w')

    try:
        sf = Salesforce(username = user_v,
                        password = passwd_v,
                        security_token = token_v,
                        session = session)
    except:
        logging.error("Failed to connect SFDC")
        error = "Failed to connect to SFDC"
        return error

    auth_id = "Bearer " + sf.session_id
    req_headers = {'Authorization': auth_id}
    query = ("SELECT Id, ParentId, Name, Body FROM Attachment WHERE ParentId IN ("
            "SELECT SourceId FROM Case WHERE casenumber = '{}') "
            "AND BodyLength > 2000 AND BodyLength != 6912 "
            "AND (Name LIKE '%.jpg' OR Name LIKE '%.png' OR Name LIKE '%.gif') "
            "AND IsDeleted = False LIMIT 100".format(case_v))

    result = sf.query(query)
    print("Running query 1: {}\n".format(query))
    logging.info("Running query: {}".format(query))
    print("Query 1 result is: {}\n".format(result))

    total_records = result.get('totalSize', 0)
    print('Total records retrieved: {}'.format(total_records))

    logging.info('Starting to download {} attachments'.format(total_records))

    storage_dir = new_dir
    sf_pod = sf.base_url.replace("https://", "").split('.salesforce.com')[0]

    records = result.get('records', {})
    for record in records:
        body_uri = record.get('Body')
        if not body_uri:
            logging.warning("No body URI for file id {}".format(record.get('Id', '')))
            continue

        remote_file = record.get('Name')
        remote_file_lower = remote_file.lower()
        remote_path = "https://{}.salesforce.com{}".format(sf_pod, body_uri)
        local_file = "{}_{}".format(record.get('Id'), remote_file)
        local_path = os.path.join(new_dir, local_file)

        logging.info("Downloading {} to {}".format(remote_file, local_path))
        logging.debug("Remote URL: {}".format(remote_path))

        response = session.get(remote_path, headers=req_headers)
        if response.status_code != 200:
            logging.error("Download failed {}".format(response.status_code))
            continue

        with open(local_path, 'wb') as out_file:
            out_file.write(response.content)

def download_attachment_email(user_v, passwd_v, case_v, token_v, storage_v, new_dir):
    session = requests.Session()

    #new_dir = "{}\{}".format(storage_v, case_v)
    logging.info("New Directory is {}".format(new_dir))

    if not os.path.exists(new_dir):
        #check this line - is it needed?
        new_dir = "{}\{}".format(storage_v, case_v)
        os.mkdir(new_dir)
        logging.debug("Storage path doesn't exist yet - folder {} created".format(case_v))

    if not os.path.isdir(storage_v):
        logging.error("ERROR: Storage path must be a directory")
        sys.exit(1)

    logging.basicConfig(level = logging.DEBUG,
                        format = '%(asctime)s - %(levelname)s - %(message)s',
                        filemode = 'w',
                        filename = 'sfdc_log.log')

    try:
        sf = Salesforce(username = user_v,
                        password = passwd_v,
                        security_token = token_v,
                        session = session)
    except:
        logging.error("Failed to connect SFDC")
        return

    auth_id = "Bearer " + sf.session_id
    req_headers = {'Authorization': auth_id}
    query_case_id = ("SELECT Id FROM Case WHERE Casenumber = '{}'".format(case_v))

    result_case = sf.query(query_case_id)
    print("Running query 2: {}\n".format(query_case_id))
    logging.info("Running query: {}".format(query_case_id))
    print("Query 2 result is: {}\n".format(result_case))

    try:
        case_sfdc_id = result_case.get('records')[0].get('Id')
        logging.debug("The case id is: {}".format(case_sfdc_id))
        print("The case id is: {}\n".format(case_sfdc_id))
    except:
        return

    query = ("SELECT Id, ParentId, Name, Body, BodyLength FROM Attachment WHERE"
            " ParentId IN (SELECT Id FROM EmailMessage WHERE ParentId = '{}')"
            " AND BodyLength > 2000 AND BodyLength != 6912 "
            " AND (Name LIKE '%.jpg' OR Name LIKE '%.png' OR Name LIKE '%.gif')"
            " AND IsDeleted = False LIMIT 100".format(case_sfdc_id))

    result = sf.query(query)
    print("Running query 3: {}\n".format(query))
    logging.info("Running query: {}".format(query))
    print("Query 3 result is: {}\n".format(result))

    total_records = result.get('totalSize', 0)
    print('Total records retrieved: {}'.format(total_records))

    storage_dir = new_dir
    sf_pod = sf.base_url.replace("https://", "").split('.salesforce.com')[0]

    logging.info('Starting to download {} attachments'.format(total_records))
    records = result.get('records', {})
    distinct_ids = []
    for record in records:
        if record.get('BodyLength') not in distinct_ids:
            distinct_ids.append(record.get('BodyLength'))
            print(distinct_ids)
            body_uri = record.get('Body')
            if not body_uri:
                logging.warning("No body URI for file id {}".format(record.get('Id', '')))
#                continue

            remote_file = record.get('Name')
            remote_file_lower = remote_file.lower()
            remote_path = "https://{}.salesforce.com{}".format(sf_pod, body_uri)
            local_file = "{}_{}".format(record.get('Id'), remote_file)
            local_path = os.path.join(new_dir, local_file)

            logging.info("Downloading {} to {}".format(remote_file, local_path))
            logging.debug("Remote URL: {}".format(remote_path))

            response = session.get(remote_path, headers=req_headers)
            if response.status_code != 200:
                logging.error("Download failed {}".format(response.status_code))
                continue
            with open(local_path, 'wb') as out_file:
                out_file.write(response.content)
        else:
            print("Photo {} already exists".format(len(distinct_ids)))


def cleanup(new_dir):
    try:
        dir_length = len(os.listdir(new_dir))
        if dir_length == 0:
            print("There was nothing in this directory so it will be deleted")
            logging.warning("There are no files in this dir. Directory will be deleted")
            os.rmdir(new_dir)
        else:
            print("Number of files in directory: {}\n".format(dir_length))
            logging.warning("Number of files in directory: {}".format(dir_length))
    except:
        dir_length = 0

    return dir_length
