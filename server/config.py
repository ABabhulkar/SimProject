import os


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")
    PD_GAME_FILE_PATH = os.getenv("DEV_PD_GAME_FILES")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")
    PD_GAME_FILE_PATH = os.getenv("TEST_PD_GAME_FILES")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig
}
