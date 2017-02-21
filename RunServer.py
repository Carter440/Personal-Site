from flask import Flask, render_template, redirect, url_for
import projects
app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('CarterSlocum.html')

@app.route('/home')
def about_page():
	return redirect(url_for('home_page'))

@app.route('/resume')
def blog_page():
	return render_template('CarterResume.html')

@app.route('/projects')
def work_page():
	return render_template('CarterProjects.html', posts = projects.makePosts("ProjectPosts.txt"))

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)	