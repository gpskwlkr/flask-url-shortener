from flask import Flask, render_template, redirect, request, url_for
from config import Config
from urlGenerator import generateURL
from database import db

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
@app.route('/<shortID>')
def main(shortID=None):
    """
    Keyword Arguments:
        shortID {str} -- Already generated ID for some URL. (default: {None})
    
    Returns:
        redirect, or template. Depending on shortID existance in the URL.
    """
    if shortID:
        try:
            '''
            To make this moment clear.

            urlGenerator() can generate an ID with only numbers in it.
            So to make everything work perfect we're just checking is it so, or not, before fetching it's URL from database.
            '''
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
    """
    Action for form to shorten URLs.
    
    Returns:
        [redirect] -- just redirecting user to the main page with shortened URL sent to index page.
    """
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