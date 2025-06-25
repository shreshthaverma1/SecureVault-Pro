SecureVault Pro
A password manager built using Flask + MongoDB + Encryption

**Project Overview**
SecureVault Pro is a secure and user-friendly web application designed to help users store and manage their passwords safely. Built with Flask (Python) and MongoDB, it supports user authentication, password encryption using Fernet (AES-based), and a clean dashboard to view or add credentials.
Whether you're tired of remembering multiple logins or just want a personal password vault with complete control, SecureVault Pro is for you.

Installation
1. **Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/SecureVault_Pro.git
cd SecureVault_Pro
```

2. **Create a Virtual Environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

**How to Run**
1. Set Up MongoDB
- Create a MongoDB Atlas cluster.
- Whitelist your IP address.
- Create a database named securevault.
- Create a .env file or update your config.py with:

```python
MONGO_URI = "your-mongodb-connection-string"
SECRET_KEY = "your-secret-key"
```

2. Run the Flask App
```bash
python app.py
```
```
Visit: http://localhost:5001
```

**Tech Stack and Libraries**

| Technology   | Purpose                                    |
| ------------ | ------------------------------------------ |
| **Python**   | Core backend language                      |
| **Flask**    | Lightweight web framework                  |
| **MongoDB**  | NoSQL database to store user/password data |
| **PyMongo**  | MongoDB driver for Python                  |
| **Fernet**   | Encryption/decryption of stored passwords  |
| **HTML/CSS** | Frontend design (custom signup & vault UI) |


**How It Works**
1. User Authentication:
Users can sign up and log in securely.
Session-based access control ensures vault access is protected.

2. Password Encryption:
User credentials are encrypted before storing in the DB.
AES-based Fernet ensures strong, symmetric encryption.

3. Vault Access:
Users can view, add, and manage passwords.

All entries are tied to user sessions.

**License**
This project is licensed under the MIT License. Feel free to use, modify, and distribute.

**Contact Us**
For any issues, feature requests, or feedback:
shreshthaverma1711@gmail.com


