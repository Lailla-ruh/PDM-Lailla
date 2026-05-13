import streamlit as st

st.image("fotolailla.jpeg")
st.write("Site Lailla")
st.link_button("Acessar", "https://sites.google.com/d/19rZhooAY66aV-K0EKjCHUDInYhGcLZdV/p/1RbMTpxwYMKlFabiPhgpLbYpQQL6Rrco1/edit")
import streamlit as st
import base64
# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("logo coke.png")
zap_base64 = get_base64_image("zap.avif")

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://www.coca-cola.com/br/pt" target="_blank">
                <img src="data:image/png;base64,{img_base64}"
                     width="320"
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:
    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Lailla!</b>
    </div>
    """, unsafe_allow_html=True)

    subcol1, subcol2 = st.columns([1,4])

    with subcol1:
        st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            height: 100%;
        ">
        """, unsafe_allow_html=True)

        st.image("Cerejeira.png", width=800)

        st.markdown("</div>", unsafe_allow_html=True)

    # TEXTO
    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
            width: 100%;
            max-width: none;
        ">
            <b>Sobre mim<br>
          Meu nome é Lailla Ruhanny. Nasci em Itabaiana e moro em Salgado de São Félix.
        Sou estudante e gosto de aprender coisas novas. No meu dia a dia, 
        gosto de ouvir música, passar tempo com minha família e amigos e aproveitar 
        momentos de descanso e lazer. 
        </div>
        """, unsafe_allow_html=True)

with col_right:
    st.empty()

st.markdown(f"""
    <div style="text-align: center; margin-top: 10px;">
        <a href="https://wa.me/+55883981954690" target="_blank">
            <img src="data:image/avif;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
