from app import db
from models.device import Device


class User(db.Document):
    """
    用户
    """
    name = db.StringField(max_length=30, required=True)
    password = db.StringField(max_length=30, min_length=6, required=True)
    phone = db.StringField()
    device = db.ReferenceField(Device)
    devices = db.ListField(db.ReferenceField(Device))

    def __str__(self):
        return f'name: {self.name} - phone: {self.phone}'


