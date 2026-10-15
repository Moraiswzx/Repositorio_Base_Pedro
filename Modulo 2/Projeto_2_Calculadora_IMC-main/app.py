import streamlit as st

#-------------------------------- SIDEBAR
st.sidebar.title("Calculadora de IMC")



#------------------------------- BODY
st.title("Calculadora de IMC")

peso = st.text_input("Digite seu peso:", 0.0)
altura = st.text_input("Digite sua altura:", 0.0)

if st.button("Calcular"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        class_imc = "abaixopeso"
        st.warning(f"Seu IMC é {imc:.2f}. Você está abaixo do peso")

    elif imc < 24.9:
        class_imc = "pesosaudavel"
        st.success(f"Seu IMC é {imc:.2f}. Seu peso é saudável!")
     
    elif imc < 29.9:
        class_imc = "sobrepeso"
        st.success(f"Seu IMC é {imc:.2f}. Você está com sobrepeso!")

            
    elif imc < 34.9:
        class_imc = "obesidade1"
        st.success(f"Seu IMC é {imc:.2f}. Você está com Obsidade Grau 1!")

    elif imc < 39.9:
        class_imc = "obesidade2"
        st.success(f"Seu IMC é {imc:.2f}. Você está com Obsidade Grau 2!")

    else:
        class_imc = "obesidade3"
        st.success(f"Seu IMC é {imc:.2f}. Você está com Obsidade Grau 3!")

    st.markdown("- - -")

    st.image(f"{class_imc}.png")

    with open(f"{class_imc}.txt", "r", encoding="utf-8") as f:
        texto = f.read()

    st.markdown(texto)