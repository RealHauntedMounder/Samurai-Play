from config import create_app


application = create_app()

from controller import routes
application.register_blueprint(routes)
if __name__ == "__main__":
    application.run(debug=True)