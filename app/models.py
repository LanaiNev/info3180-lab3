from . import db

class Profile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    gender = db.Column(db.String(10))
    email = db.Column(db.String(35))
    location = db.Column(db.String(70))
    bio = db.Column(db.String(250))
    photo = db.Column(db.String(200))
    date = db.Column(db.String(50))
    
    def __init__(self, fname, lname, gender, email, location, bio, photo, date):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.photo = photo
        self.date = date
        


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
