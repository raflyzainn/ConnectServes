from flask import Blueprint, render_template

homepageCustomer_bp = Blueprint('homepage_customer', __name__)

@homepageCustomer_bp.route('/')
def homepage_customer():
    return render_template("homepage_customer.html")