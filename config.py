class Configuration(object):
    DEBUG = True  # debug mode
    USE_RELOADER = True  # automatic reloader
    SECRET_KEY = 'secret key'  # something very secret
    SECURITY_PASSWORD_SALT = 'salt'  # security password salt
    SECURITY_PASSWORD_HASH = 'sha512_crypt'  # password encryption method
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable track modification notifications
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://<user>:<password>@localhost/<database_name>'  # connecting to MySQL database
