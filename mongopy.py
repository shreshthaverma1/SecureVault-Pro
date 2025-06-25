from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/" )
#create a database
db = client["studentsDB"]
#create a collection 
student = db["students"]

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")
    student.insert_one({"Name": name, "Age": age, "Branch": branch })
    print("Data Added Successfully!")

def view_data():
    for s in student.find():
        print(f"ID: {s['_id']} | Name: {s['name']} | Age: {s['age']} | Branch: {s['branch']}")

def search_student():
    namecheck = input("Enter Name: ")
    results = student.find({"Name": namecheck})
    found = False
    for s in results:
        print(f"ID: {s['_id']} | Name: {s['name']} | Age: {s['age']} | Branch: {s['branch']}")
        found = True
    if not found:
        print("No match found.")

def delete_student():
    id = input("Enter student ID to delete: ")
    result = student.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        print(" Deleted successfully.")
    else:
        print("ID not found.")

while True:
    print("\n1. Add Student\n2. View All\n3. Search\n4. Delete\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_data()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid option.")