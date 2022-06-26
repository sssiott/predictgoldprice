from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    from .views import main_views
    from .views import predict_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(predict_views.bp)
    return app


if __name__ == '__main__':
    create_app().run()