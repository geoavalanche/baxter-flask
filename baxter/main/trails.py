"""
The trail routes to view the site
"""

from flask import (render_template,
                   Response,
                   make_response,
                   url_for,
                   current_app)

from . import main
from .. import db
from ..models import Trail


@main.route('/trails/')
def trails():
    return render_template('trails.html')


@main.route('/trails/<id>/')
def trail(id):
    trail = Trail.query.get_or_404(id)
    return render_template('trail.html', trail=trail)
