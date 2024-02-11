import psycopg2, json, uuid

# get database auth from file
database_url = open("/Users/luiswagner/Desktop/GitHub/database.txt", "r").read()

# start connection with db
conn_details = psycopg2.connect(database_url)
cursor = conn_details.cursor()


def create_example_poll():
    try:
        query = """
        INSERT INTO polls (question, answers, ip, one_per_ip, admin_key) VALUES (%s, %s, %s, %s, %s)
        """
        data = (
            "Is this a test question?",
            json.dumps({"A": "YES", "B": "MAYBE", "C": "NO", "D": "NOPE"}),
            "192.168.1.0",
            True,
            str(uuid.uuid4()),
        )
        # execute query
        cursor.execute(query, data)
        conn_details.commit()

        # close connection
        cursor.close()
        conn_details.close()
        print("Successfully created example poll in database!")
    except Exception as e:
        print(f"Error creating poll, error: {e}")


def create_example_vote():
    try:
        query = """
        INSERT INTO votes(choice, p_id, ip) VALUES (%s, %s, %s)
        """
        data = (
            "A",
            1,
            "192.168.1.0",
        )
        # execute query
        cursor.execute(query, data)
        conn_details.commit()

        # close connection
        cursor.close()
        conn_details.close()
        print("Successfully inserted example vote in database!")
    except Exception as e:
        print(f"Error adding vote, error: {e}")


def create_tables():
    try:
        query = """
            CREATE TABLE polls (
                p_id SERIAL PRIMARY KEY,
                question TEXT NOT NULL,
                answers JSON NOT NULL,
                creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                ip TEXT NOT NULL,
                one_per_ip BOOLEAN DEFAULT TRUE,
                admin_key TEXT NOT NULL,
                status BOOLEAN DEFAULT TRUE
            );
            CREATE TABLE votes (
                v_id SERIAL PRIMARY KEY,
                choice TEXT NOT NULL,
                p_id INTEGER NOT NULL,
                FOREIGN KEY (p_id) REFERENCES polls(p_id),
                ip TEXT NOT NULL,
                creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            );
        """
        # execute query
        cursor.execute(query)
        conn_details.commit()

        # close connection
        cursor.close()
        conn_details.close()
        print("Successfully created tables in database!")
    except Exception as e:
        print(f"Error creating tables, error: {e}")


# create_example_vote()
# create_tables()
create_example_poll()
