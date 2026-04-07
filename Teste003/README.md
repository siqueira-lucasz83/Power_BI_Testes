# 🚗 Dashboard de Vendas de Carros - Projeto Power BI - Teste 003

## 📌 Visão Geral

Este projeto tem como objetivo analisar dados de vendas de veículos através de um pipeline completo de dados, integrando banco de dados, tratamento em Python e visualização no Power BI.

Diferente dos projetos anteriores, aqui foi desenvolvido um fluxo mais próximo do ambiente profissional, envolvendo extração, transformação e carga de dados (ETL).

---

## 🛠 Ferramentas Utilizadas

* Power BI
* Power Query
* DAX
* Python (pandas, mysql-connector)
* MySQL

---

## 🔄 Pipeline de Dados (ETL)

O projeto segue as etapas abaixo:

1. **Extração (Extract)**

   * Dados armazenados em banco MySQL

2. **Transformação (Transform)**

   * Limpeza e tratamento com Python (pandas)
   * Criação de colunas como mês e ano
   * Padronização de dados

3. **Carga (Load)**

   * Exportação para CSV
   * Importação no Power BI

---

## 🗄 Base de Dados

A base contém informações de vendas de veículos, incluindo:

* Marca
* Modelo
* Ano do veículo
* Data da venda
* Preço
* Vendedor
* Região

---

## 🧱 Modelagem de Dados

Foi aplicada modelagem em formato **Star Schema (modelo dimensional)**:

* **fVendas** → tabela fato
* **dCalendario** → dimensão de tempo

Relacionamento:

* fVendas[data] → dCalendario[Date]

---

## 📈 Indicadores Criados (KPIs)

* Faturamento Total
* Quantidade de Vendas
* Ticket Médio
* Faturamento por Marca
* Faturamento por Região
* Evolução temporal das vendas

---

## 🧠 Foco do Projeto

Este projeto foi desenvolvido com ênfase em:

* Integração entre banco de dados e BI
* Processo ETL com Python
* Modelagem de dados (boas práticas)
* Criação de medidas com DAX
* Organização de projeto para portfólio

---

## 📊 Visualizações

O dashboard inclui:

* Cards com KPIs principais
* Gráfico de colunas (faturamento por período)
* Gráfico de barras (faturamento por marca)
* Gráfico de pizza (vendas por região)
* Segmentações (filtros) por:

  * Ano
  * Marca

---

## 📁 Estrutura do Projeto

```plaintext
Teste003/
│
├── README.md
├── Python/
├── Dados/
│   ├── CSV/
│   ├── Excel/
│   └── MySQL/
├── Capturas_de_Tela/
```

---

## 🎯 Objetivo do Projeto

* Simular um pipeline de dados real
* Consolidar conhecimentos em Python, SQL e Power BI
* Aplicar boas práticas de modelagem
* Desenvolver um projeto completo para portfólio

---

## 🚀 Considerações

Este projeto representa uma evolução significativa, saindo de análises baseadas apenas em arquivos para um fluxo completo de dados, mais próximo do cenário encontrado no mercado.

---
