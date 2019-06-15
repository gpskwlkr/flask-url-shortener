import random
import string
from config import Config
from database import db


characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', \
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', \
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def generateURL():
    """
    Generates a random bunch of characters to use as ID
    
    Returns:
        shortened_url [str] -- [Generated string used for ID later]
    """
    url: str = Config.BASE_URL
    newurl: str = ''
    for i in range(5):
        newurl += random.choice(characterList)
    if not db.checkId(newurl):
        shortened_url: str = f'{url}/{newurl}'
    else:
        generateURL()
    return shortened_url