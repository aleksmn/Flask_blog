import os

from flask import Flask, render_template

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
    
    @app.route('/')
    def home():
        return render_template('index.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app