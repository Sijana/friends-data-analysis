import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns

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