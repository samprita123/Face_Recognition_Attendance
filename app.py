from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mark-attendance', methods=['POST'])
def mark_attendance():
    # Run your Python attendance code
    subprocess.run(['python', 'your_attendance_code.py'])

    # Return a response
    return jsonify({'message': 'Attendance marked successfully'})

if __name__ == '__main__':
    app.run(debug=True)
