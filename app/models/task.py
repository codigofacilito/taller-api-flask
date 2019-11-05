from . import db

from sqlalchemy import desc, asc
from sqlalchemy.event import listen

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, 
                            default=db.func.current_timestamp())

    @classmethod
    def new(cls, title, description, deadline):
        return Task(title=title, description=description, deadline=deadline)

    @classmethod
    def get_by_page(cls, order, page, per_page=10):
        sort = desc(Task.id) if order == 'desc' else asc(Task.id)
        return Task.query.order_by(sort).paginate(page, per_page).items

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except:
            return False

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

    def __str__(self):
        return self.title

def insert_tasks(*args, **kwargs):
    db.session.add(
        Task(title='Title 1', description='Description', deadline='2019-12-12 12:00:00')
    )
    db.session.add(
        Task(title='Title 2', description='Description', deadline='2019-12-12 12:00:00')
    )
    db.session.commit()

listen(Task.__table__, 'after_create', insert_tasks)