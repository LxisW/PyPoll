from api.app import app
from api.utils.database_helper import DatabaseHelper

database_url = open("/Users/luiswagner/Desktop/GitHub/database.txt", "r").read()

if __name__ == "__main__":
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True
    app.config["DATABASE_URL"] = database_url
    app.db_helper = DatabaseHelper(app.config["DATABASE_URL"])
    app.run(debug=True)  # dev

"""
TODO
Switch between only one per ip or not
Create admin link for updating poll --> close or ip setting change
"""
