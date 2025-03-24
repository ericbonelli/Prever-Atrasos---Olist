# Explicação com SHAP
st.subheader("🔍 Explicação da Previsão")

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(entrada)

st.markdown("O gráfico abaixo mostra como cada variável influenciou a previsão:")

fig, ax = plt.subplots(figsize=(10, 4))
shap.plots._waterfall.waterfall_legacy(
    explainer.expected_value[0],
    shap_values[0][0],
    feature_names=entrada.columns,
    max_display=10,
    show=False
)
st.pyplot(fig)
