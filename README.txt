This is a simple Flask application that allows users to manage a list of patients, their problems, and related data.
Below is a brief overview of each file:

app.py: This is the main file that contains the Flask application. It has several routes to manage patients,
their problems, and related data. It also contains functions to load and save patient data to a JSON file called
patients.json.

assessment_and_plan.py: This file contains a function auto_generate_assessment_and_plan(problem) that takes a problem
as an argument and returns a predefined assessment and plan for that problem.

patient_list.html: This HTML template displays a list of patients with their initials, allowing users to add new
patients or delete existing ones.

patient_detail.html: This HTML template displays detailed information about a patient, including hospital problems,
chronic problems, resolved problems, labs, micro, imaging, and a to-do list. Users can add, move, or update problems
and data, as well as manage the to-do list.

The application allows users to manage patients and their associated problems and data by providing an interface to
add, delete, move, and update the information. The auto-generated assessment and plan function helps users quickly
create a predefined assessment and plan for common problems.