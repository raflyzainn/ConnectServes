from flask import Blueprint, render_template

homepage_bp = Blueprint('homepage', __name__)

@homepage_bp.route('/')  
@homepage_bp.route('/homepage')
def homepage():
    return render_template("homepage.html")

from flask import Blueprint, render_template, request, session, redirect, url_for

masuk_bp = Blueprint('masuk', __name__)

@masuk_bp.route('/masuk', methods=['GET', 'POST'])
def masuk():
    return render_template("masuk.html")

from flask import Blueprint, render_template, request

daftar_bp = Blueprint('daftar', __name__)

@daftar_bp.route('/daftar', methods=['GET', 'POST'])
def daftar():
    return render_template("daftar.html")