from flask import Flask
from Controllers.homepage import homepage_bp

app = Flask(__name__, template_folder='Templates', static_folder='Images')

app.register_blueprint(homepage_bp)

if __name__ == '__main__':
    app.run(debug=True)