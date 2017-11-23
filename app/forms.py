# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, BooleanField
from wtforms.validators import DataRequired

class FormCompress(Form):
	quality = StringField('quality')

class FormCrop(Form):
	x1 = StringField('x1')
	y1 = StringField('y1')
	x2 = StringField('x2')
	y2 = StringField('y2')
	height = StringField('height')
	width = StringField('width')

class FormRotate(Form):
	vertically = BooleanField()
	horizontally = BooleanField()
	rotate = StringField('Rotate')