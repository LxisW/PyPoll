import psycopg2, json, uuid
from psycopg2 import pool
from api.utils.helper import Helper


class DatabaseHelper:
    def __init__(self, database_url):
        # initialize database with pools to handle traffic better
        self.connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10, database_url)

    def get_connection(self):
        # get a connection
        return self.connection_pool.getconn()

    def put_connection(self, conn):
        self.connection_pool.putconn(conn)

    def get_poll_data(self, poll_id):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM polls WHERE p_id=%s;"
            cursor.execute(query, (poll_id,))
            results = cursor.fetchall()
            cursor.close()
            result_data = results[0]
            # print(result_data)
            poll_data = {
                "id": result_data[0],
                "question": result_data[1],
                "answers": result_data[2],
                "one_per_ip": result_data[5],
            }
            return poll_data
        except Exception as e:
            print(f"Error fetching poll data: {e}")
        finally:
            self.put_connection(conn)

    def get_votes(self, poll_id):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM votes WHERE p_id=%s"
            cursor.execute(query, (poll_id,))
            results = cursor.fetchall()
            cursor.close()
            votes = {"A": 0, "B": 0, "C": 0, "D": 0}
            for vote in results:
                key = vote[1]
                votes[key] += 1

            return votes
        except Exception as e:
            print(f"Error fetching votes: {e}")
        finally:
            self.put_connection(conn)

    def has_voted(self, ip, poll_id: int):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM votes WHERE ip = %s AND p_id=%s;",
                (ip, poll_id),
            )
            count = cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"Error checking vote: {e}")
            return False
        finally:
            self.put_connection(conn)

    def add_vote(self, poll_id, ip, choice, one_per_ip):
        success = False
        conn = self.get_connection()
        if choice not in ["A", "B", "C", "D"]:
            # invalid choice
            return False
        try:
            if not self.has_voted(ip=ip, poll_id=poll_id) or not one_per_ip:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO votes(choice, p_id, ip) VALUES (%s, %s, %s)",
                    (choice, poll_id, ip),
                )
                conn.commit()
                if cursor.rowcount == 1:
                    success = True
            else:
                success = False
        except Exception as e:
            print(f"Error checking vote: {e}")
        finally:
            self.put_connection(conn)

        return success

    def create_poll(
        self,
        question,
        answers,
        ip,
        one_per_ip,
    ):
        # Default return values
        poll_id = -1
        success = False
        admin_key = str(uuid.uuid4())

        # start connection with database
        conn = self.get_connection()

        # Convert one_per_ip to boolean
        one_per_ip = True if one_per_ip == "on" else False

        valid = Helper.check_answers(answers=answers)
        try:
            if valid:
                # Prepare and execute the SQL query
                answers_json = json.dumps(answers)
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO polls(question, answers, ip, one_per_ip, admin_key) VALUES (%s, %s, %s, %s, %s) RETURNING p_id;",
                    (question, answers_json, ip, one_per_ip, admin_key),
                )
                # Fetch the generated poll ID
                poll_id = cursor.fetchone()[0]
                conn.commit()
                success = True

            else:
                success = False
        except Exception as e:
            print(f"Error creating poll: {e}")
        finally:
            self.put_connection(conn)
        return (success, poll_id, admin_key)

    def check_admin_key(self, poll_id, admin_key):
        try:
            # dafault case
            valid = False
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT p_id FROM polls WHERE p_id=%s AND admin_key=%s"
            cursor.execute(query, (poll_id, admin_key))
            results = cursor.fetchall()
            if len(results) > 0:
                valid = True

        except Exception as e:
            print(f"Error fetching votes: {e}")

        finally:
            self.put_connection(conn)
            return valid

    def get_one_per_ip(self, poll_id):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            query = "SELECT one_per_ip FROM polls WHERE p_id=%s;"
            cursor.execute(query, (poll_id,))
            results = cursor.fetchall()
            cursor.close()
            result_data = results[0]
            one_per_ip = result_data[0]

            return one_per_ip
        except Exception as e:
            print(f"Error fetching poll data: {e}")
        finally:
            self.put_connection(conn)
