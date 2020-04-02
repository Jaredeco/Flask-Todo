from flask import Flask, render_template, request, session, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta



app = Flask(__name__)
app.secret_key = "key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class todos(db.Model):
	_id = db.Column("id", db.Integer, primary_key=True)
	todo_v = db.Column(db.String(100))
	def __init__(self, todo_v):
		self.todo_v = todo_v


@app.route('/', methods=['POST', 'GET'])
def home():
	if request.method == 'POST':
		todo = request.form['text']
		data = todos(todo)
		db.session.add(data)
		db.session.commit()
		todo_t = todos.query.all()
		return render_template("home.html", t = todo_t)
	else:
		todo_t = todos.query.all()
		return render_template("home.html", t= todo_t)

@app.route('/delete/<_id>')
def delete(_id):
	dele = todos.query.filter_by(_id=_id).first()
	db.session.delete(dele)
	db.session.commit()
	return redirect("/")


if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)
