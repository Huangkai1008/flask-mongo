from . import base


def load(app):
    app.config.from_object(base)
