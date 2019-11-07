from app import db


class Curso(db.Model):
    __table__ = db.Model.metadata.tables['cursos']

    def __repr__(self):
        return self.nome
