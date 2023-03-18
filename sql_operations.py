import pandas as pd
import sqlite3

create_table = """
CREATE TABLE student_score
(Id INTEGER, Name VARCHAR(20), Math REAL,
Science REAL
):"""
executeSQL = sqlite3.connect(':memory:')
executeSQL.execute(create_table)
executeSQL.commit()
SQL_query = executeSQL.execute('select * from student_score')
resultset = SQL_query.fetchall()
resultset
