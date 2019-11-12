[![Build Status](https://travis-ci.org/umdocsmedit/RedCapHealthFair.svg?branch=master)](https://travis-ci.org/umdocsmedit/RedCapHealthFair)

# REDCap Health Fair

This repository serves as the location for the REDCap data dictionary managed
by the Medical Informatics team for the South Florida Health Fairs put on by
the University of Miami Miller School of Medicine Department of Community
Service.

## Getting Started
You should only need to run through these steps once.
- [Obtain REDCap API
  Tokens](https://github.com/umdocsmedit/RedCapHealthFair/blob/master/docs/api_tokens.md) for each project of interest
- Install the [required programs](https://github.com/umdocsmedit/RedCapHealthFair/blob/master/docs/required_programs.md)
- [Create a GitHub account](https://github.com/join?source=header-home)
- [Fork the repository](https://github.com/umdocsmedit/RedCapHealthFair/blob/master/docs/fork.md)
- [Setup your configuration
  file](https://github.com/umdocsmedit/RedCapHealthFair/blob/master/docs/config_setup.md)

## Editing
Use these steps when you'd like to make and propose changes to REDCap

- Synchronize your repository with this one by making a [pull
  request](https://github.com/umdocsmedit/RedCapHealthFair/blob/master/docs/pull_request.md) to your
  forked repository
- Pull down any changes from your repository to your local machine
- Setup your python environement
    - If you decide to use virtual environment:
	    - `mkvirtualenv rchf` - this will make a new virtual environment
		  called rchf (REDCap HealthFair), you'll only need to do this the
		  first time, afterward you can simply use: `workon rchf`
	- This is also a one time thing to ensure you have all the requirements
	  for python installed `python -m pip install -r requirements.txt` 
- Synchronize your current version with MedIT Test Project, by uploading your
  data dictionary to REDCap
    - `python ./scripts/upload.py`
- Login to redcap and make your changes on the MedIT Test project
- Update the repository data by downloading back into the repo
    - `python ./scripts/download.py`
- Push changes via git to the cloud GitHub
- Make a pull request from you forked repository to this one (this step will
  require approval)
