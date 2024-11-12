from flask_app import app
app.secret_key = "Waves are breaking izquierda"
from flask_app.controllers import users
from flask_app.controllers import matchas   
from flask_app.controllers import reviews
from flask_app.controllers import bags


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port = 5001)