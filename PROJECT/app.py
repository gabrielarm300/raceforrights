from flask import Flask
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/templates/index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5500)