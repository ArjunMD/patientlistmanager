from flask import Flask, render_template, request, redirect, url_for
from assessment_and_plan import auto_generate_assessment_and_plan
import json


def load_patients():
    try:
        with open("patients.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_patients(patients):
    with open("patients.json", "w") as f:
        json.dump(patients, f, ensure_ascii=False, indent=4)


app = Flask(__name__)

patients = load_patients()


@app.route('/')
def patient_list():
    return render_template('patient_list.html', patients=patients)


@app.route('/add', methods=['POST'])
def add_patient():
    initials = request.form['initials']
    patients.append({'initials': initials, 'hospital_problems': [], 'chronic_problems': [], 'resolved_problems': [],
                     'labs': [], 'micro': [], 'imaging': []})

    save_patients(patients)
    return redirect(url_for('patient_list'))


@app.route('/delete_patient/<initials>', methods=['POST'])
def delete_patient(initials):
    global patients
    patients = [p for p in patients if p['initials'] != initials]
    save_patients(patients)  # Save the updated patients data to the JSON file
    return redirect(url_for('patient_list'))


@app.route('/patient/<initials>')
def patient_detail(initials):
    patient = [p for p in patients if p['initials'] == initials][0]
    return render_template('patient_detail.html', patient=patient)


@app.route('/patient/<initials>/add_hospital_problem', methods=['POST'])
def add_hospital_problem(initials):
    problem = request.form['problem']
    patient = [p for p in patients if p['initials'] == initials][0]
    assessment_and_plan = auto_generate_assessment_and_plan(problem)
    patient['hospital_problems'].append({'text': problem, 'assessment_and_plan': assessment_and_plan})
    save_patients(patients)
    return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/add_chronic_problem', methods=['POST'])
def add_chronic_problem(initials):
    problem = request.form['problem']
    patient = [p for p in patients if p['initials'] == initials][0]
    assessment_and_plan = auto_generate_assessment_and_plan(problem)
    patient['chronic_problems'].append({'text': problem, 'assessment_and_plan': assessment_and_plan})
    save_patients(patients)
    return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/move_problem', methods=['POST'])
def move_problem(initials):
    source = request.form['source']
    target = request.form['target']
    problem_index = int(request.form['problem_index'])
    patient = [p for p in patients if p['initials'] == initials][0]
    problem = patient[source].pop(problem_index)
    patient[target].append(problem)
    save_patients(patients)
    return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/update_assessment_and_plan', methods=['POST'])
def update_assessment_and_plan(initials):
    problem_index = int(request.form['problem_index'])
    assessment_and_plan = request.form['assessment_and_plan']
    patient = [p for p in patients if p['initials'] == initials][0]

    if problem_index < len(patient['hospital_problems']):
        problem_type = 'hospital_problems'
    elif problem_index < len(patient['hospital_problems']) + len(patient['chronic_problems']):
        problem_index -= len(patient['hospital_problems'])
        problem_type = 'chronic_problems'
    else:
        problem_index -= len(patient['hospital_problems']) + len(patient['chronic_problems'])
        problem_type = 'resolved_problems'

    patient[problem_type][problem_index]['assessment_and_plan'] = assessment_and_plan

    save_patients(patients)
    return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/add_data/<data_type>', methods=['POST'])
def add_data(initials, data_type):
    data = request.form['data']
    patient = [p for p in patients if p['initials'] == initials][0]
    patient[data_type].append(data)
    save_patients(patients)
    return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/add_todo', methods=['POST'])
def add_todo(initials):
    todo = request.form['todo']
    patient = [p for p in patients if p['initials'] == initials][0]
    patient.setdefault('todos', []).append({'text': todo, 'completed': False})
    save_patients(patients)

    from_page = request.form.get('from_page')
    if from_page == 'patient_list':
        return redirect(url_for('patient_list'))
    else:
        return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/toggle_todo/<int:todo_index>', methods=['POST'])
def toggle_todo(initials, todo_index):
    patient = [p for p in patients if p['initials'] == initials][0]
    patient['todos'][todo_index]['completed'] = not patient['todos'][todo_index]['completed']
    save_patients(patients)

    from_page = request.form.get('from_page')
    if from_page == 'patient_list':
        return redirect(url_for('patient_list'))
    else:
        return redirect(url_for('patient_detail', initials=initials))


@app.route('/patient/<initials>/clear_todos', methods=['POST'])
def clear_todos(initials):
    patient = [p for p in patients if p['initials'] == initials][0]
    patient['todos'] = []
    save_patients(patients)

    from_page = request.form.get('from_page')
    if from_page == 'patient_list':
        return redirect(url_for('patient_list'))
    else:
        return redirect(url_for('patient_detail', initials=initials))


if __name__ == '__main__':
    app.run()
