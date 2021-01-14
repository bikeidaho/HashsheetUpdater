# Overview
## HashsheetUpdater
This Python project contains scripts to retrieve current Ethereum network statistic values as well as current farm statistic values from HiveOS and records them into a google spreadsheet. It also records each of these values on a secondary sheet for historical purposes.

This project contains:  
   1. A Python script to initially populate the spreadsheet with labels and formulas in order to view and estimate your point in time rigs revenue, cost and profit over 24 Hours, 30 Days and 1 Year periods.
   1. A Python script to update the spreadsheet with current Ethereum network statistic values as well as current rig statistic values from HiveOS.
   1. A PowerShell script for use with windows task scheduler in order to automatically update data on a reoccurring schedule.

**\*\*\*The calculations presented within this spreadsheet are estimates only and not intended to be used to provide any financial advice. I am not liable for the accuracy of the calculations. This project is intended only for entertainment, educational and informational purposes.**  

### Values Updated  
|Ethereum Network Stats|HiveOS Farm Stats|
| :------------------: | :--------: |
|ETH Price USD|Rig Hash Rate|
Network Rate|Rig Power Watts|
Block Time|Power Cost KW/H|
Block Reward|Mining Probability|
Blocks 1D|Est Blocks per Month|

## Configuration and setup
   1. Prep Google
   1. Install OS specific dependencies
   1. Install HashsheetUpdater    

### Google Preparation
#### Create service account and enable permissions  
   1. Enable Programmatic Access
      1. Login to google and head to the Google Developers Console and create a new project.
      1. In the box labeled “Search for APIs and Services”, search for “Google Drive API” and enable it.
      1. In the box labeled “Search for APIs and Services”, search for “Google Sheets API” and enable it.
   1. Create Service Account
      1. Go to “APIs & Services > Credentials” and choose “Create credentials > Service account key”.
      1. Fill out the form.
      1. Click “Create key”.
      1. Select “JSON” and click “Create”.

This will automatically download a JSON file with credentials including the service account email address which you will use to 'share' with later in this setup. This file will also need to be copied into your project directory!

#### Create initial spreadsheet and prep  
   1. Log into google and create new blank spreadsheet. Also, create a second tabbed blank sheet for the historically stored values (at the bottom of the main sheet).
   The name of this spreadsheet will need to be enter later in the config.py file.
   1. Share spreadsheet with service account created in the above step. Make sure this account has editor permissions.

### Windows Preparation
#### Install Python
   1. Download Python  
   https://www.python.org/downloads/windows/

   1. Install Python

#### Install Git
   1. Download Git for Windows  
   https://gitforwindows.org/

   1. Install Git for Windows

#### Install HashsheetUpdater project
   1. Open a PowerShell prompt as Admin.  
   1. Make a new directory for project and change into it.  
   `mkdir $project_dir`  
   `cd $project_dir`  
   1. Pull most recent version of project from Github.  
   `git pull $url_project`  
   1. Copy initial config file.  
   `cp config-sample.py config.py`  
   1. Edit and populate config.py using your favorite text or code editor. (I personally use VSCode on Windows.)  
   `code config.py`  
   1. Update windows-scheduler.ps1 with project path.
   `code windows-scheduler.ps1`
   
#### Populate new spreadsheet with initial data and labels  
   1. Open PowerShell and navigate into the project directory.
   `cd $path_to_project_directory`
   1. Run the initial python script in order to populate the blank spreadsheet with headers, labels and initial data.  
   `python .\initial.py`  

#### Prepping initial spreadsheet
   1. Open the newly created and populated spreadsheet in a web browser.  
   1. Press Ctrl + A in order to select all content on the spreadsheet.  
   1. Press Ctrl + H; Find '\' and Replace with ''.
   1. Press Replace all.

#### Manually run updater to populate initial values
Navigate back to your PowerShell terminal.  
   1. Run updater script manually.  
   `python .\updater.py `

#### Tweaking initial spreadsheet - Optional  
At this point you can customize the spreadsheet to your liking.

#### Scheduling the Windows task  
   1. Open Task Scheduler as Administrator  
   1. With the Task Scheduler Library highlighted, press Create Task in the right-hand navigation panel.  
   1. On the General Tab  
      1. Populate the Name field and select the radio button 'Run whether user is logged on or not'.  
      1. Change Configure for: from Windows Vista to Windows 10.  
   1. On the Triggers Tab  
      1. Press New.  
      1. Under Settings select Daily.   
      1. Change Start to some time in the past such as 01/13/2021 12:10:00 PM. 
      1. Select checkbox Repeat task every: then change the first dropdown to 10 minutes and leave the duration of: dropdown as 1 day.  
      1. Click OK.   
   1. On the Actions Tab  
      1. Press New.  
      1. Under Program/script: the path to your powershell executable. (i.e. 'powershell.exe' or 'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'  
      1. Next to Add arguments: enter '-noexit -ExecutionPolicy Bypass -File $path_to_project\hashsheetupdater\windows-scheduler.ps1'.  
      1. Press OK.  
      1. Press OK again (You will likely be prompted for your user password at this point. This is granting the program to be run as your user account.).  

### Ubuntu 20.04 Preparation  
   1.  Install Python and Git via terminal  
   `sudo apt-get install python -y && apt-get install git -y`

#### Install HashsheetUpdater project
   1. In a terminal, make a new directory for project and change into it.  
   `mkdir $project_dir`  
   `cd $project_dir`  
   1. Pull most recent version of project from Github.  
   `git pull $url_project`  
   1. Copy initial config file.  
   `cp config-sample.py config.py`  
   1. Edit and populate config.py using your favorite text or code editor. (I personally use Vim on Linux.)  
   `vim config.py`  
   
   
#### Populate new spreadsheet with initial data and labels  
   1. In terminal, navigate into the project directory.
   `cd $path_to_project_directory`
   1. Run the initial python script in order to populate the blank spreadsheet with headers, labels and initial data.  
   `python .\initial.py`  

#### Prepping initial spreadsheet
   1. Open the newly created and populated spreadsheet in a web browser.  
   1. Press Ctrl + A in order to select all content on the spreadsheet.  
   1. Press Ctrl + H; Find '\' and Replace with ''.
   1. Press Replace all.

#### Manually run updater to populate initial values
Navigate back to your PowerShell terminal.  
   1. Run updater script manually.  
   `python .\updater.py `

#### Tweaking initial spreadsheet - Optional  
At this point you can customize the spreadsheet to your liking.

#### Scheduling the task via CRON  
   1. Make the script executable.
   `chmod u+x $path_to_script.py`
   1. In terminal, edit your crontab.
   `crontab -e`
   1.  Add the following to the end of the crontab
   `*/10 * * * * $path_to_script.py`