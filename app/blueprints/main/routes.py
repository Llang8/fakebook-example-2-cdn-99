from . import bp as app
from flask import render_template, request, redirect, url_for, flash
from app.blueprints.main.models import User, Post
from app import db
from flask_login import current_user, login_required

# Routes that return/display HTML

@app.route('/')
@login_required
def home():
    posts = Post.query.all()

    return render_template('home.html', user=current_user, posts=posts)

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html')

@app.route('/post', methods=['POST'])
@login_required
def create_post():
    post_title = request.form['title']
    post_body = request.form['body']
    
    new_post = Post(title=post_title, body=post_body, user_id=current_user.id)

    db.session.add(new_post)
    db.session.commit()

    flash('Post added successfully', 'success')
    return redirect(url_for('main.home'))

@app.route('/post/<id>')
def post(id):
    single_post = Post.query.get(id)
    return render_template('single-post.html', post=single_post)