import pandas as pd 

df = pd.read_csv("ar_words.csv")


triggers = df["words"].to_list()
reactions = df["reactions"].to_list()
df.index = triggers

for i in triggers:
        print(df.loc[i,"reactions"])