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

