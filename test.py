from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy as sq
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = sq(app)


@app.route('/')
def hello():
	return render_template('add.html')

@app.route('/edit')
def edit():
	return render_template('edit.html')
if __name__ == "__main__":
	app.run(debug=True)