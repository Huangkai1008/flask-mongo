from app import db


class Device(db.Document):
    """
    设备
    """
    device_name = db.StringField()
    mac_address = db.StringField()

    def __str__(self):
        return f'device_name:{self.device_name} - mac_address: {self.mac_address}'
