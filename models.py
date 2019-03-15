from main import db


class Brand(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    namebrand = db.Column(db.String(25), unique=True, index=True)

    def __repr__(self):
        return '<Brand %r>' % self.namebrand
