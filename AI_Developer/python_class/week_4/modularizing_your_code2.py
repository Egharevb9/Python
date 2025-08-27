# Python Modules

# What a module is (a .py file that can be reused)

#  - Importing built-in modules (math, random, datetime)

#  - Writing your own module (creating my_module.py and importing it)

#  - Aliasing modules (import numpy as np)



# What is a Module?

# - A module in Python is simply a file with .py extension that contains Python code (functions, variables, or classes) which can be reused in other programs.

# - Instead of writing the same code again and again, you can write it once in a module and then import it anywhere.


# - LEts think of a module as a toolbox. Each tool (function, variable, or class) can be taken out and used whenever needed, without rebuilding the tool from scratch.


# Importing Built-in Modules

# - Python already comes with many pre-built modules that you can use directly.
# - Some common examples are:

# - math -for mathematical operations

# - random - for generating random numbers

# - datetime - for working with dates and time.
# - etc.

# - To use built in modules, you have to load them into your environment, that is, import them.

# Different Ways to Import Modules
# Import the whole module
import math


# let put it to use

print(math.sqrt(100))
#  Note that you must specify the module name when calling a function within it.

# import as an alias
import math as m

# let put it to use
print(m.sqrt(36))
# This shortens the module name, this is common with libraries like numpy, pandas, etc


#  Import specific functions or variables

from math import sqrt, pi

print(sqrt(36))
print(pi)
# - here you dont need the prefix 'math.' anymore

# Import everything from the module
from math import *

print(sqrt(49))
print(pi)
# This is usually not recommended because it can cause name conflits if two modules have functions with the same name

# Writing Your Own Module**

# - step1: Create a folder. Name it my_module

# - step2: Create a file inside the folder. Name it first.py

# - step3: Create another file inside the same folder. Name it second.py

# - Step4: Create another file still inside the same folder. Name it main.py



# here is the folder structure
# ```
# project_folder/
# │
# ├── my_module/
# │   ├── first.py
# │   ├── second.py
# │   └── main.py

# ```
# - Note that anyone with forward slash is a folder while the ones with extensions are the files.



# Python Packages

# - What a package is (a folder with __init__.py)

# - Installing and using third-party packages (pip install requests, import requests)

# - Organizing multiple modules into a package


# What is a Package?

# - A package in Python is a way to organize related modules together into a folder.

# - Inside this folder, there must be a special file called `__init__.py` (can be empty). This file tells Python that the folder should be treated as a package.

# - uhmm, let think of a package as a standard mechanic workshop, and each module is a different toolbox inside the workshop. The __init__.py file is like the label on the workshop telling passerbys that this is a mechanic workshop.

# *Do you understand?

# Third-Party Packages**

# - Python comes with some built-in modules, but you can also install extra packages created by others.

# These packages are stored in the Python Package Index (PyPI).

# We install them using pip (Python’s package manager) or conda a


# **How to Install Python Packages

# Using pip
# - This is te most common method.
# - It installs packages from PyPI. It is the Python's central package repository.

# To work with it, you ave to use it in your terminal

# ```
# pip install requests                # Install latest version

# pip install requests==2.28         # Install specific version

# pip install --upgrade requests     # Upgrade existing package

# pip uninstall requests             # Remove package
# ```


#  Using `uv`**

# - Thisi is the modern, super-fast package and project manager
# - IT is a RUST-based that unifies package installation, virtual environment and pyton version management into one fast, modern CLI.

# - To use uv

# ```
# # Run this command on your terminal depending on your OS

# Recommended method: standalone installer
 # macOS/Linux

# curl -LsSf https://astral.sh/uv/install.sh | sh

# or

# Windows

# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"  
# ```

# - After installation, verify version.

# ```
# uv --version
# ```

# - Using uv to install packages
# - But before it works you must have a workin `virtual environment` 

# ```
# uv add requests              # Install package and update project files

# uv pip install flask         # Works like pip but much faster

# uv remove requests           # Uninstall

# uv venv                      # Create a virtual environment automatically

# uv run script.py             # Run scripts in the managed environment

# ```

# -- Other package managers that you should try exploring

# | Method                            | Description                     | Best For                                 |
# | --------------------------------- | ------------------------------- | ---------------------------------------- |
# | `pip install ...`                 | Standard installation from PyPI | Most common and simple use case          |
# | `pip install -r requirements.txt` | Batch install from file         | Reproducible projects                    |
# | Virtualenv + `pip`                | Isolated environments           | Independent project setups               |
# | `conda install ...`               | Data science ecosystem          | Scientific and system-level dependencies |
# | Clone + `pip install .`           | Custom or non-PyPI packages     | Local development and experiments        |
# | `.whl install`                    | Prebuilt package install        | Faster installations                     |
# | `pip install -e .`                | Editable (development) install  | Active package development               |
# | `uv ...`                          | All-in-one modern manager       | Speed, simplicity, and full workflow     |


# Creating a virtual Environment

# What is a Virtual Environment?
# - A virtual environment (venv) is an isolated workspace where you can install and manage Python packages without affecting the global/system Python installation.

# - Each project can have its own dependencies, even if they conflict with other projects.

# - Why should you form the habit of always creating a Venv before starting a project?

#  - It keeps project dependencies separate.
#  - It prevents version conflicts.
#  - It makes collaboration easier (everyone uses the same environment).
#  - It is required in many production setups.



# How to create a Virtual Environment**

# ```
# # Create a virtual environment
# python -m venv virtual_environment_name


# # This will create a folder inside your working folder with the name "virtual_environment_name"
# ```

# - To use it, you have to activate it.
# 1. Click on the folder

# 2. Look for Script and open it.
# 3. Look for 'activate'

#4.  Right click on it and look for copy relative path

#5. Click on it.

#6.  Finally to your terminal and select Command prompt then paste the path you copied.

# Altenatively, you can use this script.

# ```
# virtual_environment_name\Scripts\activate  # For windows

#  source virtual_environment_name/bin/activate # linux or macOS
# ```

# **Deactivating a virtual Environment**
# deactivate
# ```

# **Saving and Sharing Requirements**


# ```

# # To freeze the installed packages into a file
# pip freeze > requirements.txt


# # To install them later

# pip install -r requirements.txt
# ```

# *Creating Your Package

# my_project/
# │
# ├── my_package/              # Package folder
# │   ├── __init__.py          # Makes this folder a package
# │   ├── math_utils.py        # Module 1
# │   ├── string_utils.py      # Module 2
# │
# └── main.py                  # Script that uses the package
# package




# 1.__init__.py 

# - This is a special file tells python that my_package is a package. It can be empty or used to initialize the package.

# __init__.py
print("my_package is being imported")

# Optional: import functions directly for easier access
from .math_utils import add, subtract
from .string_utils import capitalize_text


# 2. math_utils.py

# - Module for math operations