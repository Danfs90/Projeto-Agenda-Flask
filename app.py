import sqlite3
from flask import Flask, render_template, request, jsonify
from projeto_agenda.models import Events 
from projeto_agenda import session
from datetime import datetime
app = Flask(__name__)

app.secret_key = "danilo.dev"


@app.route('/')
def index():
    calendar = session.query(Events).all()
    
    return render_template('index.html', calendar = calendar)

@app.route("/insert",methods=["POST","GET"])
def insert():
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']

        event = Events()
        event.title = title
        event.start_event = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        event.end_event = datetime.strptime(end,"%Y-%m-%d %H:%M:%S")
        session.add(event)
        msg = 'success'
    
    return jsonify(msg)

@app.route("/update",methods=["POST","GET"])
def update():
    if request.method == 'POST':
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        id = request.form['id']
        print(title) 
        print(start) 

        msg = 'success'
    return jsonify(msg) 

@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():
    if request.method == 'POST':
        
        getid = session.query(Events).get(request.form['id'])
        session.delete(getid)
        msg = 'Record deleted successfully'
    return jsonify(msg) 

if __name__ == "__main__":
    app.run(debug=True)