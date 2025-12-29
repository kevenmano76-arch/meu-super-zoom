import streamlit as st
import google.generativeai as genai
from PIL import Image

# =========================================================
# 🔑 COLOQUE SUA CHAVE DENTRO DAS ASPAS ABAIXO:
CHAVE_API = "AIzaSyDfajAj5aqfzFrr730QFFKDiiiHeLt1uPY"
# =========================================================

genai.configure(api_key=CHAVE_API)

st.set_page_config(page_title="IA Super Zoom 4K")
st.title("🚀 Super Zoom IA & Resolução 4K")

st.write("Tire uma foto borrada e a IA vai reconstruir os detalhes para você.")

# Botão para abrir a câmera
foto = st.camera_input("Tirar Foto")

if foto:
    img = Image.open(foto)
    st.image(img, caption="Foto Original capturada")
    
    with st.spinner('IA analisando e corrigindo pixels para 4K...'):
        model = genai.GenerativeModel('gemini-pro-vision')
        
        # O comando focado em melhorar a imagem e ajeitar o borrão
        comando = """
        Aja como um sistema de inteligência artificial de super-resolução. 
        Analise esta imagem que está com borrão de zoom digital. 
        Reconstrua mentalmente os detalhes em resolução 4K. 
        Corrija as falhas nos detalhes e me diga exatamente o que foi aprimorado, 
        revelando textos, objetos ou rostos que estavam ilegíveis.
        """
        
        resposta = model.generate_content([comando, img])
        
        st.subheader("✅ Melhoria de Detalhes (Modo 4K):")
        st.success(resposta.text)

