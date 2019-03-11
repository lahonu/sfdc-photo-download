
<span style="display:block;align:center"><img src='https://static.brandfolder.com/salesforce/logo/salesforce-primary-logo.png' height='100'/></span>

# SFDC Photo Downloader

Downloads all images attached to a Salesforce case into a local Dropbox folder

<p align="center">
  <img height="500" src="https://i.imgur.com/lsjQljB.png">
</p>

_Built with Python and Flask_

## Installation

### Pre-Work

#### Dropbox Configuration
Download the [Dropbox Client](https://www.dropbox.com/install) and create a folder that will hold the photos that are downloaded from Salesforce. This should be configured to your corporate Dropbox account. Copy the path of this folder - you will need it later.

Once created, right-click this folder and select 'View on <span>Dropbox.com</span>' and copy this URL - you will need it later.
#### Salesforce Token
You will also need your Salesforce token - if you are accustomed to using SSO and don't have a Salesforce token, please go to https://login.salesforce.com/ and click 'Forgot Your Password?' to create a password. _This password is only used for the API, and will not interfere with your SSO login._ Once you set your password, you will receive an email with your Token.

### Download and Install this application

#### Create a local folder and download the zip
Create a folder that will hold this application (this will now be referred to as the _project root folder_). Head on over to the [Releases](https://github.com/lahonu/sfdc-photo-download/releases/latest) tab and download the zip archive. Unzip this folder into the root of your project folder.

#### Or, clone the repository
Optionally, you can clone this repository into your project root folder.

#### Verify Local Environment
Your setup should now look as follows:
```
My_Project_Folder
└── sfdc-photo-download-1.x
    ├── app
    │   ├── static
    │   ├── templates
    │   ├── __init__.py
    │   └── sfdc.py
    ├── .env
    ├── install.bat
    ├── README.md
    ├── requirements.txt
    ├── sfdc.py
    └── start.bat
```
### Run install.bat
Run install.bat to install the application. It will open a command prompt window - please wait for the window to finish before continuing (this can take up to 5 minutes).

### Edit the .env file
This file contains your personal information - edit the following variables with the information gathered in the 'Pre Work' section.
```
SFDC_Token
Dropbox_URL
Local_Dropbox_Folder
```
**Please note** - The \ character in Local_Dropbox_Folder needs to be escaped - please enter it as follows:
`C:\\Users\\username\\My_Project_Folder`

#### Verify Setup

Your project folder should now have the following structure:
```
My_Project_Folder
├── sfdc-photo-download-1.x
│   ├── app
│   │   ├── static
│   │   ├── templates
│   │   ├── __init__.py
│   │   └── sfdc.py
│   ├── .env
│   ├── install.bat
│   ├── README.md
│   ├── requirements.txt
│   ├── sfdc.py
│   └── start.bat
└── venv
    ├── Include
    ├── Lib
    ├── Scripts
    ├── pip-selfcheck.json
    └── pyvenv.cfg
```

## Using the Application
To start the application, navigate to the application root folder and double-click the `start.bat` file. A command prompt will appear, and once loaded you can open `http://localhost:5000` in your browser.
