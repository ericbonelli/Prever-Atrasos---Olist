import streamlit as st
import pandas as pd
import joblib

# Carregar modelo e colunas
model = joblib.load("modelo_atraso.pkl")
colunas = joblib.load("colunas_modelo.pkl")

st.set_page_config(page_title="Previsão de Atraso", layout="centered")
st.title("📦 Previsão de Atraso na Entrega — Olist")

st.markdown("Preencha as informações do pedido abaixo para prever o risco de atraso:")

# Inputs do usuário
price = st.number_input("💰 Preço do produto (R$)", min_value=0.0, value=100.0, step=10.0)
freight_value = st.number_input("🚚 Valor do frete (R$)", min_value=0.0, value=20.0, step=1.0)
review_score = st.slider("⭐ Nota média do cliente (1 a 5)", 1, 5, value=5)
review_ruim = st.checkbox("🔴 Cliente com avaliação ruim?")
review_neutro = st.checkbox("🟡 Cliente com avaliação neutra?")
prazo_estimado = st.number_input("📆 Prazo estimado de entrega (dias)", min_value=1, value=7)
dia_semana = st.selectbox("📅 Dia da semana da compra", {
    0: "Segunda", 1: "Terça", 2: "Quarta", 3: "Quinta", 4: "Sexta", 5: "Sábado", 6: "Domingo"
})

# Região do cliente
regioes = ["Centro-Oeste", "Nordeste", "Norte", "Sudeste", "Sul"]
regiao = st.selectbox("🗺️ Região do cliente", regioes)

# Preparar entrada para o modelo
linha = dict.fromkeys(colunas, 0)
linha["price"] = price
linha["freight_value"] = freight_value
linha["review_score"] = review_score
linha["review_category_Ruim"] = int(review_ruim)
linha["review_category_Neutro"] = int(review_neutro)
linha["prazo_estimado"] = prazo_estimado
linha["dia_semana_compra"] = dia_semana

# Ativar dummy da região
col_regiao = f"regiao_cliente_{regiao}"
if col_regiao in colunas:
    linha[col_regiao] = 1

# Criar DataFrame com os valores certos
entrada = pd.DataFrame([linha], columns=colunas)

# Prever
if st.button("🔮 Prever Atraso"):
    pred = model.predict(entrada)[0]
    prob = model.predict_proba(entrada)[0][1]

    st.subheader("📊 Resultado")
    if pred == 1:
        st.error(f"⚠️ Alta chance de atraso! Probabilidade: {prob:.1%}")
    else:
        st.success(f"✅ Entrega prevista no prazo. Risco de atraso: {prob:.1%}")