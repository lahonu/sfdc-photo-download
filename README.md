
<span style="display:block;align:center"><img src='https://static.brandfolder.com/salesforce/logo/salesforce-primary-logo.png' height='100'/></span>

# SFDC Photo Downloader

Downloads all images attached to a Salesforce case into a local Dropbox folder
_Built with Python and Flask_

## Installation

### Pre-Work
The following will need to be set up to use the application:
1. A local Dropbox folder where your the case photos will be downloaded to
2. The URL of the Dropbox folder

#### Dropbox Configuration
Download the [Dropbox Client](https://www.dropbox.com/install) and create a folder that will hold the photos that you download from Salesforce. This should be configured to your corporate Dropbox account.

Once created, right-click this folder and select 'View on <span>Dropbox.com</span>' and copy this URL.

### Download and Install this application

#### Create a local folder and download the zip
Create a folder that will hold this application (this will now be referred to as the _project root folder_). Head on over to the [Releases](https://github.com/lahonu/sfdc-photo-download/releases/latest) tab and download the zip archive. Unzip this folder into the root of your project folder.

#### Or, clone the repository
Optionally, you can clone this repository into your project root folder.

#### Verify Local Environment
Your setup should now look as follows:
```
My_Project_Folder
└── sfdc-photo-download-1.0
    ├── app
    │   ├── ──pycache──
    │   ├── static
    │   ├── templates
    │   ├── ──init──.py
    │   └── sfdc.py
    ├── .env
    ├── README.md
    ├── requirements.txt
    └── sfdc.py
```
### Create Virtual Environment

In a command prompt run the following commands from the project root folder.
```
"C:\Program Files\Alteryx\bin\Miniconda3\python.exe" -m venv .\venv
```
Once that completes, also run this command from the same folder.
```
venv\Scripts\activate.bat
```
You will now see a (venv) marker at the beginning of your line which indicates you are in the virtual environment.

Now that you are working in the virtualenv, change directories into the application root folder and install the project dependencies.
```
cd sfdc-photo-download-1.0
pip install -r requirements.txt
```

### Edit the .env file
This file contains the information specific to you - edit the following variables with the information gathered in the 'Pre Work' section.
```
SFDC_Token
Dropbox_URL
Local_Dropbox_Folder
```

#### Verify Setup

If everything was successful, your project folder should now have the following structure:
```
My_Project_Folder
├── sfdc-photo-download-1.0
│   ├── app
│   │   ├── ──pycache──
│   │   ├── static
│   │   ├── templates
│   │   ├── ──init──.py
│   │   └── sfdc.py
│   ├── .env
│   ├── README.md
│   ├── requirements.txt
│   └── sfdc.py
└── venv
    ├── Include
    ├── Lib
    ├── Scripts
    ├── pip-selfcheck.json
    └── pyvenv.cfg
```
You can verify the application is working by running `flask run` in the application root folder and then visit `http://localhost:5000` in your browser.

## Using the Application
To start the application, navigate to the application folder and activate your python environment.
```
venv\Scripts\activate.bat
```

Then, change into the project root folder.
```
cd sfdc-photo-download
```

Lastly, run `flask run`. Open `http://localhost:5000` in your browser.
