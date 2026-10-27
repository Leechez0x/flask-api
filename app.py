from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/students')
def get_students():
    students = [
        {'id': 1, 'name': 'Benjamin', 'age': 21},
        {'id': 2, 'name': 'Olawura', 'age': 19},
        {'id': 3, 'name': 'Leechez Ogo', 'age': 22}
    ]
    return jsonify(students)

@app.route('/api/students/<int:student_id>')
def get_student(student_id):
    students = [
        {'id': 1, 'name': 'Benjamin', 'age': 21},
        {'id': 2, 'name': 'Olawura', 'age': 19},
        {'id': 3, 'name': 'Leechez Ogo', 'age': 22}
    ]
    for student in students:
        if student['id'] == student_id:
            return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404

if __name__ == "__main__":
    app.run(debug=True)