from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  
db = SQLAlchemy(app)
CORS(app)

class Todo(db.Model):
    sNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    
    
def __repr__(self) -> str:
    return f"{self.sNo}-{self.title}"
    
    
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/entry')
def app_entry():
    todo = Todo(title="My First Entry")
    db.session.add(todo)
    db.session.commit()
    return 'Done changes!'
    
@app.route('/show')
def show():
    all_users = Todo.query.all()
    return all_users
    
@app.route('/members')
def members():
    return {"members": ["member1", "member2", "member3", "member4"]}

if __name__ == "__main__":
    app.run(host='0.0.0.0')