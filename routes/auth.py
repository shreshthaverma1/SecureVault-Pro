from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient
import bcrypt
from config import Config 
from bson.objectid import ObjectId

# Blueprint setup
auth_bp = Blueprint("auth", __name__)

# MongoDB connection
mongo = MongoClient(Config.MONGO_URI)
db = mongo["securevault"]
users = db["users"]

# ---------------- SIGNUP ROUTE ----------------
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if email already exists
        if users.find_one({"email": email}):
            flash("Email is already registered. Try logging in!")
            return redirect(url_for("auth.signup"))

        # Hash the password and save the user
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert_one({
            "username": username,
            "email": email,
            "password_hash": hashed_pw,
            "vault": []  
        })

        flash("Signup successful! Please login.")
        return redirect(url_for("auth.login"))

    return render_template("signup.html")

# ---------------- LOGIN ROUTE ----------------
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = users.find_one({"email": email})
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password_hash"]):
            session["user"] = str(user["_id"])
            session["username"] = user["username"]
            flash("Login successful!")
            return redirect("/dashboard")  # Safe and direct redirect
        else:
            flash("Invalid email or password")
            return redirect(url_for("auth.login"))

    return render_template("login.html")

# ---------------- LOGOUT ROUTE ----------------
@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!")
    return redirect(url_for("auth.login"))




@auth_bp.route("/vault")
def vault():
    if "user" not in session:
        flash("Please log in first.")
        return redirect(url_for("auth.login"))

    print("Session ID:", session.get("user"))  

    user = users.find_one({"_id": ObjectId(session["user"])})
    print("Fetched user:", user)  

    if not user:
        flash("User not found.")
        return redirect(url_for("auth.login"))

    return render_template("vault.html", username=session["username"], vault=user["vault"])


@auth_bp.route("/add-password", methods=["POST"])
def add_password():
    if "user" not in session:
        return redirect(url_for("auth.login"))

    site = request.form["site"]
    username = request.form["username"]
    password = request.form["password"]

    users.update_one(
        {"_id": ObjectId(session["user"])},
        {"$push": {"vault": {
            "site": site,
            "username": username,
            "password": password
        }}}
    )

    flash("Password added successfully!")
    return redirect(url_for("auth.vault"))
