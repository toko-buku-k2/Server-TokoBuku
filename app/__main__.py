from flask import Flask
from api import api as api_blueprint
from config import Config, connect, handle_request

app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.config.from_object(Config)
handle_request(app)
connect(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5127, debug=False)