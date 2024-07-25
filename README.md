# Aave Leveraging Calculator

Aave Leveraging Calculator is a project designed to calculate potential profits and liquidation prices on web3 lending platforms. It helps users to optimize their leveraging strategies by providing accurate and real-time calculations.

**Note:** This project is currently under development and is considered an experimental feature. Use it with caution and do not rely on it blindly for critical financial decisions.

## Features

- Calculate potential profits based on current market conditions.
- Determine the liquidation price for leveraged positions.

## Installation Guide

### Prerequisites

Ensure you have Python 3.10 installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Installing Python

#### Windows

1. Download the Python 3.10 installer from the [official website](https://www.python.org/downloads/windows/).
2. Run the installer.
3. Make sure to check the box that says "Add Python to PATH".
4. Click on "Install Now".
5. Verify the installation by opening Command Prompt and running:
   ```sh
   python --version
   ```

### Linux

1. Open a terminal
2. Update your package list:
   ```sh
   sudo apt update
   ```
3. Install Python 3.10:
   ```sh
   sudo apt install python3.10
   ```
4. Verify the installation:
   ```sh
   python --version
   ```

### Installing Pipenv

Once Python 3.10 is installed, you need to install Pipenv. Pipenv is a packaging tool for Python that combines Pip and virtualenv into a single application.

1. Open your terminal or command prompt.
2. Run the following command to install Pipenv:
   ```sh
   pip install pipenv
   ```
3. Verify the installation:
   ```sh
   pipenv --version
   ```

### Cloning the Project

To clone the Aave Leveraging Calculator repository, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
   ```sh
   git clone git@github.com:selenio032/aave-leverage-calculator.git
   ```

### Configuration

Before running the project, you may need to adjust some parameters to suit your specific needs. Open the ./aave_leveraging_calculator/constants.py file and modify the parameters as required.

1. Open your terminal or command prompt on the folder you cloned the project
2. Install packages:
   ```sh
   pipenv install
   ```

### Running the Project

After installing all the dependencies, you can run the project. Make sure you are in the virtual environment.

1. Open your terminal or command prompt on the folder you cloned the project
2. Activate the virtual environment:
   ```sh
   pipenv shell
   ```
3. Run the following command to start the application:
   ```sh
   python main.py
   ```

### Configuration

If you wish to contribute to the project, please fork the repository and create a new branch for your features or bug fixes. Submit a pull request with a clear description of your changes.
