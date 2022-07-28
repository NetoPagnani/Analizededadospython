# Desafio: Descobrir por que 26% dos clientes estão cancelando (churn), e verificar se 26% esta correto


# Passo 1: Importar a base de dados.
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados.
# display(tabela)
# axis = 0 -> eixo da linha
# axis = 1 -> eixo da coluna
# Entender as informações que voce tem disponivel.
# excluir coluna inutil
tabela = tabela.drop("Unnamed: 0", axis=1)
tabela = tabela.drop("IDCliente", axis=1)
print(tabela)

# Descobrir as cagadas da base de dados.
# Informação que não te ajuda, te atrapalha.
# Passo 3: Tratamento de dados (Resolver as cagadas).
print(tabela.info())
# Informações são do tipo correto.
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
# Informações vazias.
# coluna vazia -> excluir
tabela = tabela.dropna(how="all", axis=1)
# linha que tem informação vazia -> excluir
tabela = tabela.dropna(how="any", axis=0)
# Passo 4: Analise inicial dos dados.
# como estão os cancelamento? 26%?
print(tabela["Churn"].value_counts)
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))
# Passo 5: Descobrir os motivos do cancelamento.
import plotly.express as px

# todo grafico é feito com duas etapas:
# criar o grafico
# exibir o grafico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()

# Conclusões:

# Clientes que estão a pouco tempo estão cancelando muito.
# Pode estar fazendo uma promoção que ta dando 1º de graça.
# O Inicio do serviço pro cliente ta sendo muito confuso.
# A 1ª experiencia do cliente está sendo ruim.
# Podemos criar incentivos nos primeiros meses, primeiro ano mais barato.

# Boleto eletronico tem muito mais cancelamento do que as outra formas de pagamento.
# Oferecer desconto nas outras formas de pagamento.

# Clientes com contrato mensal tem muito mais chance de cancelar.
# Oferecer plano anual com desconto.

# Quanto mais serviços o cliente tem, menor a chance de ele cancelar.
# Oferecer serviços extra de graça.

# Clientes com mais linhas com familia maior, tem menos chance de cancelar.
# 2ª linha de graça ou desconto.


