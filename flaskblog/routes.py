from flaskblog import app
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Vaishnav',
        'title': 'Post 1',
        'content': 'Contest of post 1',
        'date_posted': 'july 20',
    },
    {
        'author': 'Indie',
        'title': 'Post 2',
        'content': 'Contest of post 2',
        'date_posted': 'july 25',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title = 'Flask-Blog About')


@app.route("/announcements")
def announcements():
    return render_template('announcements.html',title = 'Flask-Blog Announcements')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (form.password.data == 'password' and form.username.data == 'indie'):
            flash('Successfully Logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, Check Credentials', 'danger')
    return render_template('login.html', title='Log-In', form=form)
