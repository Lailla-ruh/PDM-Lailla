import streamlit as st
import pandas as pd
import os
import base64

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="TechClientes PRO",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "clientes.csv"

# ============================================================
# CAMINHOS DAS IMAGENS
# ============================================================

IMAGEM_HERO = os.path.join(
    "imagens",
    "hero.jpg"
)

IMAGEM_CLIENTES = os.path.join(
    "imagens",
    "clientes.jpg"
)

# ============================================================
# FUNÇÃO PARA CONVERTER IMAGEM EM BASE64
# ============================================================

def imagem_base64(caminho):

    if not os.path.exists(caminho):
        return None

    try:
        with open(caminho, "rb") as arquivo:
            return base64.b64encode(
                arquivo.read()
            ).decode()

    except Exception:
        return None


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* ============================================================
   FUNDO
   ============================================================ */

.stApp {
    background: linear-gradient(
        135deg,
        #F0F0E5 0%,
        #E1E4C8 50%,
        #D4DCB5 100%
    );
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ============================================================
   SIDEBAR
   ============================================================ */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #162630,
        #223944
    );

    border-right: 2px solid #77864B;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

.logo-title {
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 11px;
    font-weight: 700;
    color: #BFCB9C !important;
    letter-spacing: 1px;
}

/* ============================================================
   TÍTULOS
   ============================================================ */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #26311F !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 17px;
    color: #46513B !important;
    margin-bottom: 30px;
}

/* ============================================================
   HERO
   ============================================================ */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.22);
}

.hero-image {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background: linear-gradient(
        90deg,
        rgba(14,28,38,0.97) 0%,
        rgba(14,28,38,0.86) 45%,
        rgba(14,28,38,0.18) 100%
    );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;
    transform: translateY(-50%);
    max-width: 580px;
    z-index: 2;
}

.hero-number {
    font-size: 70px;
    font-weight: 800;
    color: #A4D080 !important;
    line-height: 1;
}

.hero-title {
    font-size: 46px;
    font-weight: 800;
    color: #FFFFFF !important;
    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #E8EDDE !important;
    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;
    margin-top: 24px;
    padding: 10px 22px;
    border-radius: 30px;
    background: #6E8040;
    color: #FFFFFF !important;
    font-size: 14px;
    font-weight: 700;
}

/* ============================================================
   CARDS
   ============================================================ */

.info-card {
    background: #FFFFFF;
    border-radius: 22px;
    padding: 28px;
    min-height: 170px;

    border: 1px solid rgba(
        111,
        128,
        63,
        0.30
    );

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-number {
    font-size: 34px;
    font-weight: 800;
    color: #26311F !important;
    margin-top: 10px;
}

.card-label {
    font-size: 14px;
    font-weight: 700;
    color: #566248 !important;
    margin-top: 5px;
}

/* ============================================================
   CARD ESCURO
   ============================================================ */

.dark-card {
    background: linear-gradient(
        135deg,
        #152631,
        #233C48
    );

    border-radius: 24px;
    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #E2E9DA !important;
    line-height: 1.7;
}

/* ============================================================
   IMAGEM SECUNDÁRIA
   ============================================================ */

.secondary-image {
    width: 100%;
    height: 100%;
    min-height: 260px;
    max-height: 330px;

    object-fit: cover;

    border-radius: 24px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

/* ============================================================
   FORMULÁRIO
   ============================================================ */

[data-testid="stForm"] {
    background: rgba(
        255,
        255,
        255,
        0.88
    );

    padding: 30px;

    border-radius: 25px;

    border: 1px solid #B8C391;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}

[data-testid="stWidgetLabel"] label,
.stTextInput label,
.stSelectbox label,
.stTextArea label {
    color: #26311F !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}

/* ============================================================
   INPUTS
   ============================================================ */

.stTextInput input,
.stTextArea textarea {

    background-color: #FFFFFF !important;

    color: #202820 !important;

    border: 2px solid #7C8956 !important;

    border-radius: 12px !important;

    font-size: 16px !important;
}

/* ============================================================
   SELECTBOX
   ============================================================ */

[data-baseweb="select"] > div {

    background-color: #2F323C !important;

    border: 2px solid #687548 !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] * {
    color: #FFFFFF !important;
}

/* ============================================================
   BOTÕES
   ============================================================ */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    background: linear-gradient(
        135deg,
        #52632D,
        #788B48
    ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(
            82,
            99,
            45,
            0.25
        );
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    background: linear-gradient(
        135deg,
        #435323,
        #687A3D
    ) !important;
}

/* ============================================================
   DATAFRAME
   ============================================================ */

[data-testid="stDataFrame"] {
    border-radius: 15px;
    overflow: hidden;
}

/* ============================================================
   FOOTER
   ============================================================ */

.footer {

    margin-top: 50px;

    text-align: center;

    color: #536044 !important;

    font-size: 14px;

    font-weight: 600;
}

/* ============================================================
   RESPONSIVO
   ============================================================ */

@media (max-width: 900px) {

    .hero-container {
        height: 500px;
    }

    .hero-title {
        font-size: 36px;
    }

    .hero-number {
        font-size: 55px;
    }

    .hero-content {
        left: 6%;
        right: 6%;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNÇÕES DE DADOS
# ============================================================

def carregar_dados():

    colunas = [
        "Nome",
        "CPF_CNPJ",
        "Telefone",
        "Email",
        "Cidade",
        "Endereco",
        "Tipo",
        "Observacoes"
    ]

    if not os.path.exists(ARQUIVO):

        return pd.DataFrame(
            columns=colunas
        )

    try:

        dados = pd.read_csv(
            ARQUIVO,
            encoding="utf-8-sig"
        )

    except Exception:

        return pd.DataFrame(
            columns=colunas
        )

    for coluna in colunas:

        if coluna not in dados.columns:

            dados[coluna] = ""

    return dados[colunas]


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# ============================================================
# CARREGAR CLIENTES
# ============================================================

df = carregar_dados()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    """
<div class="logo-title">
    TechClientes
</div>

<div class="logo-subtitle">
    GESTÃO DE CLIENTES
</div>
""",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)

menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "Dashboard",
        "+ Cadastrar Cliente",
        "Clientes Cadastrados"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "TechClientes PRO 2026"
)


# ============================================================
# DASHBOARD
# ============================================================

if menu == "Dashboard":

    # --------------------------------------------------------
    # IMAGEM HERO
    # --------------------------------------------------------

    hero_base64 = imagem_base64(
        IMAGEM_HERO
    )

    if hero_base64:

        st.markdown(
            f"""
<div class="hero-container">

    <img
        class="hero-image"
        src="data:image/jpeg;base64,{hero_base64}"
    >

    <div class="hero-overlay"></div>

    <div class="hero-content">

        <div class="hero-number">
            01.
        </div>

        <div class="hero-title">
            Seus clientes.<br>
            Total controle.
        </div>

        <div class="hero-text">
            Gerencie seus clientes em um só lugar.<br>
            Cadastre, consulte e mantenha suas informações
            organizadas de forma simples e profissional.
        </div>

        <div class="hero-badge">
            GESTÃO INTELIGENTE
        </div>

    </div>

</div>
""",
            unsafe_allow_html=True
        )

    else:

        # Caso a imagem não exista,
        # mostra um Hero sem imagem.

        st.markdown(
            """
<div class="hero-container"
     style="
     background:
     linear-gradient(
        135deg,
        #162630,
        #314A35
     );
     ">

    <div class="hero-content">

        <div class="hero-number">
            01.
        </div>

        <div class="hero-title">
            Seus clientes.<br>
            Total controle.
        </div>

        <div class="hero-text">
            Gerencie seus clientes em um só lugar.<br>
            Cadastre, consulte e mantenha suas informações
            organizadas de forma simples e profissional.
        </div>

        <div class="hero-badge">
            GESTÃO INTELIGENTE
        </div>

    </div>

</div>
""",
            unsafe_allow_html=True
        )

        st.warning(
            "Coloque a imagem hero.jpg dentro da pasta imagens."
        )

    # --------------------------------------------------------
    # TÍTULO
    # --------------------------------------------------------

    st.markdown(
        """
<div class="page-title">
    Visão geral dos clientes
</div>

<div class="page-subtitle">
    Acompanhe sua base de clientes e mantenha os cadastros atualizados.
</div>
""",
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # INDICADORES
    # --------------------------------------------------------

    total_clientes = len(df)

    clientes_pf = len(
        df[
            df["Tipo"]
            .astype(str)
            .str.upper()
            .str.strip()
            == "PESSOA FÍSICA"
        ]
    )

    clientes_pj = len(
        df[
            df["Tipo"]
            .astype(str)
            .str.upper()
            .str.strip()
            == "PESSOA JURÍDICA"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            f"""
<div class="info-card">

    <div class="card-number">
        {total_clientes}
    </div>

    <div class="card-label">
        CLIENTES CADASTRADOS
    </div>

</div>
""",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
<div class="info-card">

    <div class="card-number">
        {clientes_pf}
    </div>

    <div class="card-label">
        PESSOAS FÍSICAS
    </div>

</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
<div class="info-card">

    <div class="card-number">
        {clientes_pj}
    </div>

    <div class="card-label">
        PESSOAS JURÍDICAS
    </div>

</div>
""",
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # ÁREA INFORMATIVA
    # --------------------------------------------------------

    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )

    coluna1, coluna2 = st.columns(
        [1.1, 1]
    )

    with coluna1:

        st.markdown(
            """
<div class="dark-card">

    <h2>
        Gestão Profissional
    </h2>

    <p>
        O TechClientes PRO permite manter
        todos os seus clientes organizados
        em uma única plataforma.
    </p>

    <p>
        Consulte nomes, documentos, telefones,
        e-mails, endereços e demais informações
        com rapidez e praticidade.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

    with coluna2:

        imagem_clientes_base64 = imagem_base64(
            IMAGEM_CLIENTES
        )

        if imagem_clientes_base64:

            st.markdown(
                f"""
<img
    class="secondary-image"
    src="data:image/jpeg;base64,{imagem_clientes_base64}"
>
""",
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                """
<div class="dark-card">

    <h2>
        Clientes
    </h2>

    <p>
        Coloque a imagem clientes.jpg
        dentro da pasta imagens.
    </p>

</div>
""",
                unsafe_allow_html=True
            )


# ============================================================
# CADASTRAR CLIENTE
# ============================================================

elif menu == "+ Cadastrar Cliente":

    st.markdown(
        """
<div class="page-title">
    Novo Cliente
</div>

<div class="page-subtitle">
    Adicione um novo cliente à sua base de dados.
</div>
""",
        unsafe_allow_html=True
    )

    with st.form(
        "cadastro_cliente",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)

        # ----------------------------------------------------
        # COLUNA 1
        # ----------------------------------------------------

        with col1:

            nome = st.text_input(
                "Nome / Razão Social",
                placeholder="Digite o nome do cliente"
            )

            cpf_cnpj = st.text_input(
                "CPF / CNPJ",
                placeholder="Digite o CPF ou CNPJ"
            )

            telefone = st.text_input(
                "Telefone / WhatsApp",
                placeholder="(00) 00000-0000"
            )

            email = st.text_input(
                "E-mail",
                placeholder="cliente@email.com"
            )

        # ----------------------------------------------------
        # COLUNA 2
        # ----------------------------------------------------

        with col2:

            cidade = st.text_input(
                "Cidade",
                placeholder="Digite a cidade"
            )

            endereco = st.text_input(
                "Endereço",
                placeholder="Rua, número, bairro..."
            )

            tipo = st.selectbox(
                "Tipo de Cliente",
                [
                    "Pessoa Física",
                    "Pessoa Jurídica"
                ]
            )

            observacoes = st.text_area(
                "Observações",
                placeholder="Digite alguma observação..."
            )

        # ----------------------------------------------------
        # BOTÃO
        # ----------------------------------------------------

        cadastrar = st.form_submit_button(
            "CADASTRAR CLIENTE"
        )

        # ----------------------------------------------------
        # PROCESSAMENTO
        # ----------------------------------------------------

        if cadastrar:

            if not nome.strip():

                st.warning(
                    "Preencha o nome do cliente."
                )

            else:

                novo_cliente = pd.DataFrame(
                    [
                        {
                            "Nome": nome.strip(),

                            "CPF_CNPJ":
                                cpf_cnpj.strip(),

                            "Telefone":
                                telefone.strip(),

                            "Email":
                                email.strip(),

                            "Cidade":
                                cidade.strip(),

                            "Endereco":
                                endereco.strip(),

                            "Tipo":
                                tipo,

                            "Observacoes":
                                observacoes.strip()
                        }
                    ]
                )

                df = pd.concat(
                    [
                        df,
                        novo_cliente
                    ],
                    ignore_index=True
                )

                salvar_dados(df)

                st.success(
                    "Cliente cadastrado com sucesso!"
                )

                st.rerun()


# ============================================================
# CLIENTES CADASTRADOS
# ============================================================

elif menu == "Clientes Cadastrados":

    st.markdown(
        """
<div class="page-title">
    Clientes Cadastrados
</div>

<div class="page-subtitle">
    Consulte, pesquise e exclua clientes da sua base.
</div>
""",
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # NENHUM CLIENTE
    # --------------------------------------------------------

    if df.empty:

        st.markdown(
            """
<div class="dark-card">

    <h2>
        Nenhum cliente cadastrado
    </h2>

    <p>
        Sua base de clientes ainda está vazia.
        Cadastre seu primeiro cliente para começar.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # EXISTEM CLIENTES
    # --------------------------------------------------------

    else:

        busca = st.text_input(
            "Pesquisar cliente",
            placeholder=(
                "Digite nome, CPF/CNPJ, telefone, "
                "e-mail, cidade ou tipo..."
            )
        )

        # ----------------------------------------------------
        # FILTRO
        # ----------------------------------------------------

        if busca.strip():

            texto_busca = busca.strip()

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        texto_busca,
                        case=False,
                        na=False,
                        regex=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df

        # ----------------------------------------------------
        # RESULTADO
        # ----------------------------------------------------

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Nome": "Nome / Razão Social",
                "CPF_CNPJ": "CPF / CNPJ",
                "Telefone": "Telefone",
                "Email": "E-mail",
                "Cidade": "Cidade",
                "Endereco": "Endereço",
                "Tipo": "Tipo",
                "Observacoes": "Observações"
            }
        )

        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )

        # ----------------------------------------------------
        # EXCLUSÃO
        # ----------------------------------------------------

        opcoes_clientes = df.index.tolist()

        cliente_excluir = st.selectbox(
            "Selecione um cliente para excluir",

            options=opcoes_clientes,

            format_func=lambda indice:
                (
                    f"{df.loc[indice, 'Nome']} "
                    f"- "
                    f"{df.loc[indice, 'CPF_CNPJ']}"
                )
        )

        if st.button(
            "EXCLUIR CLIENTE"
        ):

            df = (
                df
                .drop(
                    index=cliente_excluir
                )
                .reset_index(
                    drop=True
                )
            )

            salvar_dados(df)

            st.success(
                "Cliente excluído com sucesso!"
            )

            st.rerun()


# ============================================================
# RODAPÉ
# ============================================================

st.markdown(
    """
<div class="footer">

    TechClientes PRO<br>

    Gestão inteligente de clientes

</div>
""",
    unsafe_allow_html=True
)
