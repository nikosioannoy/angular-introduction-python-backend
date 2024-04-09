from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from mongoengine import connect
from src.user_blueprint import user


app = Flask(__name__)
jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "super secret and difficult to guess key"

connect(
    host="mongodb+srv://cfuser:nikospro13@atlascluster.kkejasq.mongodb.net/",
    db="Coding-Factory",
    alias="coding-factory",
)

cors = CORS(
    app,
    resources={r"*": {"origins": ["http://localhost:4200"]}},
)

app.register_blueprint(user, url_prefix="/user")
