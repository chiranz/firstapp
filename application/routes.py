from flask import session, render_template, flash, redirect, url_for
from application import app
from application.forms import RegistrationForm, LoginForm



@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html', title="Home")


@app.route("/register",methods=["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# Shows one time message on web using success color
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('index'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'chiran@gmail.com' and form.password.data=='howareyou':
		# Shows one time message on web using success color
			flash(f'You have been succesfully logged in!', 'success')
			return redirect(url_for('index'))
		else:
			flash(f'Login Unsuccessful. Enter valid data', 'danger')
	return render_template('login.html', title='Login', form=form)