# Backend Server Documentation

## Table of Contents

- [File Structure](#file-structure)
- [Run the Server](#run-the-server)
- [Run Tests](#run-tests)
- [Development](#development)
  - [Python](#python)

## File Structure

The backend server is structured using the Model-View-Controller (MVC) architecture for improved maintainability. The key components of the file structure are:

- `models/`: Contains the data models for the application.
- `routes/`: Contains the routes that handle client requests and return responses.
- `controllers/`: Contains the logic that connects the models and routes.
- `utils/`: Contains utility functions and classes, such as audio file to MIDI conversion tools.

## Run the Server

To start the backend server, navigate to the project's server directory and run the following command:

```bash
python run.py
```

## Run Tests

To run the automated tests for the backend server, navigate to the project's server directory and run the following command:

```bash
python -m pytest
```

## Development Setup

## Python Environment Setup

All dependencies are stored in `requirements.txt`. To set up your Python environment, follow these steps:

### Create a Virtual Environment

This command creates a new virtual environment named `venv`.

```bash
python -m venv .venv
```

**1. Activate the Virtual Environment:**

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.\.venv\Scripts\activate
```

**2. Install Dependencies:**

```bash
pip install -r requirements.txt
```

This command installs all the dependencies listed in requirements.txt into your virtual environment.

**3. Update Dependencies (Optional):**

If you've added new packages during development and want to update requirements.txt, you can use:

```bash
pip freeze > requirements.txt
```

This command will overwrite requirements.txt with the current list of packages installed in your virtual environment.
