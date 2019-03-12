import json
import connexion
from config import *
# flask instance
app = connexion.App(__name__)
app.add_api('swagger.yaml')

@app.route('/')
def index():
    return json.dumps({'hello': 'world'})


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=True)
