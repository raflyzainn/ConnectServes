from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Silakan masuk terlebih dahulu.', 'error')
            return redirect(url_for('masuk.masuk'))
        return f(*args, **kwargs)
    return decorated_function

def role_required(roles):
    def decorator(f):
        @wraps(f)
        @login_required
        def decorated_function(*args, **kwargs):
            if session.get('user_role') not in roles:
                flash('Anda tidak memiliki akses ke halaman ini.', 'error')
                return redirect(url_for('homepage'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def get_user_data():
    if 'logged_in' in session:
        return {
            'email': session.get('user_email'),
            'name': session.get('user_name'),
            'role': session.get('user_role')
        }
    return None