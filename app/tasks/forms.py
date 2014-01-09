from flask_wtf import Form
from wtforms import TextField, DateField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired

class AddTask(Form):
	task_id = IntegerField('Priority')
	name = TextField('Task Name', validators=[DataRequired()])
	due_date = DateField('Date Due (mm/dd/yyyy)', validators=[DataRequired()], format='%m/%d/%Y')
	priority = SelectField('Priority', validators=[DataRequired()], 
		choices=[('1','1'), ('2','2'), ('3','3')])
	posted_date = DateField('Posted Date (mm/dd/yyyy)', validators=[DataRequired()], format='%m/%d/%Y')
