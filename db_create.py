from app import db 
from app.models import FTasks
from datetime import date 

db.create_all()

db.session.add(FTasks("Test data task", date(2013, 3, 13), 10, 1))
db.session.add(FTasks("Another test entry", date(2013, 3, 13), 10, 1))
db.session.commit()