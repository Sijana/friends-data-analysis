import pandas as pd

df_ratings = pd.read_csv("friends_episodes_data.csv", encoding='latin-1')
df_ratings["Episode_Title"] = df_ratings["Episode_Title"].str.lower()
df_episodes = pd.read_csv("friends_episodes_numbers.csv")
df_episodes["title"] = df_episodes["title"].str.lower()

# print(df_ratings.head())
# print(df_episodes.head())

df_episodes = df_episodes[["title", "episode_num_in_season", "episode_num_overall", "written_by", "original_air_date", "us_viewers"]]

df = pd.merge(df_ratings, df_episodes, how="left", left_on="Episode_Title", right_on="title")
df.drop(columns=["title"], inplace=True)
df.to_csv("friends_episode_ratings.csv", index=False)