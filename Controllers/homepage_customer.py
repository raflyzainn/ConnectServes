from flask import Blueprint, render_template

homepage_customer_bp = Blueprint('homepage_customer', __name__)

@homepage_customer_bp.route('/homepage-customer')
def homepage_customer():
    return render_template("homepage_customer.html")