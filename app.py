from telegram.ext.updater import Updater
from flask import Flask
app = Flask(__name__)
updater = Updater("5243900708:AAFo-DUpJ64SoEds4DqzNQtAUIKxyxTSruQ",
                  use_context=True)
@app.route('/')
def hello_world():
    return 'Hello, World!'
