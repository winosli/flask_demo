import sqlite3
from db import db
from sqlalchemy.ext.declarative import declarative_base
# Model = Internal representation
# Helper - methods to retrieve some data
class AppModel(db.Model):
    __tablename__ = 'apps'

    _id = db.Column(db.String, primary_key=True)
    date = db.Column(db.String(50))
    downloads = db.Column(db.Integer)
    too = db.Column(db.Integer)
    pa = db.Column(db.String)
    mes = db.Column(db.String)

    def __init__(self, _id, date, downloads, too, pa, mes):
        self._id = _id
        self.date = date
        self.downloads = downloads
        self.too = too
        self.pa = pa
        self.mes = mes

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, _id):
        app = cls.query.filter_by(_id=_id).first()
        return app

    @classmethod
    def add_download(cls, _id):
        app = cls.query.filter_by(_id=_id).first()
        app.downloads += 1
        return app

    @classmethod
    def update_app(cls, _id, too, pa, mes):
        app = cls.query.filter_by(_id=_id).first()
        app.downloads += 1
        app.too = too
        app.pa = pa
        app.mes = mes
        return app


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    def json(self):
        return {'_id': self._id, 'date': self.date, 'downloads': self.downloads, 'too': self.too, 'pa': self.pa, 'mes': self.mes}