from flask import Flask
from Controllers.homepage import homepage_bp
from Controllers.masuk import masuk_bp
from Controllers.daftar import daftar_bp

app = Flask(__name__, template_folder='Templates', static_folder='Images')

app.register_blueprint(homepage_bp)
app.register_blueprint(masuk_bp)
app.register_blueprint(daftar_bp)

if __name__ == '__main__':
    app.run(debug=True)