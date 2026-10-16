import pandas as pd 

dados = {
    'categoria': ['Eletrônicos', 'Eletrônicos', 'Eletrônicos', 'Eletrônicos',
                  'Roupas', 'Roupas', 'Roupas', 'Roupas',
                  'Alimentos', 'Alimentos', 'Alimentos', 'Alimentos'],
    'ano':       [2022, 2022, 2023, 2023,
                  2022, 2022, 2023, 2023,
                  2022, 2022, 2023, 2023],
    'vendas':    [1000, 1500, 2000, 2500,
                  800,  900,  1100, 1300,
                  500,  600,  700,  850]
}

df = pd.DataFrame(dados)

print("DataFrame original")
print(df)
print("\n")

tabela_pivot = df.pivot_table(index='categoria' #define a coluna que sera usada como linha da tabela
                              , columns='ano'#define a coluna que será usada como coluna
                              , values='vendas'#coluna cujos valores serão agregados
                              , aggfunc='sum'#função agregação
                              )

print("vendas somadas por categoria e ano")
print(tabela_pivot)
print("\n")