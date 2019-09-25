import sqlite3
import pandas as pd

conn = sqlite3.connect('Data/database.sqlite')
matchTrain = pd.read_sql("SELECT * FROM Match WHERE season!='2015/2016';", conn)
matchTest = pd.read_sql("SELECT * FROM Match WHERE season='2015/2016';", conn)
country = pd.read_sql("SELECT * FROM Country;", conn)
league = pd.read_sql("SELECT * FROM League;", conn)

team = pd.read_sql("SELECT * FROM Team;", conn)
teamAttributes = pd.read_sql("SELECT * FROM Team_Attributes;", conn)
player = pd.read_sql("SELECT * FROM Player;", conn)
playerAttributes = pd.read_sql("SELECT * FROM Player_Attributes;", conn)

