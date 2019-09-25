conn=sqlite3.connect(r'C:\Users\ThisPC\Desktop\ML\database.sqlite')

Match_Train=pd.read_sql("SELECT Match.id as MatchId,season,stage,home_team_goal,away_team_goal,home_team_api_id,away_team_api_id,"
                        "home_player_X1,"
                        "home_player_X2,"
                        "home_player_X3,"
                        "home_player_X4,"
                        "home_player_X5,"
                        "home_player_X6,"
                        "home_player_X7,"
                        "home_player_X8,"
                        "home_player_X9,"
                        "home_player_X10,"
                        "home_player_X11,"
                        "home_player_Y1,"
                        "home_player_Y2,"
                        "home_player_Y3,"
                        "home_player_Y4,"
                        "home_player_Y5,"
                        "home_player_Y6,"
                        "home_player_Y7,"
                        "home_player_Y8,"
                        "home_player_Y9,"
                        "home_player_Y10,"
                        "home_player_Y11,"
                        "home_player_1,"
                        "home_player_2,"
                        "home_player_3,"
                        "home_player_4,"
                        "home_player_5,"
                        "home_player_6,"
                        "home_player_7,"
                        "home_player_8,"
                        "home_player_9,"
                        "home_player_10,"
                        "home_player_11,"
                        "away_player_X1,"
                        "away_player_X2,"
                        "away_player_X3,"
                        "away_player_X4,"
                        "away_player_X5,"
                        "away_player_X6,"
                        "away_player_X7,"
                        "away_player_X8,"
                        "away_player_X9,"
                        "away_player_X10,"
                        "away_player_X11,"
                        "away_player_Y1,"
                        "away_player_Y2,"
                        "away_player_Y3,"
                        "away_player_Y4,"
                        "away_player_Y5,"
                        "away_player_Y6,"
                        "away_player_Y7,"
                        "away_player_Y8,"
                        "away_player_Y9,"
                        "away_player_Y10,"
                        "away_player_Y11,"
                        "away_player_1,"
                        "away_player_2,"
                        "away_player_3,"
                        "away_player_4,"
                        "away_player_5,"
                        "away_player_6,"
                        "away_player_7,"
                        "away_player_8,"
                        "away_player_9,"
                        "away_player_10,"
                        "away_player_11,"
                      "B365H,"
                       "BWH,"
                       "IWH,"
                       "LBH,"
                       "PSH,"
                       "WHH,"
                       "SJH,"
                       "VCH,"
                       "GBH,"
                       "BSH,"
                                              "B365D,"
                       "BWD,"
                       "IWD,"
                       "LBD,"
                       "PSD,"
                       "WHD,"
                       "SJD,"
                       "VCD,"
                       "GBD,"
                       "BSD,"
                        "B365A,"
                       "BWA,"
                       "IWA,"
                       "LBA,"
                       "PSA,"
                       "WHA,"
                       "SJA,"
                       "VCA,"
                       "GBA,"
                       "BSA"
                                              " FROM Match JOIN League ON Match.league_id=League.id JOIN Country ON League.country_id=Country.id WHERE Country.name='Italy' AND season!='2015/2016';",conn)
Match_Test=pd.read_sql("SELECT Match.id as MatchId,season,stage,home_team_goal,away_team_goal,home_team_api_id,away_team_api_id,"
                        "home_player_X1,"
                        "home_player_X2,"
                        "home_player_X3,"
                        "home_player_X4,"
                        "home_player_X5,"
                        "home_player_X6,"
                        "home_player_X7,"
                        "home_player_X8,"
                        "home_player_X9,"
                        "home_player_X10,"
                        "home_player_X11,"
                        "home_player_Y1,"
                        "home_player_Y2,"
                        "home_player_Y3,"
                        "home_player_Y4,"
                        "home_player_Y5,"
                        "home_player_Y6,"
                        "home_player_Y7,"
                        "home_player_Y8,"
                        "home_player_Y9,"
                        "home_player_Y10,"
                        "home_player_Y11,"
                        "home_player_1,"
                        "home_player_2,"
                        "home_player_3,"
                        "home_player_4,"
                        "home_player_5,"
                        "home_player_6,"
                        "home_player_7,"
                        "home_player_8,"
                        "home_player_9,"
                        "home_player_10,"
                        "home_player_11,"
                        "away_player_X1,"
                        "away_player_X2,"
                        "away_player_X3,"
                        "away_player_X4,"
                        "away_player_X5,"
                        "away_player_X6,"
                        "away_player_X7,"
                        "away_player_X8,"
                        "away_player_X9,"
                        "away_player_X10,"
                        "away_player_X11,"
                        "away_player_Y1,"
                        "away_player_Y2,"
                        "away_player_Y3,"
                        "away_player_Y4,"
                        "away_player_Y5,"
                        "away_player_Y6,"
                        "away_player_Y7,"
                        "away_player_Y8,"
                        "away_player_Y9,"
                        "away_player_Y10,"
                        "away_player_Y11,"
                        "away_player_1,"
                        "away_player_2,"
                        "away_player_3,"
                        "away_player_4,"
                        "away_player_5,"
                        "away_player_6,"
                        "away_player_7,"
                        "away_player_8,"
                        "away_player_9,"
                        "away_player_10,"
                        "away_player_11,"
                       "B365H,"
                       "BWH,"
                       "IWH,"
                       "LBH,"
                       "PSH,"
                       "WHH,"
                       "SJH,"
                       "VCH,"
                       "GBH,"
                       "BSH,"
                                              "B365D,"
                       "BWD,"
                       "IWD,"
                       "LBD,"
                       "PSD,"
                       "WHD,"
                       "SJD,"
                       "VCD,"
                       "GBD,"
                       "BSD,"
                        "B365A,"
                       "BWA,"
                       "IWA,"
                       "LBA,"
                       "PSA,"
                       "WHA,"
                       "SJA,"
                       "VCA,"
                       "GBA,"
                       "BSA"
                      
                        " FROM Match JOIN League ON Match.league_id=League.id JOIN Country ON League.country_id=Country.id WHERE Country.name='Italy' AND season='2015/2016';",conn)


Team_Attributes=pd.read_sql("SELECT id as Team_Attributes_id,team_fifa_api_id as Team_Attributes_team_fifa_api_id,team_api_id as Team_Attributes_team_api_id,date as Team_Attributes_date,buildUpPlaySpeed,buildUpPlaySpeedClass,buildUpPlayDribbling,buildUpPlayDribblingClass,buildUpPlayPassing,buildUpPlayPassingClass,buildUpPlayPositioningClass,chanceCreationPassing,chanceCreationPassingClass,chanceCreationCrossing,chanceCreationCrossingClass,chanceCreationShooting,chanceCreationShootingClass,chanceCreationPositioningClass,defencePressure,defencePressureClass,defenceAggression,defenceAggressionClass,defenceTeamWidth,defenceTeamWidthClass,defenceDefenderLineClass,season as Team_Attributes_season FROM Team_Attributes WHERE Team_Attributes_season is not null",conn)
Team_Attributes=Team_Attributes.drop_duplicates(subset={'Team_Attributes_team_api_id','Team_Attributes_season'})
Home_Match_Train=pd.merge(Match_Train,Team_Attributes,left_on=['home_team_api_id','season'], right_on=['Team_Attributes_team_api_id', 'Team_Attributes_season'])
Home_Match_Train.drop(columns=['Team_Attributes_id','Team_Attributes_team_fifa_api_id','Team_Attributes_team_api_id','Team_Attributes_date','Team_Attributes_season'])
Match_Train_Attributes=pd.merge(Home_Match_Train,Team_Attributes,left_on=['away_team_api_id','season'], right_on=['Team_Attributes_team_api_id', 'Team_Attributes_season'])

Match_Train_Attributes.drop(columns=['Team_Attributes_id_y','Team_Attributes_team_fifa_api_id_y','Team_Attributes_team_api_id_y','Team_Attributes_date_y','Team_Attributes_season_y'])

Match_Player_Attributes=pd.read_sql("SELECT * FROM Match_Player_Attributes",conn)

Match_Train=pd.merge(Match_Train_Attributes,Match_Player_Attributes,left_on='MatchId',right_on='match_id')
Match_Train.drop(columns='match_id')

print(list(Match_Train.columns))

Team_Attributes=pd.read_sql("SELECT id as Team_Attributes_id,team_fifa_api_id as Team_Attributes_team_fifa_api_id,team_api_id as Team_Attributes_team_api_id,date as Team_Attributes_date,buildUpPlaySpeed,buildUpPlaySpeedClass,buildUpPlayDribbling,buildUpPlayDribblingClass,buildUpPlayPassing,buildUpPlayPassingClass,buildUpPlayPositioningClass,chanceCreationPassing,chanceCreationPassingClass,chanceCreationCrossing,chanceCreationCrossingClass,chanceCreationShooting,chanceCreationShootingClass,chanceCreationPositioningClass,defencePressure,defencePressureClass,defenceAggression,defenceAggressionClass,defenceTeamWidth,defenceTeamWidthClass,defenceDefenderLineClass,season as Team_Attributes_season FROM Team_Attributes WHERE Team_Attributes_season is not null",conn)
Team_Attributes=Team_Attributes.drop_duplicates(subset={'Team_Attributes_team_api_id','Team_Attributes_season'})
Home_Match_Test=pd.merge(Match_Test,Team_Attributes,left_on=['home_team_api_id','season'], right_on=['Team_Attributes_team_api_id', 'Team_Attributes_season'])
Home_Match_Test.drop(columns=['Team_Attributes_id','Team_Attributes_team_fifa_api_id','Team_Attributes_team_api_id','Team_Attributes_date','Team_Attributes_season'])
Match_Test_Attributes=pd.merge(Home_Match_Test,Team_Attributes,left_on=['away_team_api_id','season'], right_on=['Team_Attributes_team_api_id', 'Team_Attributes_season'])

Match_Test_Attributes.drop(columns=['Team_Attributes_id_y','Team_Attributes_team_fifa_api_id_y','Team_Attributes_team_api_id_y','Team_Attributes_date_y','Team_Attributes_season_y'])

Match_Player_Attributes=pd.read_sql("SELECT * FROM Match_Player_Attributes",conn)

Match_Test=pd.merge(Match_Test_Attributes,Match_Player_Attributes,left_on='MatchId',right_on='match_id')
Match_Test.drop(columns='match_id')
