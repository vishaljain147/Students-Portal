from flask import*
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casestudy.db'
db = SQLAlchemy(app)
database={}
class login(db.Model):
    username = db.Column(db.String(80),primary_key=True)
    password = db.Column(db.String(120), unique=True, nullable=False)
    details_f = db.relationship('details', backref='login', lazy=True)
    attendance_f = db.relationship('attendance', backref='login', lazy=True)
    academics_f = db.relationship('academics', backref='login', lazy=True)
    fees_f = db.relationship('fees', backref='login', lazy=True)
    library_f = db.relationship('library', backref='login', lazy=True)
    hostel_f = db.relationship('hostel', backref='login', lazy=True)
class details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno=db.Column(db.Integer,db.ForeignKey(login.username),unique=True,)
    name=db.Column(db.String(120), unique=False, nullable=False)
    course=db.Column(db.String(50), unique=False, nullable=False)
    sec=db.Column(db.String(5), unique=False, nullable=False)
    cmid=db.Column(db.String(50), unique=True, nullable=False)
    smid=db.Column(db.String(50), unique=True, nullable=False)
    byear=db.Column(db.Integer, unique=False, nullable=False)
    eyear=db.Column(db.Integer, unique=False, nullable=False)
    dob=db.Column(db.String(15), unique=False, nullable=False)
    bloodgroup=db.Column(db.String(10), unique=False, nullable=False)
    mobileno=db.Column(db.Integer, unique=True, nullable=False)
    aadharno=db.Column(db.Integer, unique=True, nullable=False)
    fathername=db.Column(db.String(50), unique=False, nullable=False)
    mothername=db.Column(db.String(50), unique=False, nullable=False)
    parentmobileno=db.Column(db.Integer, unique=True, nullable=False)
    resiaddress=db.Column(db.String(60), unique=False, nullable=False)
    tutorid=db.Column(db.Integer, unique=False, nullable=False)
    stay=db.Column(db.String(15), unique=False, nullable=False)
    gender=db.Column(db.String(5), unique=False, nullable=False)
    city=db.Column(db.String(30), unique=False, nullable=False)
    district=db.Column(db.String(30), unique=False, nullable=False)
    pincode=db.Column(db.Integer, unique=False, nullable=False)
    #gender,city,district,pincode
class tutor(db.Model):
    tutorid=db.Column(db.String(10),unique=True,primary_key=True)
    tname=db.Column(db.String(120), unique=False, nullable=False)
    tmid=db.Column(db.String(50), unique=True, nullable=False)
    mobileno=db.Column(db.Integer, unique=True, nullable=False)
    roomno=db.Column(db.Integer, unique=False, nullable=False)
class cllass(db.Model):
    cno=db.Column(db.String(10), primary_key=True, nullable=False)
    course=db.Column(db.String(50), unique=False, nullable=False)
    sec=db.Column(db.String(5), unique=False, nullable=False)
    labno1=db.Column(db.Integer, unique=False, nullable=False)
    labname1=db.Column(db.String(50), unique=False, nullable=False)
    labno2=db.Column(db.Integer, unique=False, nullable=False)
    labname2=db.Column(db.String(50), unique=False, nullable=False)
    labno3=db.Column(db.Integer, unique=False, nullable=False)
    labname3=db.Column(db.String(50), unique=False, nullable=False)
class attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno=db.Column(db.Integer,db.ForeignKey(login.username), unique=True)
    course=db.Column(db.String(50), unique=False, nullable=False)
    sub1=db.Column(db.Integer, unique=False, nullable=False)
    sub2=db.Column(db.Integer, unique=False, nullable=False)
    sub3=db.Column(db.Integer, unique=False, nullable=False)
    sub4=db.Column(db.Integer, unique=False, nullable=False)
    sub5=db.Column(db.Integer, unique=False, nullable=False)
    sub6=db.Column(db.Integer, unique=False, nullable=False)
class academics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno=db.Column(db.Integer, db.ForeignKey(login.username),unique=True)
    sub1=db.Column(db.String(5), unique=False, nullable=False)
    sub2=db.Column(db.String(5), unique=False, nullable=False)
    sub3=db.Column(db.String(5), unique=False, nullable=False)
    sub4=db.Column(db.String(5), unique=False, nullable=False)
    sub5=db.Column(db.String(5), unique=False, nullable=False)
    sub6=db.Column(db.String(5), unique=False, nullable=False)
    cgpa=db.Column(db.Integer, unique=False, nullable=False)   
class fees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno=db.Column(db.Integer,db.ForeignKey(login.username), unique=True)
    course=db.Column(db.String(50), unique=False, nullable=False)
    tamt=db.Column(db.Integer, unique=False, nullable=False)
    tpaid=db.Column(db.Integer, unique=False, nullable=False)
    tpending=db.Column(db.Integer, unique=False, nullable=False)
    tduedate=db.Column(db.DateTime, unique=False, nullable=False)
    eamt=db.Column(db.Integer, unique=False, nullable=False)
    epaid=db.Column(db.Integer, unique=False, nullable=False)
    epending=db.Column(db.Integer, unique=False, nullable=False)
    eduedate=db.Column(db.DateTime, unique=False, nullable=False)

class library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno=db.Column(db.Integer, db.ForeignKey(login.username),unique=True )
    borrowedb=db.Column(db.Integer, unique=False, primary_key=False)
    returnedb=db.Column(db.Integer, unique=False, primary_key=False)
    reservedb=db.Column(db.Integer, unique=False, primary_key=False)
    totalf=db.Column(db.Integer, unique=False, primary_key=False)
    paid=db.Column(db.Integer, unique=False, primary_key=False)
    npaid=db.Column(db.Integer, unique=False, primary_key=False)
    duedate=db.Column(db.DateTime, unique=False, nullable=False)
class hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno=db.Column(db.Integer,db.ForeignKey(login.username), unique=True)
    name=db.Column(db.String(120), unique=False, primary_key=False)
    roomno=db.Column(db.String(5), unique=False, primary_key=False)
    wname=db.Column(db.String(50), unique=False, primary_key=False)
    mfees=db.Column(db.Integer, unique=False, primary_key=False)
    paidstatus=db.Column(db.String(10), unique=False, primary_key=False)
    fine=db.Column(db.Integer, unique=False, primary_key=False)
with app.app_context():
     db.create_all()
     exe=db.session.query(login)
     for i in exe:
          database[i.username]=i.password
@app.route('/')
def initail():
    return render_template('practice.html')
@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['Username']
    pwd=request.form['Password']
    if name1 not in database:
         return render_template('practice.html',info='Invalid User')
    else:
        if database[name1]!=pwd:
            return render_template('practice.html',info='Invalid Password')
        else:
            database.clear()
            database[name1]=pwd
            a=db.session.query(details).all()
            return render_template('home.html', ptr=a,k=int(name1))
@app.route('/forget.html')
def forget():
    return render_template('forget.html')
@app.route("/form_forget",methods=['POST','GET'])
def defpass():
    regnum=request.form['registernumber']
    mobnum=request.form['mobilenumber']
    check=db.session.execute(login).filter_by(username==int(regnum))
    print(check)
@app.route('/details.html')
def detail():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(details).all()
    return render_template('details.html', ptr=a,k=k)
@app.route('/tutor.html')
def tutorr():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a = db.session.query(tutor,details).join(details,tutor.tutorid==details.tutorid).all()
    for i,j in a:
        print(i.tutorid,j.registerno)
    return render_template('tutor.html',ptr=a,k=k)
@app.route('/cllass.html')
def cllasss():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(cllass,details).join(details,cllass.sec==details.sec).all()
    for i,j in a:
        print(i.cno,j.name)
    return render_template('cllass.html',ptr=a,k=k)
@app.route('/attendance.html')
def attendancee():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(attendance).all()
    return render_template('attendance.html',ptr=a,k=k)
@app.route('/academics.html')
def academicss():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(academics).all()
    return render_template('academics.html',ptr=a,k=k)
@app.route('/fees.html')
def feess():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(fees).all()
    return render_template('fees.html',ptr=a,k=k)
@app.route('/library.html')
def libraryy():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(library).all()
    return render_template('library.html',ptr=a,k=k)
@app.route('/hostel.html')
def hostell():
    k=0
    value=database.keys()
    for i in value:
        k=int(i)
    a=db.session.query(hostel).all()
    return render_template('hostel.html',ptr=a,k=k)
@app.route('/practice.html')
def practice():
    return render_template('practice.html')
if __name__ == '__main__':
    app.run()

