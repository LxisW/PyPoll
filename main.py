from api.app import app
from api.utils.database_helper import DatabaseHelper

# main file to start the Flask Web-Server
database_url = open("/Users/luiswagner/Desktop/GitHub/database.txt", "r").read()

if __name__ == "__main__":
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["DATABASE_URL"] = database_url
    app.db_helper = DatabaseHelper(app.config["DATABASE_URL"])
    app.run(debug=True)  # dev
