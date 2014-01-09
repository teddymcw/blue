import os

from blue import app

port = int(os.environ.get('POST', 5000))
app.run(host='0.0.0.0', port=post, debug=True)
