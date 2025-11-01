import streamlit as st
from utils import check_password

if not check_password():
    st.stop()

st.set_page_config(page_title="Ferramentas Utilizadas", page_icon="🛠️", layout="wide")
st.title("🛠️ Ferramentas e Tecnologias Utilizadas")
st.markdown("---")

# Dividi em colunas para organizar melhor o conteúdo
col1, col2 = st.columns(2)

with col1:
    st.subheader("Desenvolvimento e Versionamento")
    st.markdown("- **IDE:** Visual Studio Code")
    st.markdown("- **Controle de Versão:** Git / GitHub")

    st.subheader("Plataformas de Análise e IA")
    st.markdown("- **Linguagem:** Python 3.10+")
    st.markdown("- **Testes de Algoritmos:** Google Colab (para prototipagem e teste dos modelos supervisionados)")
    st.markdown("- **API de IA:** Google Gemini (modelo `gemini-pro-latest`)")

    st.subheader("Aplicação Web e Deploy")
    st.markdown("- **Framework Web:** Streamlit")
    st.markdown("- **Hospedagem:** Streamlit Community Cloud (gratuito)")

    st.subheader("Banco de Dados e Coleta")
    st.markdown("- **Coleta:** API do Twitter/X (v1.1 e v2)")
    st.markdown("- **Armazenamento:** PostgreSQL (hospedado no Render.com)")


with col2:
    st.subheader("Principais Bibliotecas (Python)")
    st.markdown("- **Aplicação Web:** `streamlit`")
    st.markdown("- **Segurança (Login):** `bcrypt`")
    st.markdown("- **Banco de Dados:** `SQLAlchemy`, `psycopg2-binary`")
    st.markdown("- **Análise de Dados:** `pandas`")
    st.markdown("- **NLP e ML:** `scikit-learn`, `nltk`")
    st.markdown("- **Visualização:** `matplotlib`, `wordcloud`, `plotly`")
    st.markdown("- **API de IA:** `google.generativeai`")

    # Adicionando as especificações do computador da imagem
    st.subheader("Ambiente de Desenvolvimento (Hardware)")
    st.markdown("As análises e o desenvolvimento foram realizados no computador 'PC-DEV' com as seguintes especificações:")
    with st.expander("Clique para ver as especificações"):
        # Referencia a imagem que você enviou
        st.image("image_fac62a.png", caption="Especificações do dispositivo de desenvolvimento")
        st.markdown(
            """
            - **Processador (CPU):** AMD Ryzen 7 5800X 8-Core (3.80 GHz)
            - **Memória RAM:** 32,0 GB
            - **Placa de Vídeo (GPU):** Radeon RX550/550 Series (4 GB)
            - **Armazenamento:** 932 GB
            - **Sistema Operacional:** Windows (64 bits, processador x64)
            """
        )
        st.caption("Nota: Para a imagem carregar, o arquivo 'image_fac62a.png' deve estar na pasta raiz do projeto (junto com 'app.py').")
