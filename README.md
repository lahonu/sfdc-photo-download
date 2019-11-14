
<span style="display:block;align:center"><img src='https://static.brandfolder.com/salesforce/logo/salesforce-primary-logo.png' height='70'/></span>

# SFDC Photo Downloader

Downloads all images/files attached to a Salesforce case into a local Dropbox folder for easy viewing, sharing, or uploading for SME posts.

<p align="center">
  <img height="500" src="https://i.imgur.com/kCk58bx.png">
</p>

**Built with**
* Python
* Flask

## Installation

### Pre-Work

#### Dropbox Configuration
Download the [Dropbox Client](https://www.dropbox.com/install) and create a folder to hold the photos that are downloaded from Salesforce. This should be linked to your corporate Dropbox account. Copy the path of this folder - you will need it later.

Once created, right-click this folder and select 'View on <span>Dropbox.com</span>' and copy this URL - you will need it later.

#### Salesforce Token
If you are accustomed to using SSO and don't have a Salesforce token, please go to https://login.salesforce.com/ and click 'Forgot Your Password?' to create a password. _This password is only used for the API, and will not interfere with your SSO login._ Once you set your password, you will receive an email with your Token.

### Download and Install this application

#### Create a local folder and download the zip
Create a folder that will hold this application (this will now be referred to as the _project root folder_). Head on over to the [Releases](https://github.com/lahonu/sfdc-photo-download/releases/latest) tab and download the zip archive. Unzip this folder into your project root folder.

#### Or, clone the repository
Optionally, you can clone this repository into your project root folder.

```$ git clone https://github.com/lahonu/sfdc-photo-download.git```

### Verify Local Environment
Your setup should now look as follows:
```
My_Project_Folder
└── sfdc-photo-download-2.x
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
This file contains your personal information - edit the following variables with the information gathered in the 'Pre-Work' section.
```
SFDC_Token
Dropbox_URL
Local_Dropbox_Folder
```
**Please note** - The \ character in Local_Dropbox_Folder needs to be escaped - please enter as follows:
`C:\\Users\\username\\My_Project_Folder`

### Verify Setup

Your project root folder should now have the following structure:
```
My_Project_Folder
├── sfdc-photo-download-2.x
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
To start the application, navigate to the sfdc-photo-download-2.x and double-click the `start.bat` file. A command prompt will appear - look for `Running on http://127.0.0.1:5000/` at the bottom of the screen. This means it's now running!

Once loaded open `http://localhost:5000` in your browser to use the app.

**On first run, the app may take up to a minute to load.**


