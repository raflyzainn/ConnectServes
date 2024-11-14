from flask import Blueprint, render_template

homepage_merchant_bp = Blueprint('homepage_merchant', __name__)

@homepage_merchant_bp.route('/homepage-merchant')
def homepage_merchant():
    return render_template("homepage_merchant.html")