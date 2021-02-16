#!/usr/bin/env python3

from service import create_app

app = create_app()


if __name__ == "__main__":
    app.run(host=app.config["FLASK_RUN_HOST"], app.config["FLASK_RUN_PORT"], debug=app.config["DEBUG"])
