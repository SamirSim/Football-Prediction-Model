
#Cleaning the matches table

#Drop the rows that have no player information
toDrop = []
for i in range(1, 11):
    toDrop.append('home_player_'+str(i))
    toDrop.append('away_player_'+str(i))
    toDrop.append('home_player_X'+str(i))
    toDrop.append('home_player_Y'+str(i))
    toDrop.append('away_player_X'+str(i))
    toDrop.append('away_player_Y'+str(i))

tempMatch = match.dropna(axis=0, how='any', thresh=None, subset=toDrop, inplace=False)


betWins, betDraws, betLoss = [], [], []

betSites = ('B365', 'BW', 'IW', 'LB', 'PS', 'WH', 'SJ', 'VC', 'GB', 'BS')

for i in betSites:
    betWins.append(i+'H')     
    betDraws.append(i+'D')
    betLoss.append(i+'A')

#Drop the rows that don't have any bet score
toDrop = []
for i in betWins:
    toDrop.append(i)
for i in betDraws:
    toDrop.append(i)
for i in betLoss:
    toDrop.append(i)
    
tempMatch = tempMatch.dropna(axis=0, how='all', thresh=None, subset=toDrop, inplace=False)

toDrop = ['goal', 'shoton', 'shotoff', 'foulcommit', 'card', 'cross', 'corner', 'possession']
tempMatch = tempMatch.drop(columns=toDrop)

#Fill the Null values of bet scores
newMatches = pd.DataFrame()
for row in tempMatch.iterrows():
    
    #Get the columns into Pandas dataframes
    valuesBetWins = row[1][betWins]
    valuesBetDraws = row[1][betDraws]
    valuesBetLoss = row[1][betLoss]
    
    #Calculate the average for each one
    avgBetWins = valuesBetWins.mean(skipna=True)
    avgBetDraws = valuesBetDraws.mean(skipna=True)
    avgBetLoss = valuesBetLoss.mean(skipna=True)

    #Replace the Null values
    for i in betWins:
        if str(row[1][i]) == 'nan':
            row[1][i] = avgBetWins
            
    for i in betDraws:
        if str(row[1][i]) == 'nan':
            row[1][i] = avgBetDraws
        
    for i in betLoss:
        if str(row[1][i]) == 'nan':
            row[1][i] = avgBetLoss

    newMatches = newMatches.append(row[1])
    
#Cleaning the Player  Attributes table
#Drop some columns from the player attributes table 
toDrop = ['overall_rating', 'attacking_work_rate', 'volleys']
newPlayerAttributes = playerAttributes.dropna(axis=0, how='any', thresh=None, subset=toDrop, inplace=False)

#Cleaning the Team attributes table
#Drop the buildUpDribbling column from the team attributes table 
toDrop = ['buildUpPlayDribbling']
newTeamAttributes = teamAttributes.drop(columns=toDrop)
