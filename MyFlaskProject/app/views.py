from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.secret_key = 'Süper gizli şifre'

db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Booking(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(100), nullable=False)
   email = db.Column(db.String(100), nullable=False)
   service = db.Column(db.String(100), nullable=False)
   date = db.Column(db.DateTime, nullable=False)
   special_request = db.Column(db.Text, nullable=True)
   def delete(self):
        db.session.delete(self)
        db.session.commit() 
   
    
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(Booking, db.session))

@app.route('/book', methods=['POST'])
def book():
   name = request.form['name']
   email = request.form['email']
   service = request.form['service']
   date_str = request.form['date']
   try:
        date = datetime.strptime(date_str, '%m/%d/%Y') if date_str else None
   except ValueError:
        # Eğer tarih çözümleme hatası alırsak, hata mesajını kontrol et
        print(f"Tarih çözümleme hatasi: {date_str}")
        date = None
   special_request = request.form['special_request']

   booking = Booking(name=name, email=email, service=service, date=date, special_request=special_request)
   db.session.add(booking)
   db.session.commit()

   return redirect(url_for('index'))


@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    new_contact = Contact(name=name, email=email, subject=subject, message=message)
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('index'))



admin.add_view(ModelView(Contact, db.session))

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/service")
def service():
    return render_template("service.html")


@app.route("/booking")
def booking():
    return render_template("booking.html")


@app.route("/team")
def team():
    return render_template("team.html")


@app.route("/testimonial")
def testimonial():
    return render_template("testimonial.html")


@app.route("/404.html")
def error():
    return render_template("404.html")



if __name__ == '__main__':
   db.create_all()
   app.run(debug=True)
   

   


