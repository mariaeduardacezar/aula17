import pandas as pd

df = pd.read_csv(r"C:\Users\maria.cezar\Documents\funcionarios.csv")

#print(df)

df.groupby('departamento')['salario'].mean()
df.groupby('departamento').agg(media_salario= ("salario", "mean"))

#print(df.groupby('departamento')['salario'].mean())

#agrupar por departamento e situação do funcionário
resultado = df.groupby(["departamento", "ativo"]).size()
print(resultado.round(2))

#agrupar por departament e agregação de varias colunas
resultado = df.groupby("departamento").agg()