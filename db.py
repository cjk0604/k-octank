import pymysql
import os


class DB:
    """ Database layer
    """

    def query(self, statement, *positional_parameters):
        # rds settings
        #db_name = 'koctank'
        # rds_host = os.environ['DATABASE_HOST']
        # db_user = os.environ['DATABASE_USER']
        # password = os.environ['DATABASE_PASSWORD']
        # db_name = os.environ['DATABASE_DB_NAME']

        rds_host = "koctankdbcluster.cmctwgljftes.us-east-1.rds.amazonaws.com"
        db_user = "admin"
        password = "welcome123"
        db_name = "koctank"
        port = 3306

        server_address = (rds_host, port)
        conn = pymysql.connect(rds_host, user=db_user, passwd=password, db=db_name, connect_timeout=5,
                               charset='utf8mb4')

        print("trying to connect")
        result = None
        try:
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(statement, positional_parameters)
                result = cursor.fetchall()
                print("Connection successs!!!!!!!!!")
        finally:
            conn.commit()
            conn.close()
        return result
