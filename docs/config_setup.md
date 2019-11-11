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
