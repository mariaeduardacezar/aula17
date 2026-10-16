import pandas as pd


vendas = pd.DataFrame({
    'id_cliente': [1, 2, 3, 4],
    'produto':    ['Notebook', 'Mouse', 'Teclado', 'Monitor']
})

clientes = pd.DataFrame({
    'id_cliente': [1, 2, 3, 5],
    'nome':       ['Ana', 'Bruno', 'Carlos', 'Eva'],
    'cidade':     ['SP', 'RJ', 'MG', 'BA']
})

resultado_merge = pd.merge(vendas, clientes, on='id_cliente')

print(resultado_merge)