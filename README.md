# Installation

From inside your project root directory, run the following commands to create and activate a virtual environment:

    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate # On Unix or MacOS

Install the required dependencies:

    pip install -r requirements.txt

Start the Django development server:

    python manage.py runserver

Visit `http://localhost:8000/` in your web browser to view the application.
