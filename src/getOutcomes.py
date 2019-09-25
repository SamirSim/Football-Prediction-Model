# Loading all functions
def get_match_label(match):
    ''' Derives a label for a given match. '''

    #Define variables
    home_goals = match['home_team_goal']
    away_goals = match['away_team_goal']

    label = pd.DataFrame()
    label.loc[0,'match_api_id'] = match['match_api_id']

    #Identify match label
    if home_goals > away_goals:
        label.loc[0,'label'] = "1"
    if home_goals == away_goals:
        label.loc[0,'label'] = "0"
    if home_goals < away_goals:
        label.loc[0,'label'] = "-1"

    #Return label
    return label.loc[0]


labels = matches.apply(get_match_label, axis = 1)

del matches['home_team_goal']
del matches['away_team_goal']
matches['final_score'] = labels['label']
