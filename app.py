from flask import Flask
from app_factory import create_app
from flaskr.routes.world import bp

app = Flask(__name__)
create_app(app)

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run()
