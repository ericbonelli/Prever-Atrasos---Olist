import streamlit as st
import pandas as pd
import joblib
import shap
import matplotlib.pyplot as plt

# Carregar modelo e colunas
model = joblib.load("modelo_atraso.pkl")
colunas = joblib.load("colunas_modelo.pkl")

st.set_page_config(page_title="Previsão de Atraso na Entrega", layout="centered")
st.title("📦 Previsão de Atraso na Entrega — Olist")

st.markdown("Preencha as informações do pedido abaixo para estimar o risco de atraso na entrega.")

# === Inputs do usuário ===

st.subheader("🛒 Informações do Pedido")

price = st.number_input("💰 Preço do produto (R$)", min_value=0.0, value=100.0, step=10.0)
freight_value = st.number_input("🚚 Valor do frete (R$)", min_value=0.0, value=20.0, step=1.0)
prazo_estimado = st.number_input("📆 Prazo estimado de entrega (dias)", min_value=1, value=7)
dia_semana = st.selectbox("📅 Dia da semana da compra",
                          options={0: "Segunda", 1: "Terça", 2: "Quarta", 3: "Quinta", 4: "Sexta", 5: "Sábado", 6: "Domingo"},
                          format_func=lambda x: f"{x} - {['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'][x]}")

st.subheader("👤 Perfil do Cliente")

cliente_novo = st.checkbox("🆕 Cliente novo (sem histórico de nota)?", value=False)

if not cliente_novo:
    review_score = st.slider("⭐ Nota média do cliente (1 a 5)", 1, 5, value=5)
    review_ruim = st.checkbox("🔴 Cliente já deu nota 1 ou 2?")
    review_neutro = st.checkbox("🟡 Cliente já deu nota 3?")
else:
    review_score = 3
    review_ruim = False
    review_neutro = False

regioes = ["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"]
regiao = st.selectbox("🗺️ Região do cliente", regioes)

# === Montar input do modelo ===

linha = dict.fromkeys(colunas, 0)
linha["price"] = price
linha["freight_value"] = freight_value
linha["review_score"] = review_score
linha["review_category_Ruim"] = int(review_ruim)
linha["review_category_Neutro"] = int(review_neutro)
linha["prazo_estimado"] = prazo_estimado
linha["dia_semana_compra"] = dia_semana

# Dummy para região
col_regiao = f"regiao_cliente_{regiao}"
if col_regiao in colunas:
    linha[col_regiao] = 1

entrada = pd.DataFrame([linha], columns=colunas)

# === Previsão ===

if st.button("🔮 Prever Atraso"):
    pred = model.predict(entrada)[0]
    prob = model.predict_proba(entrada)[0][1]

    st.subheader("📊 Resultado")
    if pred == 1:
        st.error(f"⚠️ Alta chance de **atraso**.\nProbabilidade: {prob:.1%}")
    else:
        st.success(f"✅ Entrega prevista **no prazo**.\nRisco de atraso: {prob:.1%}")

    # === Explicação com SHAP ===
    st.subheader("🔍 Explicação da Previsão")

    explainer = shap.TreeExplainer(model)  # SEM CACHE
    shap_values = explainer.shap_values(entrada)

    st.markdown("O gráfico abaixo mostra como cada variável influenciou a previsão:")

    fig, ax = plt.subplots(figsize=(10, 4))
    shap.plots._waterfall.waterfall_legacy(
        explainer.expected_value[1],
        shap_values[1][0],
        feature_names=entrada.columns,
        max_display=10,
        show=False
    )
    st.pyplot(fig)
