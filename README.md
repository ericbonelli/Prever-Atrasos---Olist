# Prever Atrasos - Olist

# **Etapa 1 do CRISP-DM: Entendimento do Negócio**

A primeira etapa do **CRISP-DM (Cross Industry Standard Process for Data Mining)** é o **Entendimento do Negócio**, que envolve a definição do problema, os objetivos do projeto e as restrições do contexto empresarial. O objetivo dessa fase é garantir que o time de ciência de dados compreenda o domínio do problema e alinhe o modelo preditivo às necessidades e estratégias da empresa.

---

## **1.1 Definição do Objetivo do Negócio**
O objetivo central deste projeto é **reduzir atrasos de entrega e melhorar as avaliações dos clientes** na Olist. Com isso, buscamos:

- **Aumentar a retenção de clientes**: melhorar a experiência para incentivar recompras.
- **Reduzir impactos negativos da logística**: minimizar atrasos e otimizar processos de entrega.
- **Aprimorar a reputação da Olist**: garantir que os vendedores e transportadoras proporcionem um serviço de qualidade.

---

## **1.2 Situação Atual do Negócio**
A Olist opera como um marketplace intermediário, conectando pequenos negócios a grandes canais de venda, mas enfrenta desafios como:

- **Dependência de múltiplos stakeholders**: vendedores, transportadoras e clientes.
- **Complexidade logística**: entregas cobrindo todo o Brasil, incluindo regiões remotas.
- **Impacto direto da experiência do cliente**: avaliações negativas afetam a reputação e reduzem a retenção.

Atualmente, o monitoramento de atrasos e a gestão de satisfação do cliente são feitos com base em **dados operacionais e feedbacks diretos**. Nosso objetivo é aprimorar esse processo com **análises preditivas e otimização logística**.

---

## **1.3 Objetivo do Projeto de Ciência de Dados**
Nosso objetivo é construir um modelo que possa prever o **risco de atraso na entrega e a insatisfação do cliente** com base em:

- **Dados do pedido** (data da compra, tipo de envio, prazo estimado).
- **Informações do cliente** (localização, histórico de compras, comportamento de avaliação).
- **Dados logísticos** (transportadora, tempo médio de entrega, ocorrências de atraso anteriores).
- **Feedbacks dos clientes** (avaliações, comentários, reclamações anteriores).

---

## **1.4 Avaliação dos Requisitos**
Para o sucesso do projeto, precisamos considerar:

- **Fontes de Dados**: Quais bases estão disponíveis? Os dados são confiáveis e completos?
- **Indicadores de Sucesso**: Qual será a métrica principal do modelo? Precisão na previsão de atrasos, melhoria na média das avaliações?
- **Restrições Técnicas**: O modelo precisa ser interpretável para uso operacional?
- **Aspectos Legais e Éticos**: O modelo deve considerar a **LGPD (Lei Geral de Proteção de Dados)** e evitar vieses discriminatórios.

---

## **1.5 Planejamento do Projeto**
Com o entendimento do negócio definido, o próximo passo é estruturar um **cronograma** para as etapas seguintes do CRISP-DM:

1. **Entendimento dos Dados** (coleta, análise exploratória, identificação de padrões e outliers).
2. **Preparação dos Dados** (limpeza, transformação, engenharia de features).
3. **Modelagem** (seleção e treinamento de algoritmos preditivos).
4. **Avaliação do Modelo** (validação, métricas de desempenho e ajustes).
5. **Implantação** (integração do modelo na operação da Olist para otimização contínua).

---

Essa fase garante que todas as partes envolvidas estejam **alinhadas sobre os objetivos do projeto**, as expectativas e os desafios a serem enfrentados. **Com um bom entendimento do negócio, evitamos desperdício de tempo e garantimos que o modelo atenda às necessidades reais da Olist.**


# **Etapa 2 do CRISP-DM: Estrutura dos Dados**

Nesta fase, exploramos a estrutura e a qualidade do dataset consolidado da Olist, com foco em identificar padrões iniciais, valores ausentes e possíveis problemas nos dados que impactam a experiência do cliente e a logística de entrega.

---

## 📌 1. Estrutura do Dataset

- **Fonte:** consolidação de 4 tabelas: pedidos, clientes, itens e avaliações.
- **Total de registros:** aproximadamente 99 mil linhas.
- **Total de colunas:** 25 variáveis.
- **Principais variáveis:**
  - `review_score`: nota do cliente (1 a 5)
  - `price`: valor do item comprado
  - `freight_value`: valor do frete
  - `order_delivered_customer_date`, `order_estimated_delivery_date`: datas para cálculo de atraso
  - `customer_state`, `seller_id`: localização do cliente e vendedor

---

## 📌 2. Valores Ausentes e Duplicados

- **Campos com nulos relevantes:**
  - `review_comment_title`: ~58% ausente
  - `review_comment_message`: ~45% ausente
  - `order_delivered_customer_date`: nulo em pedidos não entregues ou cancelados
- **Campos críticos (`price`, `freight_value`)** têm pouquíssimos nulos.
- **Duplicatas:** nenhuma duplicata de `order_id` encontrada.

---

## 📌 3. Inconsistências e Problemas Identificados

- **Entregas inválidas:** datas de entrega anteriores à data da compra.
- **Preços suspeitos:** registros com `price <= 0`.
- **Fretes extremos:** valores acima do percentil 99 (R$150+).

Esses casos foram apenas diagnosticados nesta etapa e serão tratados na Etapa 3.

---

## 📌 4. Análise Exploratória Visual

### 🎯 Distribuição das Avaliações dos Clientes
- A maior parte das avaliações são 4 ou 5 estrelas.
- Notas 1 e 2 representam ~10% dos pedidos.

### 🚚 Distribuição dos Dias de Atraso na Entrega
- Muitos pedidos entregues adiantados (valores negativos).
- Pico em 0 dias e outro entre 3 e 5 dias de atraso.

### 💸 Preço vs Frete
- Fretes caros aparecem mesmo para produtos de valor baixo.
- Não há relação linear clara entre preço e frete.

### ⏱️ Tempo de Entrega vs Avaliação
- Notas baixas concentram maior tempo médio de entrega.
- Clientes que receberam no prazo ou adiantado tendem a avaliar melhor.

---

## 📌 5. Correlações

- **`delivery_delay` vs `review_score`:** correlação negativa (-0.23)  
- **`freight_value` e `price`:** quase nenhuma correlação (0.02)  
- **Correlação entre `delivery_delay` e `total_delivery_time`:** moderada

---

## ✅ Conclusão da Etapa 2

- A estrutura dos dados está adequada, com poucos nulos críticos.
- As análises sugerem que **atrasos têm impacto direto na avaliação do cliente**.
- Há registros inconsistentes (entrega inválida, frete extremo, preço nulo) que serão tratados na próxima fase.

**➡️ A Etapa 3 (Preparação dos Dados)** focará em criar variáveis derivadas, tratar valores problemáticos e preparar os dados para modelagem preditiva ou segmentações.


# **Etapa 3 do CRISP-DM: Preparação dos Dados**

Após entender a estrutura e qualidade dos dados, a Etapa 3 tem como objetivo transformar, corrigir e enriquecer os dados, preparando-os para análises avançadas e modelagem preditiva.

---

## 📌 1. Tratamento de Valores Ausentes

- As colunas `review_comment_title` e `review_comment_message` foram preenchidas com `"Sem título"` e `"Sem comentário"`.
- As colunas críticas `price` e `freight_value` com valores nulos foram removidas.

---

## 📌 2. Remoção de Inconsistências

- **Entregas inválidas:** registros com `order_delivered_customer_date` anterior à data da compra foram excluídos.
- **Preços suspeitos:** registros com `price <= 0` foram removidos.
- **Fretes extremos:** valores acima do percentil 99 foram excluídos para evitar distorções.

---

## 📌 3. Criação de Variáveis Derivadas

Variáveis criadas para enriquecer o contexto analítico e alimentar modelos de previsão:

| Variável              | Descrição                                                            |
|------------------------|----------------------------------------------------------------------|
| `delivery_delay`       | Diferença entre a data real e a estimada de entrega (em dias)       |
| `total_delivery_time`  | Dias entre a compra e a entrega do pedido                           |
| `entrega_status`       | Classificação: "Adiantado", "No Prazo" ou "Atrasado"                |
| `review_category`      | Classificação da nota: "Ruim" (1-2), "Neutro" (3), "Boa" (4-5)      |

---

## 📌 4. Formatação para Modelagem Preditiva

### 🔹 Conversão de Variáveis Categóricas
- As variáveis `entrega_status`, `review_category` e `customer_state` foram convertidas em **dummies** (One-Hot Encoding).
- A primeira categoria de cada variável foi removida para evitar multicolinearidade.

### 🔹 Normalização das Variáveis Numéricas
- As variáveis `price`, `freight_value`, `delivery_delay` e `total_delivery_time` foram **normalizadas com z-score** (média = 0, desvio padrão = 1).
- Isso garante que todas estejam na mesma escala, o que melhora o desempenho de vários algoritmos de machine learning.

---

## 📌 5. Exportação Final

O dataset preparado e formatado foi salvo como:
- `olist_preparado.csv` — dados tratados e com novas variáveis
- `olist_modelagem.csv` — dados prontos para algoritmos de machine learning

---

## ✅ Conclusão da Etapa 3

Com os dados limpos, enriquecidos e formatados, estamos prontos para a próxima fase do projeto: análise preditiva, segmentações ou qualquer técnica de modelagem baseada em dados.

As variáveis estão no formato ideal para análise estatística e machine learning.

# 📊 **Etapa 4 do CRISP-DM: Modelagem**

Nesta etapa, utilizamos os dados preparados e enriquecidos para treinar um modelo capaz de prever se um pedido será entregue com atraso.

---

## 📌 Objetivo

Prever a variável `entrega_status_Atrasado` (0 = no prazo / 1 = com atraso), com base em variáveis numéricas, logísticas e de comportamento do cliente.

---

## 📌 Algoritmo Utilizado

- **Modelo:** Random Forest Classifier
- **Ajuste importante:** `class_weight='balanced'` e **SMOTE** para lidar com o desequilíbrio de classes

---

## 📌 Feature Engineering Realizada

Foram criadas 3 novas variáveis para enriquecer o modelo:

| Variável             | Descrição                                                                 |
|----------------------|--------------------------------------------------------------------------|
| `prazo_estimado`     | Dias entre a compra e a entrega estimada                                 |
| `dia_semana_compra`  | Dia da semana em que o pedido foi feito (0 = segunda, 6 = domingo)       |
| `regiao_cliente`     | Macro-região do cliente com base no estado                               |

As variáveis categóricas foram transformadas em dummies para uso no modelo.

---

## 📌 SMOTE — Balanceamento de Classes

O dataset apresentava forte desequilíbrio:

- Classe 0 (no prazo): ~93%
- Classe 1 (com atraso): ~7%

Utilizamos **SMOTE (Synthetic Minority Oversampling Technique)** para criar exemplos sintéticos da classe minoritária no conjunto de treino.

---

## 📊 Avaliação do Modelo (com SMOTE)

### 🔍 Matriz de Confusão:


### 📈 Métricas:

| Classe         | Precisão | Recall | F1-score |
|----------------|----------|--------|----------|
| **Sem atraso** | 0.97     | 0.97   | 0.97     |
| **Com atraso** | 0.55     | 0.51   | 0.53     |

- **Accuracy geral:** 94%
- **Macro F1-score:** 0.75

📌 O modelo passou a identificar **mais da metade dos atrasos**, melhorando sensivelmente o recall da classe 1.

---

## 🎯 Principais Variáveis do Modelo

| Variável                  | Importância |
|---------------------------|-------------|
| `review_score`            | 0.289       |
| `review_category_Ruim`    | 0.287       |
| `customer_zip_code_prefix`| 0.096       |
| `freight_value`           | 0.083       |
| `price`                   | 0.078       |
| `prazo_estimado`          | 0.071       |
| `dia_semana_compra`       | 0.038       |

Essas variáveis indicam que **satisfação passada, localização e logística** são bons preditores de atraso.

---

## ✅ Conclusão da Etapa 4

Com a aplicação de SMOTE, conseguimos **aumentar a sensibilidade do modelo para detectar atrasos**, mantendo alta acurácia geral.  
As novas variáveis criadas via feature engineering ajudaram o modelo a captar padrões que não estavam evidentes anteriormente.

# 📊 **Etapa 5 Crisp-DM - Avaliação dos Resultados**

Nesta etapa, avaliamos se o modelo atende aos critérios definidos no entendimento do negócio. O foco está em validar a **eficácia preditiva**, **confiabilidade das previsões** e o **potencial impacto no problema real**: atrasos na entrega.

---

## 🎯 Objetivo

Verificar se o modelo treinado consegue **prever os pedidos que serão entregues com atraso**, auxiliando na tomada de decisão logística e na melhoria da experiência do cliente.

---

## 📌 Avaliação Técnica

| Métrica                      | Valor         |
|------------------------------|---------------|
| **Acurácia**                 | 94%           |
| **Recall da classe "com atraso"** | **51%**     |
| **Precisão da classe "com atraso"** | 55%      |
| **F1-score da classe "com atraso"** | 53%      |

📌 Após aplicar **SMOTE** e criar novas variáveis via **feature engineering**, o modelo aumentou consideravelmente sua **sensibilidade (recall)** para identificar atrasos.

---

## 📊 Matriz de Confusão


- O modelo acerta 51% dos atrasos reais
- Mantém altíssima acurácia para as entregas no prazo

---

## 🔍 Interpretação das Principais Variáveis

| Variável                  | Importância | Interpretação |
|---------------------------|-------------|----------------|
| `review_score`            | Alta        | Clientes com histórico de insatisfação tendem a repetir problemas |
| `review_category_Ruim`    | Alta        | Agrava o risco de atraso |
| `customer_zip_code_prefix`| Média       | Regiões específicas têm mais atrasos |
| `freight_value`           | Média       | Fretes altos sugerem complexidade ou urgência |
| `prazo_estimado`          | Média       | Prazos curtos elevam risco |
| `dia_semana_compra`       | Baixa       | Compras em certos dias têm mais risco (ex: sexta) |

---

## ✅ Avaliação de Negócio

- 🎯 O modelo é **tecnicamente sólido** e oferece previsões com **bom equilíbrio entre precisão e recall**
- ⚠️ Erros ainda ocorrem, mas **o modelo é significativamente melhor do que o aleatório**
- ✅ É possível utilizá-lo para **classificação de risco de atraso em tempo real**, com destaque para:
  - Priorização de pedidos
  - Alerta para equipes logísticas
  - Ajuste de prazos e comunicação ao cliente

---

## ⚠️ Limitações e Oportunidades

| Limitação                         | Possível Solução                         |
|----------------------------------|------------------------------------------|
| Falta de dados operacionais (transportadora, tipo de frete) | Integração com dados logísticos |
| Granularidade alta do CEP        | Agrupar por região, estado, clusters     |
| Modelo não interpretável por todos | Aplicar SHAP ou LIME para explicabilidade |
| Pode melhorar com outro algoritmo | Testar com **XGBoost** ou **LightGBM**   |

---

## ✅ Conclusão da Etapa 5

O modelo atinge um nível de desempenho **adequado para uso prático** dentro da Olist.  
Com um recall de 51% para atrasos e acurácia total de 94%, já é possível:

- Antecipar riscos
- Otimizar a operação
- Melhorar a comunicação com o cliente

📦 Com isso, estamos prontos para seguir para a **Etapa 6 — Implantação**, onde definiremos como o modelo será integrado à rotina operacional da empresa.

# 🚀 **Etapa 6 Crisp-DM: Implantação**

A etapa de **implementação** consiste em transformar os insights e modelos desenvolvidos em uma solução funcional que possa ser utilizada por stakeholders do negócio. No contexto do projeto da Olist, essa etapa envolveu a criação de um protótipo de aplicação utilizando **Streamlit** = https://prever-atrasos---olist-7xdmub5jkf3xk4fhg2gfpb.streamlit.app/, capaz de prever a probabilidade de atraso em entregas com base em variáveis selecionadas.

---

## ✅ Objetivo da Implementação

Criar um sistema que permita prever o risco de atraso na entrega de um pedido com base nas seguintes informações:

- Preço do produto
- Valor do frete
- Prazo estimado de entrega
- Dia da semana da compra
- Estado e região do cliente
- Nota da avaliação anterior (se houver)

---

## ⚙️ Ferramentas Utilizadas

- **Python**: Linguagem base para modelagem e análise de dados.
- **Scikit-learn**: Biblioteca utilizada para o treinamento e avaliação do modelo Random Forest.
- **Pandas** e **NumPy**: Para tratamento de dados.
- **Streamlit**: Para criação da interface web simples e interativa.
- **SHAP**: Para explicar as previsões do modelo de forma interpretável.

---

## 🧠 Modelo de Machine Learning

O modelo utilizado foi um **Random Forest Classifier**, treinado para prever a variável `delivery_delay` (atraso na entrega). Após testes com balanceamento via SMOTE e inclusão de variáveis derivadas, o modelo atingiu:

- Acurácia geral: **94%**
- F1-score para classe de atraso: **0.53**
- Principais variáveis: `review_score`, `freight_value`, `price`, `prazo_estimado`, `customer_zip_code_prefix`

---

## 🖥️ Interface Desenvolvida (Streamlit)

A aplicação permite ao usuário preencher campos com as informações do pedido. Em seguida, o modelo calcula:

- Probabilidade de atraso
- Classificação: “Entrega prevista no prazo” ou “Risco de atraso”
- Explicação da previsão utilizando gráficos SHAP (quando possível)

---

## 🚧 Limitações e Considerações

- A interface atual é um **protótipo funcional**, mas pode ser aprimorada para uso em produção.
- O modelo não contempla casos onde o cliente **nunca avaliou pedidos anteriores** — uma possível melhoria seria tratar essas entradas como “sem nota”.
- O modelo requer pré-processamento específico e pode ser sensível à entrada de dados inválidos ou faltantes.

---

## ✅ Próximos Passos

- Integrar o modelo com dados reais da Olist (via API ou dashboard)
- Criar um sistema de monitoramento contínuo da acurácia do modelo
- Automatizar o re-treinamento com novos dados operacionais

