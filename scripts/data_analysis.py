import pandas as pd

df = pd.read_csv("output/friends_dialogues.csv")

# Cleaning Data:

df["Character"] = df["Character"].str.capitalize()

typo_corrections = {
    'Chan': 'Chandler',
    'Gunter': 'Gunther',
    'Mnca': 'Monica',
    'Rach': 'Rachel',
    'Phoe': 'Phoebe',
    'Racel': 'Rachel',
    'Rache': 'Rachel'
}

df['Character'] = df['Character'].replace(typo_corrections)