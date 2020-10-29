from server import db

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    result = db.Column(db.Integer, nullable=False)

    def __init__(self, result: int):
        self.result = result
