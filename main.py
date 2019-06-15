from flask import Flask, render_template, redirect, request, url_for
from config import Config
from urlGenerator import generateURL
from database import db

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/<shortID>')
def main(shortID=None):
    if shortID:
        try: 
            shortID = int(shortID)
            return redirect(db.getUrl(shortID))
        except:
            return redirect(db.getUrl(shortID))
    else:
        if request.args:
            url = request.args['url']
            return render_template('index.html', url=url)
        else:
            return render_template('index.html')

@app.route('/short', methods=['POST'])
def short():
    url = request.form['url']
    url_exists = db.checkUrl(url)
    if not url_exists:
        shortened = generateURL()
        shortened_id = shortened.split('/')[1]
        db.addEntry(shortened_id, url)
        return redirect(url_for('main', url=shortened))
    else:
        return redirect(url_for('main', url=f'{Config.BASE_URL}/{url_exists}'))


if __name__ == '__main__':
    app.run()