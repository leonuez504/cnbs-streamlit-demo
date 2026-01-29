
import streamlit as st

st.title("CNBS – Registro de Movimiento de Personal")

st.subheader("Formulario demostrativo (solo visual)")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Número de Empleado")
    st.text_input("Nombre Completo")
    st.text_input("Dependencia")
    st.text_input("Cargo Actual")

with col2:
    st.selectbox("Tipo de Movimiento", ["Ascenso", "Traslado", "Nombramiento"])
    st.text_input("Nuevo Cargo / Dependencia")
    st.date_input("Fecha del Movimiento")
    st.text_area("Observaciones")

st.button("Guardar (solo demostración)")

st.caption("Modelo visual para diseño del sistema – CNBS")

