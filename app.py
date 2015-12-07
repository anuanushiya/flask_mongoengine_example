import requests
from flask import Flask, render_template, jsonify, redirect, flash, url_for, request
from faker import Factory
from random import randint
from models import Page, Profile

app = Flask(__name__)


@app.route('/')
def index():
    """Gets all pages from the database."""
    pages = Page.objects
    return render_template('index.html', pages=pages)


@app.route('/page/<page_id>/')
def page(page_id):
    """Gets one page from the database."""
    page = Page.objects.get(id=page_id)
    return render_template('page.html', page=page)


@app.route('/profiles/')
def profiles():
    """Lists all profiles in the database and displays a button to fetch another one."""
    profiles = Profile.objects.order_by('-downloaded_at')
    return render_template('profiles/profiles.html', profiles=profiles)


@app.route('/profile/<profile_id>/')
def profile(profile_id):
    """Displays a profile."""
    profile = Profile.objects.get(id=profile_id)
    return render_template('profiles/profile.html', profile=profile)


@app.route('/get-profile/', methods=['GET', 'POST'])
def get_profiles():
    """Fetches some JSON and saves it in the database."""
    if request.method == 'POST':
        # Get some JSON
        r = requests.get('https://api.github.com/users/{}'.format(request.form['username']))

        # Make sure we got some JSON back
        if r.status_code != 200:
            flash("That username didn't work. Please try again.")
            return redirect(url_for(profiles))

        # Load the JSON into a Python dict
        profile_dict = r.json()

        # Create a new Profile object with Mongoengine, passing in the dict
        profile_object = Profile(raw_json=profile_dict)
        profile_object.save()

        # Prepare a message for the user
        flash('Saved a new profile.')

        # Redirect back to the profile list
        return redirect(url_for('profiles'))
    else:
        flash('That URL only accepts POST requests.')
        return redirect(url_for('profiles'))


if __name__ == '__main__':
    app.secret_key = "don't put this into the repo in production!"
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
