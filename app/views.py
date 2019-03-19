"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os, datetime
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash, session, abort
from app.forms import UserForm
from werkzeug.utils import secure_filename
from app.models import Profile


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/profiles/')
def profiles():
    """Render all User pages."""
    return render_template('profiles.html', accounts = db.session.query(Profile).all())


@app.route('/profile/', methods=['GET', 'POST'])
def profile():
    """Render the Add User page."""
    form = UserForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            location = request.form['location']
            gender = request.form['gender']
            bio = request.form['bio']
            currentdate = datetime.datetime.now()
            date = currentdate.strftime("%B %d, %Y")

            #photo = form.photo.data
            
            
            file = request.files['photo']
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            
            user = Profile(fname, lname, gender, email, location, bio, filename, date)
            db.session.add(user)
            db.session.commit()
            
            flash('Succesfully Uploaded', 'success')
            return redirect(url_for('profiles'))
            
    #flash_errors(form)
    return render_template('profile.html', form=form)


@app.route("/profile/<accountid>")
def accountID(accountid):
    return render_template("user.html", ac=db.session.query(Profile).filter_by(id=int(accountid)).first())
    
###
# The functions below should be applicable to all Flask apps.
###


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
