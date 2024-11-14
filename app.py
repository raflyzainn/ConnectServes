from flask import Flask
from flask_session import Session
from Controllers.homepage import homepage_bp
from Controllers.masuk import masuk_bp
from Controllers.daftar import daftar_bp
from Controllers.homepage_customer import homepage_customer_bp
from Controllers.keluar import keluar_bp  # Add this import
from Controllers.homepage_merchant import homepage_merchant_bp

# Initialize Flask app
app = Flask(__name__, template_folder='Templates', static_folder='Static')

# Session configuration
app.config['SECRET_KEY'] = 'c053d6febe5e4db670ce9c18762de227'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Register blueprints
app.register_blueprint(homepage_bp)
app.register_blueprint(masuk_bp)
app.register_blueprint(daftar_bp)
app.register_blueprint(homepage_customer_bp)
app.register_blueprint(keluar_bp)  # Register the logout blueprint
app.register_blueprint(homepage_merchant_bp)

if __name__ == '__main__':
    app.run(debug=True)