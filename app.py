from flask import Flask

from services import apis


app = Flask(__name__, template_folder="templates")
app.config.from_object('config')

apis.init_app(app)


if __name__ == '__main__':
	app.run(debug=True)