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

In a terminal run the following commands from the root folder of the forked project.

Windows
```
python -m venv .\venv
```

macOS & Linux
```
python -m venv ./venv
```

Once that completes, also run this command from the same folder.

Windows
```
venv\Scripts\activate.bat
```

macOS & Linux
```
source venv/bin/activate
```

Now that you are working in the virtualenv, install the project dependencies with the following command.

```
pip install -r requirements.txt
```

### Verify Setup

In order to verify that everything is setup correctly, run the following command, which should show you the failing tests. This is good! We'll be fixing this test once we jump into the build step.

```
pytest
```

Every time you want to check your work locally you can type that command, and it will report the status of every task in the project.

### Previewing Your Work

You can preview your work by running `flask run` in the root of your fork and then visit`http://localhost:5000` in your browser.
