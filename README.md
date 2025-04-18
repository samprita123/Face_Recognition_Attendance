# Face Recognition Attendance System

This project is a simple face recognition-based attendance system built using Python, Flask, and face recognition libraries.

## Features

- Web interface to mark attendance
- Face recognition using images
- CSV logs for each attendance session
- Easy setup and usage

---

## Folder Structure


FaceRecognitionAttendance/

├── face_recognition/

│   └── faces/                # Add your images here
       ├── friend1.jpg
       ├── friend2.jpg
       └── ...

├── venv_name/                # Virtual environment

├── app.py

├── main.py                   # Flask app

├── index.html                # HTML for the web interface

├── 24-05-10.csv              # Example attendance logs
└── ...


---

## How to Use

### 1. Clone the Project

bash
git clone https://github.com/yourusername/FaceRecognitionAttendance.git
cd FaceRecognitionAttendance


### 2. Set Up a Virtual Environment

bash
python -m venv venv_name
source venv_name/bin/activate  # On Windows: venv_name\Scripts\activate


### 3. Install Requirements

bash
pip install face_recognition flask dlib opencv-python


### 4. Add Your Friends' Photos

- Go to the face_recognition/faces/ directory.
- Add 3-4 clear face images of your friends.
- Rename the files to match their names (e.g., john.jpg, emma.jpg).

### 5. Update the Attendance Script

In the script where face recognition is processed (your_attendance_code.py), make sure it matches image names to student names.

Example:

python
known_face_names = ["John", "Emma", "Alex"]


Match these to the filenames without extensions in faces/.

---

### 6. Run the Flask App

bash
python main.py


Visit http://127.0.0.1:5000 in your browser to see the interface and mark attendance.

---

## Output

- Attendance is saved as .csv files with timestamps.
- Each file is named by date (e.g., 24-05-18.csv).

---

## Notes

- Ensure face images are clear and well-lit.
- For best results, have only one face per image.

---

## License

MIT License

---

## Author

Your Name - [GitHub](https://github.com/samprita123)
