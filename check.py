import pandas as pd

df = pd.read_csv('data/Rwanda_Poverty_Finance_Data.csv')

# Tugiye kureba niba hari 0 ziri muri CSV yacu ku nkingi ya 'Digital_App_Pct'
uturere_twabuze = df[df['Digital_App_Pct'] == 0]['District'].tolist()

print("Uturere dufite 0 muri CSV ni utu:")
print(uturere_twabuze)