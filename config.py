from os import environ


class Config:
    
    TESTING = False
    DEBUG = True
    FLASK_RUN_HOST = environ.get("FLASK_RUN_HOST", "0.0.0.0")
    FLASK_RUN_PORT = environ.get("FLASK_RUN_PORT", 5000)
