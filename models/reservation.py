from extensions import db
from datetime import datetime


class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(200))
    time = db.Column(db.DateTime(), nullable=False)
    is_listed = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    room_id = db.Column(db.Integer(), nullable=False)

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def data(self):
        return {'id': self.id, 'name': self.name, 'description': self.description,
                'time': self.time.strftime("%d/%m/%Y %H"),
                'user_id': self.user_id, 'room_id': self.room_id}

    @classmethod
    def get_by_is_listed(cls):
        return cls.query.filter_by(is_listed=True).all()

    @classmethod
    def get_by_time(cls, time):
        return cls.query.filter_by(time=time).all()

    @classmethod
    def get_by_id(cls, reservation_id):
        return cls.query.filter_by(id=reservation_id).first()

    @classmethod
    def get_by_room_id(cls, room_id):
        return cls.query.filter_by(room_id=room_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
