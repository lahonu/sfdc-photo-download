<span style="display:block;align:center"><img src='https://static.brandfolder.com/salesforce/logo/salesforce-primary-logo.png' height='100'/></span>

# SFDC Photo Downloader

Downloads all images attached to a Salesforce case into a local Dropbox folder
_Built with Python and Flask_
## Steps for Installing

Head on over to the 'Releases' tab and download the zip archive.
## Make the necessary changes
1. Create your local Dropbox folder
2. Create a project folder for this app to live in
3. Download the zip from this repository and place in your project folder
4. Install the python dependencies
5. Run Flask

## Verify Local Environment

### Create Virtual Environment

In a command prompt run the following commands from the root folder of the project.

```
python -m venv .\venv
```

Once that completes, also run this command from the same folder.

```
venv\Scripts\activate.bat
```

You will now see a (venv) marker at the beginning of your line which indicates you are in the virtual environment.

Now that you are working in the virtualenv, change to the project folder and install the project dependencies with the following commands.

```
cd sfdc-photo-download
pip install -r requirements.txt
```

### Verify Setup


You can verify the application is working by running `flask run` in the root of your fork and then visit`http://localhost:5000` in your browser.
