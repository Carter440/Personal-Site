from flask import Flask, render_template, redirect, url_for
import projects
app = Flask(__name__)


@app.route('/')
def home_page():
	return render_template('CarterSlocum.html')

@app.route('/home')
def about_page():
	return redirect(url_for('home_page'))

@app.route('/blog')
def blog_page():
	return redirect(url_for('blog_post', post='FirstPost'))

@app.route('/blog/<post>', methods=['GET'])
def blog_post(post):
    return render_template("BlogPosts/" + post + ".html")

@app.route('/projects')
def work_page():
	return render_template('CarterProjects.html', posts = projects.makePosts("ProjectPosts.txt"))

if __name__ == "__main__":
	app.run()	