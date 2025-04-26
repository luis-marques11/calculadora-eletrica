import streamlit as st

# Função de cálculo da Lei de Ohm
def ohm_calculator(v, i, r):
    if v is None:
        return i * r  # V = I * R
    elif i is None:
        return v / r  # I = V / R
    elif r is None:
        return v / i  # R = V / I

# Função de cálculo de Potência Elétrica
def potencia_calculator(v, i, r):
    if v is not None and i is not None:
        return v * i  # P = V * I
    elif i is not None and r is not None:
        return i ** 2 * r  # P = I² * R
    elif v is not None and r is not None:
        return v ** 2 / r  # P = V² / R

# Função de cálculo de resistência equivalente
def resistor_calculator(r1, r2, type_):
    if type_ == "série":
        return r1 + r2  # Resistores em série: Req = R1 + R2
    elif type_ == "paralelo":
        return 1 / (1 / r1 + 1 / r2)  # Resistores em paralelo: 1/Req = 1/R1 + 1/R2

# Função para conversão de unidades
def conversao(valor, tipo):
    if tipo == "mA ↔ A":
        return valor / 1000  # mA para A
    elif tipo == "kΩ ↔ Ω":
        return valor * 1000  # kΩ para Ω

# Layout do Streamlit
st.title("Calculadora Elétrica ⚡")
option = st.selectbox("Escolha o cálculo:", ["Lei de Ohm", "Potência Elétrica", "Associação de Resistores", "Conversão de Unidades"])

if option == "Lei de Ohm":
    st.subheader("Lei de Ohm (V, I, R)")
    v = st.number_input("Tensão (V)", value=None, step=0.1)
    i = st.number_input("Corrente (I)", value=None, step=0.1)
    r = st.number_input("Resistência (R)", value=None, step=0.1)

    if v or i or r:
        resultado = ohm_calculator(v, i, r)
        st.write(f"Resultado: {resultado}")

elif option == "Potência Elétrica":
    st.subheader("Potência Elétrica (P)")
    v = st.number_input("Tensão (V)", value=None, step=0.1)
    i = st.number_input("Corrente (I)", value=None, step=0.1)
    r = st.number_input("Resistência (R)", value=None, step=0.1)

    if v or i or r:
        resultado = potencia_calculator(v, i, r)
        st.write(f"Resultado: {resultado}")

elif option == "Associação de Resistores":
    st.subheader("Associação de Resistores")
    r1 = st.number_input("Resistor 1 (Ω)", value=None, step=0.1)
    r2 = st.number_input("Resistor 2 (Ω)", value=None, step=0.1)
    type_ = st.selectbox("Tipo de Associação", ["série", "paralelo"])

    if r1 and r2:
        resultado = resistor_calculator(r1, r2, type_)
        st.write(f"Resultado: {resultado}")

elif option == "Conversão de Unidades":
    st.subheader("Conversão de Unidades")
    valor = st.number_input("Valor", value=None, step=0.1)
    tipo = st.selectbox("Escolha a conversão", ["mA ↔ A", "kΩ ↔ Ω"])

    if valor:
        resultado = conversao(valor, tipo)
        st.write(f"Resultado: {resultado}")

# Executar o aplicativo Streamlit
