from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route("/")
@app.route("/aboutme")
def aboutme():
	return render_template('aboutme.html')

@app.route("/contact")
def contact():
	return render_template('contact.html')
@app.route("/projects")
def projects():
    return render_template('projects.html')

if __name__ == '__main__':
	app.run(debug=True)
