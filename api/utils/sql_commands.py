import psycopg2, json, uuid

database_url = open("/Users/luiswagner/Desktop/GitHub/database.txt", "r").read()

conn_details = psycopg2.connect(database_url)
cursor = conn_details.cursor()
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
    )
"""
query = """
    CREATE TABLE votes (
        v_id SERIAL PRIMARY KEY,
        choice TEXT NOT NULL,
        p_id INTEGER NOT NULL,
        FOREIGN KEY (p_id) REFERENCES polls(p_id),
        ip TEXT NOT NULL,
        creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
"""
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
cursor.execute(query, data)
conn_details.commit()
cursor.close()
conn_details.close()
