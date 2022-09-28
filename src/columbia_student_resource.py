import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("root")
        pw = os.environ.get("Kurt2cac.")
        h = os.environ.get("localhost")

        conn = pymysql.connect(
            host="e61561.cnpl1kg3ggad.us-east-1.rds.amazonaws.com",
            port=3306,
            user="admin",
            password="Kurt2cac.",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

