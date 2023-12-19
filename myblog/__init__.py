import os

from flask import Flask

# Команда для запуска приложения
# flask --app myblog run --debug


def create_app(test_config=None):
    # создаем app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'myblog.sqlite'),
    )


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # тестовая страница
    @app.route('/hello')
    def hello():
        return 'Hello, World!'


    return app