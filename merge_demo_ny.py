import pandas as pd


df1 = pd.read_csv('demo_ny.csv',low_memory=False)
df2 = pd.read_csv('edu_attain_ny.csv',low_memory=False)
df3 = pd.read_csv('employ_ny.csv',low_memory=False)
df4 = pd.read_csv('mean_income_ny.csv',low_memory=False)
df5 = pd.read_csv('race_ny.csv',low_memory=False)


print("df1 colname:", df1.columns.tolist())
print("df2 colname:", df2.columns.tolist())
print("df3 colname:", df3.columns.tolist())
print("df4 colname:", df4.columns.tolist())
print("df5 colname:", df5.columns.tolist())


merged_df = df1.merge(df2, on='GEO_ID', suffixes=('_demo', '_edu'))\
               .merge(df3, on='GEO_ID', suffixes=('', '_emp'))\
               .merge(df4, on='GEO_ID', suffixes=('', '_inc'))\
               .merge(df5, on='GEO_ID', suffixes=('', '_pov'))


merged_df.to_csv('merged_result_ny.csv', index=False)


print("\nshape:", merged_df.shape)
print("\ncolumn:", merged_df.columns.tolist())