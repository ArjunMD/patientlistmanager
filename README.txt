What is the purpose of a note? Part self-organization, part communication to other providers, part comprehensive
resource, part legal document, part legal protection, part billing assistant, part education tool. Isn't that too much?
Doesn't optimzing all of them mean optimizing none of them? What if we had something just for purpose #1.


This is a simple application that allows users to manage their list of patients, their problems, and related data.
Below is a brief overview of each file:

app.py: This is the main file that starts and contains the application. It contains most of the (functions).

assessment_and_plan.py: This file contains a function auto_generate_assessment_and_plan(problem) that takes a medical
problem as an argument and returns a suggested assessment and plan template for that problem.

patient_list.html: This HTML template displays a list of patients, allowing users to add new
patients or delete existing ones. It also shows the daily to do list.

patient_detail.html: This HTML template displays detailed information about a patient, including hospital problems,
chronic problems, resolved problems, labs, micro, imaging, and an individualized to-do list. Users can add, move, or
update problems and data, as well as manage the to-do list.

The application allows users to manage patients and their associated problems and data by providing an interface to
add, delete, move, and update the information. The auto-generated assessment and plan function helps users quickly
create a predefined assessment and plan for common problems. Hopefully it will help.