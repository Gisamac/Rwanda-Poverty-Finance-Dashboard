import pandas as pd

# 1. Soma CSV ifite ikibazo
df = pd.read_csv('data/Rwanda_Poverty_Finance_Data.csv')

# 2. Bara impuzandengo (Average/Mean) y'Uturere 16 dusigaye tudafite 0
impuzandengo_digital = df[df['Digital_App_Pct'] > 0]['Digital_App_Pct'].mean()
impuzandengo_bank = df[df['Bank_Loan_Pct'] > 0]['Bank_Loan_Pct'].mean()
impuzandengo_saving = df[df['Saving_Group_Pct'] > 0]['Saving_Group_Pct'].mean()

# 3. Simbuza 0 zose iriya mpuzandengo (Mean Imputation)
df['Digital_App_Pct'] = df['Digital_App_Pct'].replace(0, impuzandengo_digital)
df['Bank_Loan_Pct'] = df['Bank_Loan_Pct'].replace(0, impuzandengo_bank)
df['Saving_Group_Pct'] = df['Saving_Group_Pct'].replace(0, impuzandengo_saving)

# 4. Bika CSV nshya isukuye kandi yuzuye
df.to_csv('data/Rwanda_Poverty_Finance_Data.csv', index=False)

print("Byakunze! Uturere 14 twari 0 twahawe impuzandengo y'igihugu.")
print("Ubu ushobora kongera gufungura Dashboard yawe!")