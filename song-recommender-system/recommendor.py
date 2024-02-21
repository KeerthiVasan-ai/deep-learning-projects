import numpy as np
import pandas as pd

print("Hii")

def get_recommendot(num_items,model,user_id)->list():
  user_ids = np.full(num_items,user_id)
  item_ids = np.arange(num_items)
  ratings = model.predict([user_ids,item_ids])
  top_ten = np.argpartition(ratings.flatten(), 10)[:10]
  return top_ten

def get_songs(choice)->list():
    songs=[]
    song_df = pd.read_excel("/content/song_list.xlsx")
    for result in choice:
        songs.append(song_df.iloc[result].values[0])
    return songs
