# Virtual Environment (Recommended for macOS users, not required)

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

`$ python3 -m pip install -r requirements.txt`

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

# Setup Travis

Now that you have a repository, and you have travis installed, we can now link
travis with your cloned repository so that any changes you make, can be
checked for errors. This will require the following:

 - Enable Travis on your repository
 - Logging in to Travis in the terminal
 - Adding your API tokens to Travis

## Enable Travis on your repository

Head over to [travis-ci.org](travis-ci.org), once you've logged in with
github, head to your settings and enable this repository.

## Logging into Travis from the terminal

When installing necessary programs, you should have installed travis. To
ensure you have travis, try typing `travis` in your terminal app. To log in
use the following command:

`$ travis login`

You will be prompted to enter your GitHub username and password. Your password
will not show any asterisks, but just know that you are actually typing it in.

# Add your API tokens to Travis

Whenever you *push* changes to your new copied repository, travis will run
checks on it by running test, such as uploading your changes to the Test MedIT
project and ensure there are no errors when attempting to upload. However, in
order for travis to do this, we need to give travis the API tokens in a secure
way. Type the following commands below and replace the XXX's with your tokens:

1. `$ travis env set main_token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`
1. `$ travis env set test_token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX`

No you're all set with setting up and can now proceed to make changes to the
data dictionary
