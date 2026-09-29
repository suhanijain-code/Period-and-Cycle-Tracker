# Period & Cycle Tracker



## Project Overview

Period & Cycle Tracker is a Python project that uses Tkinter to develop an application that allows the user to input cycle information such as the last period date, cycle length, and period duration. The application makes calculations to determine the expected next period and current cycle day based on the information provided. The user can view the saved cycle data using the View History option.


The problem statement for this project is described in [statement.md](statement.md)


## Features

- Add a new cycle
- Input last period date
- Input cycle length
- Input period duration
- Calculate the expected next period
- Calculate the current cycle day
- Save cycle information
- View saved cycle information
- Validate user input
- Store cycle data in a JSON file


## Technologies Used

- Python
- Tkinter
- JSON
- Datetime

## Programming Concepts Used

- Functions
- Modules
- If-else statements

The project does not require any third-party Python packages or APIs


## Requirements

To run this project, one needs:

- Python 3.x
- Tkinter
- Visual Studio Code
- Python extension for Visual Studio Code
- The project files should be in the same folder


## Project Structure

```
Period Cycle Tracker

│── main.py
│── cycle_input.py
│── calculations.py
│── validation.py
│── storage.py
│── history.py
│── cycle_data.json
│── README.md
└── statement.md

```

## Input Format

### Last Period Date

The user should input the day, month, and year of the last period in the following format:

DD/MM/YYYY

Sample: 20/09/2026

### Cycle Length

The user should input an integer to represent the number of days of the cycle.

Sample: 28

### Period Duration

The user should input an integer to represent the period duration in days.

Sample: 5

## Setup

### 1. Installing Python

Install Python 3.x in your system. To verify whether Python is installed, open the terminal and execute the command below:

python --version

### 2. Installing Visual Studio Code

Install Visual Studio Code on your computer. Then, install the Python extension in Visual Studio Code.

### 3. Opening the Project Folder

Open Visual Studio Code and then click on the File Menu. From the File Menu, select Open Folder. From the Open Folder window, select the Period-Cycle-Tracker project folder.

### 4. Confirming the Project Files

Ensure all the files are in the Period-Cycle-Tracker folder.

The following files should be present:

- main.py
- cycle_input.py
- calculations.py
- validation.py
- storage.py
- history.py
- cycle_data.json
- README.md
- statement.md

### 5. Opening the Terminal

Click on Terminal > New Terminal in Visual Studio Code to open the terminal.

Ensure that the terminal is opened in the project folder

## How to run

Execute the command below to run the application:

python main.py

The Period & Cycle Tracker application will open.

## How to use

1. Run the application by executing the python main.py command.
2. Click on Add New Cycle.
3. Input the period date.
4. Input the cycle length.
5. Input the period duration.
6. Click Save Cycle.
7. The application calculates the expected next period and the current cycle day.
8. Click View History to view the saved cycle record.


## Data storage

The application stores the saved data in a JSON file called cycle_data.json

The project uses Python’s built-in JSON module to store and retrieve data.

## Testing

The application can be tested using the following test cases:

### Test 1: Add Cycle

Procedure:

1. Open the application

2. Click Add New Cycle

3. Input cycle information

4. Click Save Cycle

Test Criteria: A new cycle record should be added

### Test 2: Invalid Input

Procedure:

1. Input invalid cycle information

2. Click Save Cycle

Test Criteria: The application should not add invalid cycle information

### Test 3: View History

Procedure:

1. Save a new cycle record

2. Click View History

Test Criteria: The view history panel should open and display the saved cycle record

### Test 4: Data Storage

Procedure:

1. Save a cycle record

2. Close the application

3. Reopen the application

4. View History

Test Criteria: The view history panel should display the cycle record saved before closing the application

## Running from the Command Line

The application can be run from the command line by executing the python main.py command.

The application does not require any external Python packages

## Notes

- This project stores cycle records in a local JSON file

- Tkinter was used to develop the graphical user interface

- This project uses different Python files to organize the code

- This project uses Visual Studio Code as the development environment