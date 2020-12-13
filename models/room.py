from extensions import db


class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    is_listed = db.Column(db.Boolean(), default=True)
    room_capacity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    def data(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'room_capacity': self.room_capacity}

    @classmethod
    def get_by_is_listed(cls):
        return cls.query.filter_by(is_listed=True).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()