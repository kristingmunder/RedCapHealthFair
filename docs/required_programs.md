# Required Software

In order to begin you'll need to ensure that you have the following programs
and software installed:

## Terminals and Command Line interfaces

To install the necessary software, we'll be using *Command Line Interfaces*
(CLI). This is a computer term that contrasts with *Graphical User Interface*
(GUI) which is what most users are familiar with; i.e., buttons, text boxes
and graphical displays. CLIs instead can often achieve the same goals as GUIs
but do this by typing in a series of commands. Be certain to know how to
access your computer's CLI:

- Windows 10:
  1. Click the windows start button
  1. type "Powershell"
  1. Press enter
- macOS:
  1. Open spotlight (⌘ + space bar)
  1. Type "Terminal"
  1. Press enter

You'll see a series of commands listed below. You can simply copy and paste
those commands into the terminal or powershell and press enter to execute
those commands.

## Package Managers

In order to install all the software needed in a standardized and reproducible
way, we encourage the use of community organized and verified package
managers. In short, these package managers allow you to download and install
programs using commands rather than downloading an install from the internet.
Follow the links below to install your package manager

- Windows: `Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`
- macOS: `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

## Python 3

[Python](https://www.python.org) is a *dynamic* scripting language used in
a variety of fields, from statistical analysis and machine learning to web
development and basic programming. In fact, the ANKI flash card app was made
using Python scripts. We use python scripts to automate some of the heavy
lifting when transferring data between REDCap projects and these stored
repositories and to run tests to ensure that any chages won't cause any
technical errors.

It is important to note that we utilize Python 3. This is mentioned because
there are some version of the python programing langauge that are distributed
as Python 2.7. Most Apple macOS computers come already installed with Python
2.7, but you'll still need to follow the instructions below to ensure you have
the appropriate version. Here we list the recommend ways to install python
based on your operating system:

- Windows: `choco install python`
- macOS: `brew install python3`
