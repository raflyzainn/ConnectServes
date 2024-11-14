from flask import Blueprint, redirect, url_for, session, flash

keluar_bp = Blueprint('keluar', __name__)

@keluar_bp.route('/keluar')
def keluar():
    session.clear()
    flash('Anda telah berhasil keluar.', 'success')
    return redirect(url_for('homepage.homepage'))  