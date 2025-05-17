from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models.link import Link
from app import db
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    links = Link.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', links=links)

@bp.route('/add_link', methods=['POST'])
@login_required
def add_link():
    url = request.form.get('url')
    if not url:
        flash('URL is required')
        return redirect(url_for('main.dashboard'))
    
    # Basic URL validation
    try:
        parsed_url = urlparse(url)
        if not all([parsed_url.scheme, parsed_url.netloc]):
            raise ValueError
    except:
        flash('Invalid URL')
        return redirect(url_for('main.dashboard'))
    
    # Check if link is safe
    category = 'safe'  # Default to safe
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else url
        else:
            title = url
    except:
        title = url
        category = 'unsafe'
    
    link = Link(
        url=url,
        title=title,
        category=category,
        user_id=current_user.id
    )
    
    db.session.add(link)
    db.session.commit()
    
    flash('Link added successfully')
    return redirect(url_for('main.dashboard'))

@bp.route('/delete_link/<int:link_id>', methods=['POST'])
@login_required
def delete_link(link_id):
    link = Link.query.get_or_404(link_id)
    if link.user_id != current_user.id:
        flash('Unauthorized')
        return redirect(url_for('main.dashboard'))
    
    db.session.delete(link)
    db.session.commit()
    flash('Link deleted successfully')
    return redirect(url_for('main.dashboard')) 