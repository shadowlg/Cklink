from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

app.config.from_pyfile('cklink.cfg')

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('user'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route("/logout")
def logout():
    pass

@app.route("/register")
def register():
    pass

@app.route('/u/<uid>')
def profile(uid): 
    pass

@app.route("/link/add")
def link_add():
    pass

@app.route("/link/delete")
def link_delete():
    pass

# json format
@app.route("/link/<uid>")
def link_list(uid):
    return jsonify()

@app.route("/u/<uid>")
def user():
    pass

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///cklink.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():

    import yourapplication.models
    Base.metadata.create_all(bind=engine)

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = 
    created_time = 

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
        self.password = self.hashed(password)
        self.created_time = 

    @staticmethod
    def hashed(password):
        pass

    def __repr__(self):
        return '<User %r>' % (self.name)


class Link(Base):
    __tablename__ = 'links'
    def __init__(self):
        pass
    def __repr__(self):
        pass



if __name__ == "__main__":
    app.run()
