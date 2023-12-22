import time
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    print('sleep start')
    time.sleep(5)
    print('sleep end')

    return 'Hello World!'

if __name__ == '__main__':
    app.run()
