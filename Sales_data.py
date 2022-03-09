
import os
from forms import  Addsales, Delsales
from flask import Flask, render_template, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class My_db_details:
    dbuser = "root"
    dbpass = "MySQL2022"
    dbhost = "localhost"
    dbname = "tractortek_db"


conn = "mysql+pymysql://{0}:{1}@{2}/{3}".format(
        My_db_details.dbuser,
        My_db_details.dbpass,
        My_db_details.dbhost,
        My_db_details.dbname)

app.config['SQLALCHEMY_DATABASE_URI'] = conn

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Sales(db.Model):

    __tablename__ = 'sales_order'
    id = db.Column(db.Integer,primary_key = True)
    item_code = db.Column(db.VARCHAR(10))
    emp_id = db.Column(db.VARCHAR(10))
    quantity = db.Column(db.INTEGER)
    sales_entry_date = db.Column(db.DATE)

    def __init__(self,item_code,emp_id,quantity,sales_entry_date):
        self.item_code = item_code
        self.emp_id = emp_id
        self.quantity = quantity
        self.sales_entry_date = sales_entry_date


    def __repr__(self):
        return f"Item code: {self.item_code}"


############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def sales_entry():
    
    form = Addsales()

    if form.validate_on_submit():
        item_code = form.item_code.data 
        emp_id = form.emp_id.data   
        quantity = form.quantity.data
        sales_entry_date = form.sales_entry_date.data
        
        # Add sales order entry to database
        sales_entry = Sales(item_code,emp_id,quantity,sales_entry_date)
        db.session.add(sales_entry)
        db.session.commit()
        
        return redirect(url_for('index'))

    return render_template('add_sales_data.html',form=form)

@app.route('/delete', methods=['GET', 'POST'])
def del_sales():

    form = Delsales()

    if form.validate_on_submit():
        id = form.id.data
        sales_entry = Sales.query.get(id)
        db.session.delete(sales_entry)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('delete.html',form=form)
if __name__ == '__main__':
    app.run(debug=True)
