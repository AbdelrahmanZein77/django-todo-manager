🚀 ToDo List with Authentication

A simple Django-based ToDo List application that allows users to:

✨ Register and log in securely

✨ Create, update, toggle, and delete tasks

✨ View tasks from a clean interface

✨ Access tasks through REST API endpoints with Token Authentication

⚙️ Tech Stack

Backend: Python, Django, Django REST Framework

Database: SQLite3 (can be swapped with MySQL/PostgreSQL)

Authentication: Django Auth + DRF Token Authentication

📌 Features

User Sign Up / Login / Logout

Add and manage tasks

Task completion toggle

API endpoints secured with Token Authentication

Dynamic templates for task visualization

🚧 Status

This project is still in development 🛠️.
I’m currently improving the API part and working on adding more features.

▶️ Run Locally

Clone the repository:

git clone https://github.com/AbdelrahmanZein77/<repo-name>.git
cd <repo-name>


Create a virtual environment and activate it:

python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate  # on Linux/Mac


Install dependencies:

pip install -r requirements.txt


Run migrations and start the server:

python manage.py migrate
python manage.py runserver

📬 Future Improvements

Switch database to PostgreSQL

Add user profile and advanced authentication (JWT)

Improve frontend with modern styling (React or Bootstrap)

🔗 Author

👨‍💻 Developed by Abdelrahman Zein: [https://github.com/AbdelrahmanZein77]

📎 Connect with me on LinkedIn: [http://www.linkedin.com/in/abdelrahman-zein-35288b344]
