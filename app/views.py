from app import my_app
from flask import render_template, request
import os
from app.forms import FormCompress, FormCrop, FormRotate
from app.compress import compression, cropper, rotation

@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')

@my_app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	form = FormCompress()
	if request.method == 'POST':
		path = 'app/static/images/origin'
		f = request.files['file']
		f.save(os.path.join(path, f.filename))
		f.seek(0, os.SEEK_END)
		filesize = f.tell()
	return render_template('compress.html', form=form, image=f.filename, size=filesize)

@my_app.route('/compress/<image>', methods=['GET', 'POST' ])
def compress(image):
	formCpr = FormCompress()
	posts = []
	size = os.path.getsize('app/static/images/origin/' + image)
	if formCpr.validate_on_submit():
		quality = formCpr.quality.data
		posts = compression(image, quality)
	return render_template('compress.html', formCpr=formCpr, image=image, posts=posts, size=size)

@my_app.route('/crop/<image>', methods=['GET', 'POST'])
def crop(image):
	formCrop = FormCrop()
	posts = []
	size = os.path.getsize('app/static/images/origin/' + image)
	if formCrop.validate_on_submit():
		x1 = formCrop.x1.data
		y1 = formCrop.y1.data
		x2 = formCrop.x2.data
		y2 = formCrop.y2.data
		height = formCrop.height.data
		width = formCrop.width.data
		posts = cropper(image, x1, y1, x2, y2, width, height)
	return render_template('compress.html', formCrop=formCrop, image=image, size=size, posts=posts)

@my_app.route('/rotate/<image>', methods=['GET', 'POST'])
def rotate(image):
	formRot = FormRotate()
	posts = []
	size = os.path.getsize('app/static/images/origin/' + image)
	if formRot.validate_on_submit():
		horizontally = formRot.horizontally.data
		vertically = formRot.vertically.data
		rot = formRot.rotate.data
		posts = rotation(image, horizontally, vertically, rot)
	return render_template('compress.html', formRot=formRot, image=image, size=size, posts=posts)