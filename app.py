from flask import Flask, render_template, session, redirect, url_for
from config import Config
from routes.auth import auth_bp

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config.from_object(Config)
app.secret_key = app.config['SECRET_KEY']

@app.route("/test")
def test():
    print("STATIC URL:", url_for('static', filename='css/style.css'))
    return "Check console"

# Register Blueprint with a prefix
app.register_blueprint(auth_bp, url_prefix='/auth')

# Dashboard route (protected)
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/auth/login")
    return render_template("dashboard.html", username=session["username"])

# Home route (default entry)
@app.route("/")
def home():
    return redirect("/auth/login")  # or "/auth/signup"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
