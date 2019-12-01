# Virtual Environment (Recommended, not required)

Now is the time to set up the virtual environment.

1. Open the GitHub Desktop app
1. Click Repository > Open in terminal
1. turn on virtual environments: `$ venv`
1. make a new virtual environment: `$ mkvirtualenv rchf`
    - This command makes a new virtual environment and calls it `rchf` short
	for REDCap Health Fair. You can change this to whatever you'd like if you
	prefer something different

# Setting up python dependencies

The python scripts that automate some of the grunt work require you to install
some libraries. To do so copy, paste, and run the following command from
within the REDCap health fair directory:

`$ python -m pip install -r requirements.txt`

# Configuration Setup

In order to ensure that the program scripts that you have cloned into your
personal repository are capable of accessing REDCap, you will need to setup
a configuration file that holds your REDCap API Tokens. Follow the
instructions below:

1. Create a new file called `config.json` within the RedCapHealthFair folder that you cloned
    - The RedCapHealthFair folder should be located under your home folder on
	your computer > GitHub > RedCapHealthFair
1. Edit the file, and copy and paste the following text:

```json
{
	"main_token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
	"test_token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

Replace the `XXX`'s with your API tokens for new REDCAP for the `main_token`,
and your MedIT Test project token for the `test_token`

This configuration file allows travis to simulate an upload of your changes
directly to REDCap too determine if REDCap will have any errors to report when
attempting to upload the changes. However, we **DO NOT** want to upload this
configuration file to GitHub, since the API tokens are to be kept secret for
security reason! So we also need to send this data directoy to travis. To do this:

1. Open up the GitHub Desktop Application
1. Click Repository > Open in terminal
    - This will open a terminal CLI ready to work with the data
1. copy and paste this command: `$ python ./scripts/keygen.py`


