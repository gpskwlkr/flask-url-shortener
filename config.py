class Config(object):
    DEBUG: bool = True
    DEVELOPMENT: bool = True
    SECRET_KEY: str = 'do-i-really-need-this'
    FLASK_SECRET: str = SECRET_KEY
    TEMPLATES_AUTO_RELOAD: bool = True
    DB: str = 'urls.db'
    BASE_URL: str = 'localhost:5000'

class ProductionConfig(Config):
    DEVELOPMENT: bool = False
    DEBUG: bool = False
    TEMPLATES_AUTO_RELOAD: bool = False