import sqlite3
import pandas as pd

conn=sqlite3.connect('Data/database.sqlite')
Match=pd.read_sql("SELECT * FROM Match;",conn)
Country=pd.read_sql("SELECT * FROM Country;",conn)
League=pd.read_sql("SELECT * FROM League;",conn)

Team=pd.read_sql("SELECT * FROM Team;",conn)
Team_Attributes=pd.read_sql("SELECT * FROM Team_Attributes;",conn)
Player=pd.read_sql("SELECT * FROM Player;",conn)
Player_Attributes=pd.read_sql("SELECT * FROM Player_Attributes;",conn)

