from flask import Flask, render_template, redirect, request, url_for
from flask_api import status
from config import Config
from urlGenerator import generateURL
from database import db

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def main():
    """
    Returns:
        redirect, or simply template, depending on request arguments.
    """

    if request.args:
        url: str = request.args['url']
        return render_template('index.html', url=url)
    else:
        return render_template('index.html')

@app.route('/shrt/<shortID>', methods=['GET'])
def shrt(shortID = None):
    """
    Internal redirect function for already shortened URLs.
    
    Keyword Arguments:
        shortID {str} -- ID which is already stored in database. (default: {None})
    
    Returns:
        redirect -- To the URL which is stored in database by requested ID.
    """
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


@app.route('/short', methods=['POST'])
def short():
    """
    Action for form to shorten URLs.
    
    Returns:
        redirect -- just redirecting user to the main page with shortened URL sent to index page.
    """
    url: str = request.form['url']
    url_exists = db.checkUrl(url)
    if not url_exists:
        shortened: str = generateURL()
        shortened_id: str = shortened.split('/')[2]
        db.addEntry(shortened_id, url)
        return redirect(url_for('main', url=shortened))
    else:
        return redirect(url_for('main', url=f'{Config.BASE_URL}/{url_exists}'))


if __name__ == '__main__':
    app.run()