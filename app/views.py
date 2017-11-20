from app import my_app
from flask import render_template, request
from flask.ext import flask_cache_bust
import os
from app.forms import FormCompress, FormCrop
from app.compress import compression
from app.crop import cropper



@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')

@my_app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	form1 = FormCompress()
	form2 = FormCrop()
	if request.method == 'POST':
		path = 'app/static/images/origin'
		f = request.files['file']
		f.save(os.path.join(path, f.filename))
		f.seek(0, os.SEEK_END)
		filesize = f.tell()
	return render_template('compress.html', formCompress=form1, formCrop=form2, image=f.filename, size=filesize)

# @my_app.route('/compress', methods=['GET', 'POST'])
# def compress():
# 	form1 = FormCompress()
# 	form2 = FormCrop()
# 	posts = []
# 	if form1.validate_on_submit():
# 		quality = form1.quality.data
# 		image = form1.image.data
# 		size = form1.size.data
# 		posts = compression(image, quality)
# 	return render_template('compress.html', formCompress=form1, formCrop=form2, image=image, posts=posts, size=size)

@my_app.route('/crop', methods=['GET', 'POST'])
def crop():
	form = FormCompress()
	posts = []
	if form.validate_on_submit():
		x1 = form.x1.data
		y1 = form.y1.data
		x2 = form.x2.data
		y2 = form.y2.data
		height = form.height.data
		width = form.width.data
		quality = form.quality.data
		image = form.image.data
		size = form.size.data
		posts = cropper(image, x1, y1, x2, y2, width, height)
	return render_template('compress.html', formCompress=form, image=image, posts=posts, size=size)