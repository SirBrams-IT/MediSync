MediSyncs - Health Information System- is designed to  to simulate automation and digitization of  health program , client registration, and enrollment processes. It enables efficient tracking and management of health programs and client data, optimizing healthcare delivery.

 Key Features

- Program Management: Create and manage health programs.
- Client Registration: Register and manage client information.
- Automated Enrollment: Enroll clients in relevant health programs.
- Search & Profile: Search for clients and view detailed profiles.

 Tech Stack

- Backend: Django 5.2 (Python)
- Database: SQLite (for local development)
- API: REST API

## Installation

1. Clone the repository**:
   ```bash
   git clone https://github.com/SirBrams-IT/MediSync.git
   cd MediSyncs
   
## Create and activate a virtual environment:
python -m venv medisync
medisync\Scripts\activate  # For Windows

## Install dependancies
pip install -r requirements.txt

## Run migrations
python manage.py makemigrations
python manage.py migrate
## Start the development server
python manage.py runserver
Access the application at http://127.0.0.1:8000/


API Endpoints
Create Program: POST /programs/

Data: {"name": "Program Name"}

Create Client: POST /clients/

Data: {"name": "Client Name", "age": 30}

Enroll Client: POST /enroll/

Data: {"client_id": 1, "program_id": 2}

Search Client: GET /clients/search/{name}/

Example: /clients/search/John/

Client Profile: GET /clients/profile/{id}/

Example: /clients/profile/1/
