# REDCap API Tokens

An **A**pplication **P**rogram **I**nterface (API) is a programming concept that
some software defines, so that users can create their own software that knows
how to interact. REDCap is the application, the programs we make are the
programs, and REDCaps API is the *interface* between the two that allows
software we write to interact with REDCap data.

In order for our programs to work, we need API tokens. These tokens are
a security feature. REDCap's API works through the internet through a series
of URLs. So technically, *anyone* could access the API and mess with our
REDCap patient data! However, API tokens are the keys to accessing it.

To get a token go to the REDCap projects you need API tokens for, in the side
bar, click "API". If you already have it, your token for that project will be
displayed, if not, there should be a button to request a token. Click that
button, and wait until REDCap admins supply you with your token. **NOTE:** you
will need to do this for each project (NEW REDCAP and MedIT Test Project).
