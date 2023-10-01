from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database configuration (with SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable SQLAlchemy modification tracking

db = SQLAlchemy(app)

db.init_app(app)

# Initialize the Flask app
with app.app_context():
    db.create_all()

# Import and register the auth_routes blueprint
from routes.auth_routes import auth_bp
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)
