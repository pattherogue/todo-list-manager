# Import Flask and other necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Initialize Flask app
app = Flask(__name__, static_url_path='/static')


# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append({"task": task, "completed": False})

# Function to remove a task from the list
def remove_task(task):
    for t in tasks:
        if t["task"] == task:
            tasks.remove(t)

# Function to mark a task as completed
def mark_completed(task):
    for t in tasks:
        if t["task"] == task:
            t["completed"] = True

# Function to display the current to-do list
def get_tasks():
    return tasks

# Define routes and views
@app.route('/')
def index():
    return render_template('index.html', tasks=get_tasks())

@app.route('/add_task', methods=['POST'])
def add():
    task = request.form['task']
    add_task(task)
    return redirect(url_for('index'))

@app.route('/remove_task', methods=['POST'])
def remove():
    task = request.form['task']
    remove_task(task)
    return redirect(url_for('index'))

@app.route('/mark_completed', methods=['POST'])
def mark():
    task = request.form['task']
    mark_completed(task)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
