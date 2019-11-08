# Git

Git is a version control system. There are plenty of resources on the web that
give an overview of what Git is and how to use it. This document will briefly
explain why it is used in this project. See
[this](https://git-scm.com/video/what-is-version-control) video for an
introduction on the importance and use of git.

Briefly, git allows us to maintain **who** made changes to **what** portions
of our REDCap data dictionary and **why**. REDCap currently logs who makes
changes, however, it's logs do not tell us what, nor allow the editor to
explain the reason for the changes. Until REDCap enables features that allows
this tracking, git is an appropriate alternative.

## Using Git

Before diving into this topic, it should be noted that this website,
**GitHub**, are different products/concepts, albeit they are related. Git is
a program that works on your computer and *does not* require and internet
connection. If you wanted, you could apply a version control system to any
files and folders you wanted. GitHub essentially acts as an internet server
that allows users to *share* and *synchronize* their version control systems.

The most common way many users use git is using the command line interface.
However, there are others who do not view this as a "user-friendly"
experience, albeit that is debatable depending on your familiarity and
experience working with command line interfaces. In this case, GitHub has
created a [GitHub Desktop](https://desktop.github.com) which has graphical
user interface (GUI) that allows users to synchronize their local repositories
with repositories stored on GitHub. For now, we recommend using this
graphical-friendly version
