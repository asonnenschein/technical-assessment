from flask import Flask

from flask_app import create_app

if __name__ == "__main__":
    app: Flask = create_app()
    app.run(debug=True)
