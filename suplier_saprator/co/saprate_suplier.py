import pandas as pd
import os

f_names = os.listdir(r"D:\suplier_saprator\co\file")
print(f_names[0])
p_df = pd.read_excel(f'D:/suplier_saprator/co/file/{f_names[0]}')
s_df = pd.read_csv(r'D:\suplier_saprator\co/suport/supplier.csv')
suplier_payment = pd.DataFrame()
sdf = pd.DataFrame()

for i in range(0, len(s_df)):
    _df = s_df.iloc[i]['id']
    print(_df)
    p_df.drop(p_df[p_df['Customer No'] == _df])

p_df.to_excel(f'without supplier {f_names[0]} ', index=False)
