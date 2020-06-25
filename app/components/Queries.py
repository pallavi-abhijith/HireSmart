from components.PostgresReader.Reader import *
# sql = Reader()

class Queries():
    def run_custom_query(self,query):
        sql = Reader()
        return sql.run_query(query)

    def user(self, user_name):
        sql = Reader()
        return sql.run_query("SELECT id, name, language, city \
                FROM user1 \
                WHERE name = '"+user_name+"'"
                )

    def city_language(self, language, city):
        sql = Reader()
        return sql.run_query("SELECT * \
                FROM user1 \
                WHERE language = '"+language+"' and city = '"+city+"' ")
