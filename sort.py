import pandas as pd

df = pd.read_csv(r"C:\Users\maria.cezar\Documents\funcionarios.csv")

df = df.sort_values('salario') #organiza o dataframe pelos valores da coluna salario de forma crescente

df = df.sort_values('salario', ascending = False ) #organiza o dataframe pelos valores da coluna salario de

df = df.sort_values(["lucro", "salario"])

print(df)