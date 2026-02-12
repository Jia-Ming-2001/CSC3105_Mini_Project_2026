# CSC3105_Mini_Project_2026

Setup Instructions

Create a Virtual Environment

Open a terminal in the project root folder:

Windows (PowerShell / CMD):

python -m venv venv


Mac / Linux:

python3 -m venv venv


Activate the Virtual Environment

Windows (PowerShell):

venv\Scripts\Activate.ps1


If blocked, run once:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


Windows (Command Prompt):

venv\Scripts\activate


Mac / Linux:

source venv/bin/activate


Install Required Packages

pip install pandas numpy


Verify installation:

pip list


Run the Python Scripts

Navigate to the code folder:

cd code


Run the preprocessing script:

python CSC3105.py


Or run the dataset loader directly:

python uwb_dataset.py