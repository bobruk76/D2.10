import sentry_sdk
from http import HTTPStatus

from bottle import *
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://cc4f9fa84f754680a1eb09111f558e5f@o404439.ingest.sentry.io/5268154",
    integrations=[BottleIntegration()]
)

app = Bottle()

# Static CSS Files
@app.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@app.get("/")
@view('index')
def index():
    return {}

@app.get("/fail")

def fail():
    try:
        raise RuntimeError("Произошла сгенерированная ошибка!")
    except:
        return HTTPResponse(
                status=HTTPStatus.OK)
    return {}


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)