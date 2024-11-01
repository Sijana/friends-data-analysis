import os
import re
import pandas as pd

# Define the path to the directory with the text files
directory_path = "friends_episodes/"

# Initialize a list to hold scene count data with season and episode info
scene_data = []

# Iterate over each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        # Extract season and episode numbers from filename
        match = re.match(r"S(\d{2})E(\d{2})", filename)
        if match:
            season_num = int(match.group(1))
            episode_num = int(match.group(2))
        
        with open(os.path.join(directory_path, filename), 'r') as file:
            content = file.read()
            
            # Split by scenes using regex pattern
            scenes = re.split(r'\[Scene:.*?\]', content)
            
            # Check each scene for character mentions
            for scene in scenes:
                # Set of characters found in the current scene
                characters_in_scene = set()
                
                # Find all instances of "Name:" in the scene
                for match in re.findall(r'(\b\w+\b):', scene):
                    characters_in_scene.add(match.strip())
                
                # Add scene data for each unique character found in the scene
                for character in characters_in_scene:
                    scene_data.append({
                        "Season": season_num,
                        "Episode": episode_num,
                        "Character": character,
                    })

# Convert the scene data to a DataFrame and calculate scene counts
scene_df = pd.DataFrame(scene_data)
scene_counts_df = scene_df.groupby(["Season", "Episode", "Character"]).size().reset_index(name="Scene Count")

# Save the DataFrame to a CSV file
output_path = "output/character_scene_counts_by_episode.csv"
scene_counts_df.to_csv(output_path, index=False)