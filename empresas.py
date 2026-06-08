import streamlit as st

# =========================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================
st.set_page_config(
    page_title="Plataformas de Assistir Filmes e Séries",
    page_icon="🌐",
    layout="wide"
)

# =========================================
# TÍTULO
# =========================================
st.title("Plataformas de Assistir Filmes e Séries")
st.write("Confira algumas plataformas para assistir filmes e séries")

# =========================================
# COLUNAS
# =========================================
col1, col2, col3 = st.columns(3)

# =========================================
# EMPRESA 1
# =========================================
with col1:
    st.image("empresa1.png", use_container_width=True)
    st.subheader("Netflix")
    st.write("A Netflix é um popular serviço de streaming por assinatura que permite assistir a filmes, séries, documentários e animes sem anúncios e sob demanda.")
    st.link_button(
        "Acessar Site",
        "https://www.netflix.com/br/"
    )

# =========================================
# EMPRESA 2
# =========================================
with col2:
    st.image("empresa2.png", use_container_width=True)
    st.subheader("Prime Video")
    st.write("O Prime Video é o serviço de streaming por assinatura da Amazon. Ele oferece um vasto catálogo de filmes, séries, produções originais (como The Boys) e canais de TV ao vivo.")
    st.link_button(
        "Acessar Site",
        "https://www.primevideo.com/"
    )

# =========================================
# EMPRESA 3
# =========================================
with col3:
    st.image("empresa3.jpg", use_container_width=True)
    st.subheader("HBO")
    st.write("HBO é uma famosa rede de TV paga americana e um serviço global de streaming de propriedade da Warner Bros. Discovery.")
    st.link_button(
        "Acessar Site",
        "https://www.hbomax.com/br/pt"
    )

# =========================================
# RODAPÉ
# =========================================
st.write("---")
st.write("Desenvolvido por Lailla Ruhanny")
