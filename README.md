# SecureVault Pro

SecureVault Pro is a simple yet secure password manager built using Python, Flask, and MongoDB. It provides user authentication, encrypted credential storage, and a clean UI to manage saved passwords.


## Features

- User registration and authentication system
- Secure credential storage
- Interface to add and view stored passwords
- Clean, dark-themed user interface
- Structured using Flask blueprints

## Tech Stack

- **Frontend**: HTML5, CSS3
- **Backend**: Python (Flask)
- **Database**: SQLite (can be extended to use other databases)

## Project Structure
securevault_pro/
│
├── app.py                  # Main Flask application
├── config.py               # Configuration (secret key, Mongo URI)
├── mongopy.py              # MongoDB utility functions (optional)
├── requirements.txt        # Python dependencies
│
├── routes/
│   └── auth.py             # Signup, login, vault routes
│
├── templates/
│   ├── signup.html         # Signup page
│   ├── login.html          # Login page
│   ├── vault.html          # Password vault dashboard
│   └── dashboard.html      # Post-login landing page
│
├── static/
│   └── css/
│       ├── signup.css      # Signup page styling
|       ├── login.css       # login page styling
│       ├── vault.css       # Vault styling
|       └── dashboard.css   # dashboard styling


## Setup Instructions


## Setup Instructions

1. Clone the repository
git clone https://github.com/your-username/securevault-pro.git
cd securevault-pro


2. **Create a virtual environment and activate it**
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Configure environment
Edit config.py:
class Config:
    SECRET_KEY = "your-secret-key"
    MONGO_URI = "your-mongodb-uri"

5. Run the app
   python app.py


