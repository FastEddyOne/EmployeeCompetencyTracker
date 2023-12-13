# Competency Tracker

Competency Tracker is a console-based application designed to manage and track the competencies of employees within an organization. It allows for recording, updating, and reporting on employee competencies and assessment results.
You can generate dummy data using this repo: https://github.com/FastEddyOne/EmployeeDataGenerator

## Features

- **User Authentication**: Secure login and logout functionality.
- **User Management**: Add, edit, view, and delete user profiles.
- **Competency Management**: Manage competencies within the organization.
- **Assessment Management**: Handle assessments related to various competencies.
- **Report Generation**: Generate summaries and detailed reports.
- **CSV Operations**: Import and export assessment results via CSV files.
- **PDF Report Generation**: Create PDF summaries for user competencies.

## Installation

To set up the Competency Tracker application, follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the application directory in your terminal or command prompt.
4. `pip install bcrypt`

## Usage

To run the application, execute the following command in the application directory: `python app.py`

### Main Menu

After logging in, users will see different menu options based on their role (user or manager):

- **For Managers**: User Management, Competency Management, Assessment Management, Report Generation, CSV Operations etc.
- **For Users**: View My Competencies.

Select the appropriate option as prompted to perform different operations.

### User Management

- `View Users`: Display a list of all users.
- `Add User`: Add a new user to the system.
- `Edit User`: Edit an existing user's profile.
- `Delete User`: Remove a user from the system.

### Competency Management

- `View Competencies`: List all competencies.
- `Add Competency`: Add a new competency.
- `Edit Competency`: Modify an existing competency.
- `Delete Competency`: Delete a competency.

### Assessment Management

- `View Assessments`: View all assessments.
- `Add Assessment`: Create a new assessment.
- `Edit Assessment`: Update an existing assessment.
- `Delete Assessment`: Remove an assessment.
- `Add Assessment Result`: Record the result of an assessment for a user.

### Report Generation

- `Generate User Competency Summary`: View a summary of competencies for a specific user.
- `Generate Competency Results Summary`: Get a summary of results for a specific competency.
- `Generate PDF User Competency Summary`: Create a PDF report of a user's competency summary.

### CSV Operations

- `Import Assessment Results from CSV`: Load assessment results from a CSV file.
- `Export Data to CSV`: Export assessment results to a CSV file.

## Contributing

Contributions to the Competency Tracker are welcome.

## License

[MIT License](LICENSE)
