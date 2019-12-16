# Required Software

The document will cover information about the following:

- Terminals and Command Line Interfaces (CLI)
- Package Managers (Homebrew and Chocolatey)
- Python
- Virtual Environments
- GitHub Desktop
- Travis CLI

In order to begin you'll need to ensure that you have the following programs
and software installed:

## Terminals and Command Line interfaces

To install the necessary software, we'll be using *Command Line Interfaces*
(CLI). This is a computer term that contrasts with *Graphical User Interface*
(GUI) which is what most users are familiar with; i.e., buttons, text boxes
and graphical displays. CLIs instead can often achieve the same goals as GUIs,
but they do this by typing in a series of commands. Be certain to know how to
access your computer's CLI by following the steps below that correspond to
your operating system:

- Windows 10: Window's default command line interface is called
  [PowerShell](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/powershell).
  We'll be using this to run commands in order to install the required
  programs. The steps allow you to open PowerShell on windows
  1. Click the windows start button
  1. type "Powershell"
  1. Press enter
- macOS: on macOS we'll use the [Terminal
  App](https://support.apple.com/guide/terminal/welcome/mac)
  1. Open spotlight (⌘ + space bar)
  1. Type "Terminal"
  1. Press enter

You'll see a series of commands listed below that begin with the `$` sign. You
can simply copy and paste those commands (without the `$`) into the terminal
or powershell and press enter to execute those commands.

## Package Managers

In order to install all the software needed in a standardized and reproducible
way, we encourage the use of community organized and verified package
managers. In short, these package managers allow you to download and install
programs using commands rather than downloading and installing programs from
the internet. Follow the links below to install your package manager

### Windows: [Chocolatey](https://chocolatey.org)

Chocolatey is a relatively new package manager for Windows that allows users
to download and install software by typing commands on PowerShell. Copy and
paste the command below to install Chocolatey:

`$ Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object
System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`

### macOS: [Homebrew](https://brew.sh)

Similar to Chocolatey, homebrew allows users with macOS operating system to
manage installed packages for macOS. In contrast to Chocolatey, homebrew has
been around longer. Use the command below to install homebrew for macOS:

`$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## Python 3

**NOTE**: It is not expected that you know how to write python code, to use
this system you simply need it to run the scripts. Although, knowing some code
never hurts 😉.

[Python](https://www.python.org) is a *dynamic* scripting language used in
a variety of fields, from statistical analysis and machine learning to web
development and basic programming. In fact, the ANKI flash card app was made
using Python scripts! Check out their code
[here](https://github.com/dae/anki)! We use python scripts to automate some of
the heavy lifting when transferring data between REDCap projects and these
stored repositories and to run tests to ensure that any changes won't cause
any technical errors.

It is important to note that we utilize Python version 3. This is mentioned
because there are some version of the python programming language that are
distributed as Python 2.7. Most Apple macOS computers are already installed
with Python 2.7. Even so, you'll need to follow the instructions below to
ensure you have the appropriate version. Here we list the recommend ways to
install python based on your operating system:

- Windows: `$ choco install python`
- macOS: `$ brew install python3`

If the installation was successful, you should be able to run python by simply
typing `python` or `python3` into your terminal. Then type `exit()` to quit.

## [Virtual Environments](https://virtualenv.pypa.io/en/latest/) *Recommended*

Installing this is not required, but recommended. Because python exists in
different versions, it is nice to let your computer know what specific version
you are working with. There are python libraries and code that has been
written by others that we will use written by others using different versions
and using virtual environments ensures that we get the code that matches the
current version of Python we use. **Note:** this is only available under macOS
and linux, not Windows

Run the following command to install virtual environments for python

`$ python3 -m pip install virtualenvwrapper`

Then copy and paste the following into terminal:

```bash
printf "export WORKON_HOME=$HOME/.envs\n\nexport VIRTUALENVIRONMENT_PYTHON=$(whereis python3)\n\nfunction venv {\n\tsource /usr/local/bin/virtualenvwrapper.sh\n}\n" >> $HOME/.bash_profile
```

Now restart (close & reopen) your terminal for changes to take effect

## Git / [GitHub Desktop](http://www.itrelease.com/wp-content/uploads/2017/11/GUI-vs-CLI.png)

Git is a version control system. There are plenty of resources on the web that
give an overview of what Git is and how to use it. This section will briefly
explain why it is used in this project. See
[this](https://git-scm.com/video/what-is-version-control) video for an
introduction on the importance and use of git.

### What is Git?

Briefly, git allows us to maintain **who** made changes to **what** portions
of our REDCap data dictionary and **why**. REDCap currently logs who makes
changes, however, its logs do not tell us what, nor allow the editor to
explain the reason for the changes. Until REDCap enables features that allows
this tracking, git is an appropriate alternative.

Before downloading git, it should be noted that git, and this website,
**GitHub**, are different products/concepts, albeit they are related. Git is
a program that works on your computer and *does not* require and internet
connection. If you wanted, you could apply a version control system to any
files and folders you wanted. When you designate a new version control system
to regulate a set of files and folders, this is called a **repository**.
GitHub essentially acts as an internet server that allows users to *share* and
*synchronize* their version control systems; i.e., their repositories.

### Program to use Git 

The most common way many users use git is using the command line interface.
However, there are others who do not view this as a "user-friendly"
experience, albeit that is debatable depending on your familiarity and
experience working with command line interfaces. In this case, GitHub has
created a [GitHub Desktop](https://desktop.github.com) which has graphical
user interface (GUI) that allows users to synchronize their local repositories
with repositories stored on GitHub. For now, we recommend using this
graphical-friendly version.

**Note**: you will need a GitHub account to use this.

## [Travis](https://travis-ci.org)

Travis is a service that links with GitHub to enable *continuous integration*.
With continuous integrations, we can write programmable tests that are checked
every time we make changes to our repository or files. This allows us to
simply make changes, save our progress, and immediately receive feedback, via
Travis, indicating whether our changes broke any of our rules or tests we set
up to catch errors. Think of this as like an automated spell checker, but
instead of spelling, it's checking for whatever we need to it to check for;
i.e., valid variable names and/or branching logic, etc. Additionally, travis
enables us to encrypt files that need to be on our internet repository that
need to be stored securely. 

To install travis you'll need Ruby (Another programming language). Use this
chocolaty command:

Windows:
 - `$ choco install ruby`

macOS:
 - `$ brew install ruby`

Then use ruby to install travis:

`$ gem install travis`
