from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Student, db
from .views import views
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth',__name__)

#################################################################################################
#                                 WE ADD USERS MANUALLY HERE                                    #
#################################################################################################

@auth.route('/create-user')
def create_user():
    from werkzeug.security import generate_password_hash
    user = User(
        firstname="Benjamin",
        email="asian@food",   
        password="1234"
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('auth.login'))
    
#################################################################################################
   

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':
      email = request.form.get('username')
      passwrd = request.form.get('password')
      
      #the if user part checks if the user email exist
      user = User.query.filter_by(email=email).first()
      
      if user:
            if  user.password == passwrd:
              login_user(user)
              flash('Login Successful',category='success') 
              return redirect(url_for('views.home'))

            else:
             flash('Invalid Password',category='error')
      else:
       flash('User Dose Not Exist!',category='error')
             
      
    return render_template("signIn-signUp.html")

@auth.route('/logout')
@login_required
def logout():
      logout_user()
      return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET','POST'])
@login_required
def signup():
      if request.method == 'POST':
           email = request.form.get('mail')
           firstname = request.form.get('name')
           lastname = request.form.get('surname')
           rollnr = request.form.get('rollnr')
           gender = request.form.get('gender')
           phonenr = request.form.get('phonenr')
           age = request.form.get('age')

           email_inuse = Student.query.filter_by(email=email).first()
           rollnr_inuse = Student.query.filter_by(rollnr=rollnr).first()
           phonenr_inuse = Student.query.filter_by(phonenr=phonenr).first()
           
           if email_inuse :
                flash('Email Is Aready In Use',category='error')
           elif phonenr_inuse:
                flash('Phone Number Already Exists',category='error')
           elif rollnr_inuse:
                flash('Roll Number Already Exists',category='error')     
           elif len(firstname) < 3:
               flash('Name must be atleast 3 characters long ', category='error')
           elif any(char.isdigit() for char in firstname):
                flash('Enter Valid Name ', category='error')
           elif len(lastname) < 3:
                flash('lastname must be atleast 3 characters long ', category='error')
           elif any(char.isdigit() for char in lastname):
                 flash('Enter Valid lastname ', category='error')
           elif len(rollnr) != 5:
                 flash('Enter Valid Roll Number ', category='error')  
           elif gender == "":
                 flash('Select a gender ', category='error')
           elif len(email) < 4:
                 flash('Enter Valid Email ', category='error')     
           elif len(phonenr) !=10:
                 flash('Enter Valid Phone Number ', category='error')
           elif int(age) < 18:
                 flash('Oops you are tu yung ', category='error')
           else:
                #Add the student details to the db
                new_student = Student(firstname=firstname,lastname=lastname,rollnr=rollnr,gender=gender,email=email,phonenr=phonenr,age=age )
                db.session.add(new_student)
                db.session.commit()
                
                flash('Student Info Registered Successfully', category='success') 
                
      return render_template("register-student.html")


    

  
