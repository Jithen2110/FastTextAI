from flask import Flask
from service.healthCheck import *

app = Flask(__name__)

@app.route("/healthCheck")
def healthCheck():
    return getHealthCheckStatus()

if __name__ == '__main__':
    app.run()



