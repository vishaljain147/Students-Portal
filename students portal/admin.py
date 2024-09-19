
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'vishalkanuga'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casestudy.db'
db = SQLAlchemy(app)
database={}

# Define database models
class Login(db.Model):
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)

class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    course = db.Column(db.String(50), nullable=False)
    sec = db.Column(db.String(5), nullable=False)
    cmid = db.Column(db.String(50), unique=True, nullable=False)
    smid = db.Column(db.String(50), unique=True, nullable=False)
    byear = db.Column(db.Integer, nullable=False)
    eyear = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.String(15), nullable=False)
    bloodgroup = db.Column(db.String(10), nullable=False)
    mobileno = db.Column(db.Integer, unique=True, nullable=False)
    aadharno = db.Column(db.Integer, unique=True, nullable=False)
    fathername = db.Column(db.String(50), nullable=False)
    mothername = db.Column(db.String(50), nullable=False)
    parentmobileno = db.Column(db.Integer, unique=True, nullable=False)
    resiaddress = db.Column(db.String(60), nullable=False)
    tutorid = db.Column(db.Integer, nullable=False)
    stay = db.Column(db.String(15), nullable=False)
    gender = db.Column(db.String(5), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    district = db.Column(db.String(30), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)

class Tutor(db.Model):
    tutorid = db.Column(db.String(10), primary_key=True)
    tname = db.Column(db.String(120), nullable=False)
    tmid = db.Column(db.String(50), unique=True, nullable=False)
    mobileno = db.Column(db.Integer, unique=True, nullable=False)
    roomno = db.Column(db.Integer, nullable=False)

class Cllass(db.Model):
    cno = db.Column(db.String(10), primary_key=True)
    course = db.Column(db.String(50), nullable=False)
    sec = db.Column(db.String(5), nullable=False)
    labno1 = db.Column(db.Integer, nullable=False)
    labname1 = db.Column(db.String(50), nullable=False)
    labno2 = db.Column(db.Integer, nullable=False)
    labname2 = db.Column(db.String(50), nullable=False)
    labno3 = db.Column(db.Integer, nullable=False)
    labname3 = db.Column(db.String(50), nullable=False)

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(50), nullable=False)
    sub1 = db.Column(db.Integer, nullable=False)
    sub2 = db.Column(db.Integer, nullable=False)
    sub3 = db.Column(db.Integer, nullable=False)
    sub4 = db.Column(db.Integer, nullable=False)
    sub5 = db.Column(db.Integer, nullable=False)
    sub6 = db.Column(db.Integer, nullable=False)

class Academics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno = db.Column(db.Integer, nullable=False)
    sub1 = db.Column(db.String(5), nullable=False)
    sub2 = db.Column(db.String(5), nullable=False)
    sub3 = db.Column(db.String(5), nullable=False)
    sub4 = db.Column(db.String(5), nullable=False)
    sub5 = db.Column(db.String(5), nullable=False)
    sub6 = db.Column(db.String(5), nullable=False)
    cgpa = db.Column(db.Integer, nullable=False)

class Fees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(50), nullable=False)
    tamt = db.Column(db.Integer, nullable=False)
    tpaid = db.Column(db.Integer, nullable=False)
    tpending = db.Column(db.Integer, nullable=False)
    tduedate = db.Column(db.DateTime, nullable=False)
    eamt = db.Column(db.Integer, nullable=False)
    epaid = db.Column(db.Integer, nullable=False)
    epending = db.Column(db.Integer, nullable=False)
    eduedate = db.Column(db.DateTime, nullable=False)

class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno = db.Column(db.Integer, nullable=False)
    borrowedb = db.Column(db.Integer, nullable=False)
    returnedb = db.Column(db.Integer, nullable=False)
    reservedb = db.Column(db.Integer, nullable=False)
    totalf = db.Column(db.Integer, nullable=False)
    paid = db.Column(db.Integer, nullable=False)
    npaid = db.Column(db.Integer, nullable=False)
    duedate = db.Column(db.DateTime, nullable=False)

class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    registerno = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    roomno = db.Column(db.String(5), nullable=False)
    wname = db.Column(db.String(50), nullable=False)
    mfees = db.Column(db.Integer, nullable=False)
    paidstatus = db.Column(db.String(10), nullable=False)
    fine = db.Column(db.Integer, nullable=False)

with app.app_context():
     db.create_all()
     exe=db.session.query(Login)
     for i in exe:
          database[i.username]=i.password

# Define routes for the Flask application
@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

# Route for adding a student
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        id=request.form['id']
        registerno = request.form['registerno']
        name = request.form['name']
        course = request.form['course']
        sec=request.form['section']
        cmid=request.form['cmid']
        smid=request.form['smid']
        byear=request.form['byear']
        eyear=request.form['eyear']
        dob=request.form['dob']
        bloodgroup=request.form['bloodgroup']
        mobileno=request.form['mobileno']
        aadharno=request.form['aadharno']
        fathername=request.form['fathername']
        mothername=request.form['mothername']
        parentmobileno=request.form['parentmobileno']
        resiaddress=request.form['resiaddress']
        tutorid=request.form['tutorid']
        stay=request.form['stay']
        gender=request.form['gender']
        city=request.form['city']
        district=request.form['district']
        pincode=request.form['pincode']
        # Add other form fields similarly
        
        new_student = Details(
            registerno=registerno,
            name=name,
            course=course,
            sec=sec,
            cmid=cmid,
            smid=smid,
            byear=byear,
            eyear=eyear,
            dob=dob,
            bloodgroup=bloodgroup,
            mobileno=mobileno,
            aadharno=aadharno,
            fathername=fathername,
            mothername=mothername,
            parentmobileno=parentmobileno,
            resiaddress=resiaddress,
            tutorid=tutorid,
            stay=stay,
            gender=gender,
            city=city,
            district=district,
            pincode=pincode
             
        )
        db.session.add(new_student)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_student.html')

@app.route('/add_tutor', methods=['GET', 'POST'])
def add_tutor():
    if request.method == 'POST':
        tutorid = request.form['tutorid']
        tname = request.form['tname']
        tmid=request.form['tmid']
        mobileno=request.form['mobileno']
        roomno=request.form['roomno']
        
        
        new_tutor = Tutor(
            tutorid=tutorid,
            tname=tname,
            tmid=tmid,
            mobileno=mobileno,
            roomno=roomno
            
        )
        db.session.add(new_tutor)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_tutor.html')

@app.route('/add_academics', methods=['GET', 'POST'])
def add_academics():
    if request.method == 'POST':
        id = request.form['id']
        registerno = request.form['registerno']
        sub1 = float(request.form['sub1'])
        sub2 = float(request.form['sub2'])
        sub3 = float(request.form['sub3'])
        sub4 = float(request.form['sub4'])
        sub5 = float(request.form['sub5'])
        sub6 = float(request.form['sub6'])
        cgpa = float(request.form['cgpa'])
        
        
        new_academics = Academics(
            id=id,
            registerno=registerno,
            sub1=sub1,
            sub2=sub2,
            sub3=sub3,
            sub4=sub4,
            sub5=sub5,
            sub6=sub6,
            cgpa=cgpa            
        )
        db.session.add(new_academics)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_academics.html')

@app.route('/add_attendance', methods=['GET', 'POST'])
def add_attendance():
    if request.method == 'POST':
        id = request.form['id']
        registerno = request.form['registerno']
        course=request.form['course']
        sub1=request.form['sub1']
        sub2=request.form['sub2']
        sub3=request.form['sub3']
        sub4=request.form['sub4']
        sub5=request.form['sub5']
        sub6=request.form['sub6']
        
        
        new_attendance = Attendance(
            id=id,
            registerno=registerno,
            course=course,
            sub1=sub1,
            sub2=sub2,
            sub3=sub3,
            sub4=sub4,
            sub5=sub5,
            sub6=sub6            
        )
        db.session.add(new_attendance)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_attendance.html')

@app.route('/add_cllass', methods=['GET', 'POST'])
def add_cllass():
    if request.method == 'POST':
        cno = request.form['cno']
        course=request.form['course']
        sec=request.form['sec']
        labno1=request.form['labno1']
        labname1=request.form['labname1']
        labno2=request.form['labno2']
        labname2=request.form['labname2']
        labno3=request.form['labno3']
        labname3=request.form['labname3']
        
        
        new_cllass = Cllass(
            cno=cno,
            course=course,
            sec=sec,
            labno1=labno1,
            labname1=labname1,
            labno2=labno2,
            labname2=labname2,
            labno3=labno3,
            labname3=labname3
            
        )
        db.session.add(new_cllass)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_cllass.html')

@app.route('/add_fees', methods=['GET', 'POST'])
def add_fees():
    if request.method == 'POST':
        id = request.form['id']
        registerno=request.form['registerno']
        course=request.form['course']
        tamt=request.form['tamt']
        tpaid=request.form['tpaid']
        tpending=request.form['tpending']
        eamt=request.form['eamt']
        epaid=request.form['epaid']
        epending=request.form['epending']
        


        tduedate_date = request.form['tduedate_date']
        tduedate_time = request.form['tduedate_time']

        tduedate = datetime.strptime(tduedate_date + ' ' + tduedate_time, '%Y-%m-%d %H:%M:%S')

        eduedate_date = request.form['eduedate_date']
        eduedate_time = request.form['eduedate_time']

        eduedate = datetime.strptime(eduedate_date + ' ' + eduedate_time, '%Y-%m-%d %H:%M:%S')
        
        
        new_fees = Fees(
            id=id,
            registerno=registerno,
            course=course,
            tamt=tamt,
            tpaid=tpaid,
            tpending=tpending,
            tduedate=tduedate,
            eamt=eamt,
            epaid=epaid,
            epending=epending,
            eduedate=eduedate
            
        )
        db.session.add(new_fees)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_fees.html')

@app.route('/add_hostel', methods=['GET', 'POST'])
def add_hostel():
    if request.method == 'POST':
        id = request.form['id']
        registerno=request.form['registerno']
        name=request.form['name']
        roomno=request.form['roomno']
        wname=request.form['wname']
        mfees=request.form['mfees']
        paidstatus=request.form['paidstatus']
        fine=request.form['fine']
        
        
        
        new_hostel = Hostel(
            id=id,
            registerno=registerno,
            name=name,
            roomno=roomno,
            wname=wname,
            mfees=mfees,
            paidstatus=paidstatus,
            fine=fine
            
        )
        db.session.add(new_hostel)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_hostel.html')

@app.route('/add_library', methods=['GET', 'POST'])
def add_library():
    if request.method == 'POST':
        id = request.form['id']
        registerno=request.form['registerno']
        borrowedb=request.form['borrowedb']
        returnedb=request.form['returnedb']
        reservedb=request.form['reservedb']
        totalf=request.form['totalf']
        paid=request.form['paid']
        npaid=request.form['npaid']
        duedate_date = request.form['duedate_date']
        duedate_time = request.form['duedate_time']

        duedate = datetime.strptime(duedate_date + ' ' + duedate_time, '%Y-%m-%d %H:%M:%S')

        new_library = Library(
            id=id,
            registerno=registerno,
            borrowedb=borrowedb,
            returnedb=returnedb,
            reservedb=reservedb,
            totalf=totalf,
            paid=paid,
            npaid=npaid,
            duedate=duedate
        )
        
        db.session.add(new_library)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_library.html')

@app.route('/add_login', methods=['GET', 'POST'])
def add_login():
    if request.method == 'POST':
        username = request.form['password']
        password = request.form['username']
        
        new_login = Login(
            username=username,
            password=password
            
        )
        db.session.add(new_login)
        db.session.commit()

        return redirect(url_for('index'))
    else:
        return render_template('add_login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Login.query.filter_by(username=username, password=password).first()
        if user:
            # Storing the username in the session
            session['username'] = user.username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid username or password.')
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(port=5000)
