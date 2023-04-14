from flask.templating import render_template
import random, string

from werkzeug.utils import redirect
import showdb_py, os, flask_sslify, flask_recaptcha
from flask import Flask, request
db = showdb_py.connect(user=os.environ.get('DB_USER'), password=os.environ.get('DB_PASS'))

app = Flask(__name__)
sllify = flask_sslify.SSLify(app)
recaptcha = flask_recaptcha.ReCaptcha(app, site_key='6Ld_ghAdAAAAACan9vE4SN4uQZTlzJOtDVHm-vit', secret_key=os.environ.get('CAPTCHA_SECRET'))
recaptcha.theme = 'dark'

@app.route('/<id>')
def _redir(id):
    if id in db.keys():
        return redirect(db[id])
    else:
        return '404 Not Found (invalid ID)', 404
    
@app.route('/', methods=['GET', 'POST'])
def _main_page():
    if request.method != 'POST':
        return render_template('register.html')
    if not recaptcha.verify():
        return render_template('register.html', message="You must complete the captcha.", prefill=request.form.get('link'))
    while True:
        url = ''.join(random.sample(string.ascii_letters, 5))
        if url not in db.keys(): break
    db[url] = request.form.get('link')
    return render_template('generated.html', link=f'shortened.site/{url}')
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT'), debug=True, threaded=True)