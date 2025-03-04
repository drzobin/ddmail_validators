# What is ddmail_validators
Python package for validating input for the DDMail project.

## What is DDMail
DDMail is a e-mail system/service that prioritize privacy and security. A current production example can be found at www.ddmail.se

## Operating system
Developt for and tested on debian 12.

## Building and installing using hatchling.
### Step 1: clone github repo
`git clone https://github.com/drzobin/ddmail_validators [code path]`
`cd [code path]`<br>

### Step 2: Setup python virtual environments
`python -m venv [venv path]`<br>
`source [venv path]/bin/activate`

### Step 3: Install required dependencies
`pip install -r requirements.txt`

### Step 4: Build package
`cd [code path]`<br>
`python -m pip install --upgrade build`<br>
`python -m build `<br><br>
Packages is now located under dist folder

### Step 5: Install package
`cd [code path]`<br>
`pip install dist/[package name].whl`

## Coding
Follow PEP8 and PEP257. Use Flake8 with flake8-docstrings for linting. Strive for 100% test coverage.
