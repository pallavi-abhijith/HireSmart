import psycopg2
import pandas as pd
import pandas.io.sql as sqlio

class Reader():
     # Constructor for the Reader, this reads from PostgreSQL database or provides an error message.
    def __init__(self):
        try:
             self.conn = psycopg2.connect(host='ec2-54-185-158-241.us-west-2.compute.amazonaws.com', database='test_db', user='postgres', password='admin')
             self.query = self.conn.cursor()
             print("Status: Connected to database")
        except:
             print("Status: Failed to connect to database")
             self.conn = None
             self.query = None
        self.results = None
    # Method allows one to run a query to the SQL database and returns the results from that query
    def run_query(self, query):
        print("Status: Running query")
        self.results = sqlio.read_sql_query(query, self.conn)
        print("Status: COMPLETED")
        # self.query.execute(query)
        # self.results = self.query.fetchall()
        return self.results

    # Method prints out the results from the last SQL query or provides error message noting no results stored
    def print_results(self):
        if (self.results is not None):
            print("Status: no results stored")
            return
        else:
            print(self.results)
