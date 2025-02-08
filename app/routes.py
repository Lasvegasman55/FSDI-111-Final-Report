from flask import (
    Flask,
    render_template,
    request as flask_request
)
import requests

app = Flask(__name__)

BACKEND_URL = "http://127.0.0.1:5000/tasks"

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/tasks") 
def task_list():   
    response = requests.get(BACKEND_URL)
    if response.status_code == 200:
        task_data = response.json().get("tasks")
        return render_template("list.html", tasks=task_data)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )
