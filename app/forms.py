# -*- coding: UTF-8 -*-

from flask.ext.wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired

class FormCompress(Form):
	image = StringField('image', validators=[DataRequired()])
	size = StringField('size', validators=[DataRequired()])
	quality = StringField('quality')
	x1 = StringField('x1')
	y1 = StringField('y1')
	x2 = StringField('x2')
	y2 = StringField('y2')
	height = StringField('height')
	width = StringField('width')