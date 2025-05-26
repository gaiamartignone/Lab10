from database.DB_connect import DBConnect
from model.collegamento import Collegamento


class DAO:
    @staticmethod
    def getallarchi():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """SELECT 
                  s1.StateNme   AS s1,
                  s2.StateNme AS s2,
                  c.year AS anno
                FROM contiguity AS c
                JOIN country   AS s1  ON c.state1ab = s1.StateAbb
                JOIN country   AS s2  ON c.state2ab = s2.StateAbb
                 WHERE c.conttype = 1; """

        cursor.execute(query, )
        results =[]
        for row in cursor:
            results.append(Collegamento(row['s1'], row['s2'],row['anno']))
        cursor.close()
        conn.close()
        return results