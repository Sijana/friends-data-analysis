import pandas as pd

df_ratings = pd.read_csv("friends_episodes_data.csv")
df_ratings["Episode_Title"] = df_ratings["Episode_Title"].str.lower()
df_episodes = pd.read_csv("friends_episodes_numbers.csv")
df_episodes["title"] = df_episodes["title"].str.lower()

# print(df_ratings.head())
# print(df_episodes.head())

df = pd.merge(df_ratings, df_episodes, how="left", left_on="Episode_Title", right_on="title")

df.drop_duplicates()

print(df.dtypes)

df.to_csv("friends_episode_ratings.csv", index=False)