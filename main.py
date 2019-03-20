from flask import Flask, render_template, url_for, session
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import Session
from models import Brand, Country, Phone
basedir = os.path.abspath(os.path.dirname(__file__))
server = Flask(__name__)
server.secret_key = 'phone'
engine = create_engine('sqlite:///' + os.path.join(
                                         basedir,
                                         'database.db?check_same_thread=False'
                                          ), echo=False)
db = Session(bind=engine)

brands = db.query(Brand.id, Brand.brandname).all()
countrys = db.query(Country.id, Country.countryname).all()
displays = db.query(Phone.id, Phone.display).group_by(Phone.display).all()
rams = db.query(Phone.id, Phone.ram).group_by(Phone.ram).all()
hdds = db.query(Phone.id, Phone.hdd).group_by(Phone.hdd).all()


@server.route('/')
@server.route('/catolog')
def index():
    session['user'] = 'my'
    phones = db.query(Phone.id, Phone.name, Phone.price, Phone.text).all()
    return render_template('index.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


@server.route('/brand/<what>')
def brand(what):
    phones = db.query(Phone.id, Phone.name, Phone.price,
                      Phone.text).filter_by(brand_id=str(what))
    return render_template('index.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


@server.route('/country/<what>')
def country(what):
    phones = db.query(Phone.id, Phone.name, Phone.price,
                      Phone.text).filter_by(country_id=str(what))
    return render_template('index.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


@server.route('/display/<what>')
def display(what):
    phones = db.query(Phone.id, Phone.name, Phone.price,
                      Phone.text).filter_by(display=str(what))
    return render_template('index.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


@server.route('/ram/<what>')
def ram(what):
    phones = db.query(Phone.id, Phone.name, Phone.price,
                      Phone.text).filter_by(ram=str(what))
    return render_template('index.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


@server.route('/hdd/<what>')
def hdd(what):
    phones = db.query(Phone.id, Phone.name, Phone.price,
                      Phone.text).filter_by(hdd=str(what))
    return render_template('index.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


@server.route('/buy/<mobile>')
def buy(mobile):
    phones = db.query(Phone.id, Phone.name, Phone.price,
                      Phone.text).filter_by(id=str(mobile))
    return render_template('buy.html',  phones=phones,
                           brands=brands, countrys=countrys, displays=displays,
                           rams=rams, hdds=hdds)


if __name__ == "__main__":
    server.run(debug=True)
