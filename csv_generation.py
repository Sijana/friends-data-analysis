import pandas as pd
import numpy as np
import os
import re


# Read through all episodes and collect info on:
# 1. Season 2. Episode 3. Character speaking 4. Their lines

dir_url = "friends_episodes/"

pattern = re.compile(r'^([A-Za-z]+):\s*(.*)$')

data = []

for filename in os.listdir(dir_url):
    if filename.endswith(".txt"):
        
        season = int(filename[1:3])
        episode = int(filename[4:6])
        
        with open(os.path.join(dir_url, filename), "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                
                match = pattern.match(line)
                if match:
                    character = match.group(1).strip()
                    dialogue = match.group(2).strip()
                    
                    data.append([season, episode, character, dialogue])

df = pd.DataFrame(data, columns=["Season", "Episode", "Character", "Lines"])

print(df.head())

df.to_csv('friends_dialogues.csv', index=False)
