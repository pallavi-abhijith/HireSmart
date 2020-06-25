from components.PostgresReader.Reader import *
# sql = Reader()

class Queries():
    def run_custom_query(self,query):
        sql = Reader()
        return sql.run_query(query)

    def user(self, user_name):
        sql = Reader()
        return sql.run_query("select p.pro_id, p.pro_name, p.recent_update, pl.bytes, count(c.pro_id) \
            from projects1 p \
                join project_language pl on pl.pro_id = p.pro_id \
                    join commits c on c.pro_id = p.pro_id \
                        where p.user_id = ( \
                            select user_id from user1 where name = '"+user_name+"' ) \
                        group by p.pro_id, p.pro_name, p.recent_update, pl.bytes")

    def city_language(self, language, city):
        sql = Reader()
        return sql.run_query("SELECT u.name \
                FROM user1 u\
                join projects1 p on p.user_id = u.user_id \
                    WHERE p.language = '"+language+"' and location = '"+city+"' ")

