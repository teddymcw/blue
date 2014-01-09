from app import db

class User(db.Model):

	__tablename__ = "users"

	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String)
	password = db.Column(db.String, nullable=False)
	tasks = db.relationship('FTasks', backref='ftasks')

	def __init__(self, name=None, email=None, password=None):
		self.name = name
		self.email = email
		self.password = password


class FTasks(db.Model):

	__tablename__ = "ftasks"

	task_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	due_date = db.Column(db.Date, nullable=False)
	priority = db.Column(db.Integer, nullable=False)
	status = db.Column(db.Integer)

	def __init__(self, name, due_date, priority, status):
		self.name = name
		self.due_date = due_date
		self.priority = priority
		self.status = status

	def __repr__(self):
		#sorry but where do we get the self.body from?
		return '<name %r>' % (self.body)

