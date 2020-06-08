import sentry_sdk
from http import HTTPStatus

from bottle import *
from sentry_sdk.integrations.bottle import BottleIntegration
import logging

sentry_sdk.init(
    dsn="https://cc4f9fa84f754680a1eb09111f558e5f@o404439.ingest.sentry.io/5268154",
    integrations=[BottleIntegration()]
)


LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)

handler = logging.FileHandler(filename='info.log')
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

LOG.addHandler(handler)

app = Bottle()

# Static CSS Files
@app.route('/static/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='static/css')

@app.get("/")
@view('index')
def index():
    LOG.info(request.headers.get("User-Agent"))
    return {}

@app.get("/fail")
def fail():
    LOG.critical("Произошла сгенерированная ошибка!")
    raise RuntimeError("Произошла сгенерированная ошибка!")

@app.get("/success")
def fail():
    LOG.info(request.headers.get("User-Agent"))
    return HTTPResponse(
        status=HTTPStatus.OK)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)