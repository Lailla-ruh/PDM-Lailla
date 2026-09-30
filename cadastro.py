import streamlit as st
import pandas as pd
import os

# === CONFIGURAÇÃO DA PÁGINA ===
st.set_page_config(
    page_title="TechClientes PRO",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "clientes.csv"

# === IMAGENS ===
IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1556761175-b413da4baf72"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_CLIENTES = (
    "https://images.unsplash.com/"
    "photo-1521737711867-e3b97375f902"
    "?auto=format&fit=crop&w=1200&q=85"
)

# === CSS ===
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #F0F0E5 0%, #E1E4C8 50%, #D4DCB5 100%);
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #162630, #223944);
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

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;
    background-size: cover;
    background-position: center;
    box-shadow: 0 15px 35px rgba(0,0,0,0.22);
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

.info-card {
    background: #FFFFFF;
    border-radius: 22px;
    padding: 28px;
    min-height: 170px;
    border: 1px solid rgba(111,128,63,0.30);
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
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

.dark-card {
    background: linear-gradient(135deg, #152631, #233C48);
    border-radius: 24px;
    padding: 30px;
    box-shadow: 0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #E2E9DA !important;
    line-height: 1.7;
}

[data-testid="stForm"] {
    background: rgba(255,255,255,0.85);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid #B8C391;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

[data-testid="stWidgetLabel"] label,
.stTextInput label,
.stSelectbox label,
.stTextArea label {
    color: #26311F !important;
    font-size: 15px !important;
    font-weight: 700 !important;
}

.stTextInput input,
.stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #202820 !important;
    border: 2px solid #7C8956 !important;
    border-radius: 12px !important;
    font-size: 16px !important;
}

[data-baseweb="select"] > div {
    background-color: #2F323C !important;
    border: 2px solid #687548 !important;
    border-radius: 12px !important;
}

[data-baseweb="select"] * {
    color: #FFFFFF !important;
}

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #52632D, #788B48) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 14px !important;
    min-height: 54px;
    font-weight: 700 !important;
    box-shadow: 0 8px 18px rgba(82,99,45,0.25);
}

.footer {
    margin-top: 50px;
    text-align: center;
    color: #536044 !important;
    font-size: 14px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


# === FUNÇÕES ===

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

    if os.path.exists(ARQUIVO):

        try:
            dados = pd.read_csv(
                ARQUIVO,
                encoding="utf-8-sig"
            )

            for coluna in colunas:

                if coluna not in dados.columns:
                    dados[coluna] = ""

            return dados[colunas]

        except Exception:

            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False,
        encoding="utf-8-sig"
    )


# === CARREGAR DADOS ===

df = carregar_dados()

colunas_necessarias = [
    "Nome",
    "CPF_CNPJ",
    "Telefone",
    "Email",
    "Cidade",
    "Endereco",
    "Tipo",
    "Observacoes"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


# === SIDEBAR ===

st.sidebar.markdown(
    """
    <div class="logo-title">TechClientes</div>
    <div class="logo-subtitle">GESTÃO DE CLIENTES</div>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "Dashboard",
        "+ Cadastrar Cliente",
        "Clientes Cadastrados"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("TechClientes PRO 2026")


# ============================================================
# DASHBOARD
# ============================================================

if menu == "Dashboard":

    # === HERO ===

    st.html(
        f"""
        <div class="hero-container"
             style="background-image: url('{IMAGEM_HERO}');">

            <div class="hero-overlay"></div>

            <div class="hero-content">

                <div class="hero-number">01.</div>

                <div class="hero-title">
                    Seus clientes.<br>
                    Total controle.
                </div>

                <div class="hero-text">
                    Gerencie todos os seus clientes em um só lugar.<br>
                    Cadastre, consulte e acompanhe sua base de clientes
                    de forma ágil e profissional.
                </div>

                <div class="hero-badge">
                    GESTÃO INTELIGENTE
                </div>

            </div>

        </div>
        """
    )

    # === TÍTULO ===

    st.html(
        """
        <div class="page-title">
            Visão geral dos clientes
        </div>

        <div class="page-subtitle">
            Acompanhe sua base de clientes e mantenha os cadastros atualizados.
        </div>
        """
    )

    # === INDICADORES ===

    total_clientes = len(df)

    clientes_pf = len(
        df[
            df["Tipo"]
            .astype(str)
            .str.strip()
            .str.upper()
            == "PESSOA FÍSICA"
        ]
    )

    clientes_pj = len(
        df[
            df["Tipo"]
            .astype(str)
            .str.strip()
            .str.upper()
            == "PESSOA JURÍDICA"
        ]
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.html(
            f"""
            <div class="info-card">
                <div class="card-number">
                    {total_clientes}
                </div>

                <div class="card-label">
                    CLIENTES CADASTRADOS
                </div>
            </div>
            """
        )

    with col2:

        st.html(
            f"""
            <div class="info-card">
                <div class="card-number">
                    {clientes_pf}
                </div>

                <div class="card-label">
                    PESSOAS FÍSICAS
                </div>
            </div>
            """
        )

    with col3:

        st.html(
            f"""
            <div class="info-card">
                <div class="card-number">
                    {clientes_pj}
                </div>

                <div class="card-label">
                    PESSOAS JURÍDICAS
                </div>
            </div>
            """
        )

    # === ÁREA INFORMATIVA ===

    st.markdown("<br>", unsafe_allow_html=True)

    coluna1, coluna2 = st.columns([1.1, 1])

    with coluna1:

        st.html(
            """
            <div class="dark-card">

                <h2>
                    Gestão Profissional
                </h2>

                <p>
                    O TechClientes PRO permite manter
                    todos os clientes organizados e
                    cadastrados em um só lugar.
                </p>

                <p>
                    Monitore nomes, documentos, telefones,
                    e-mails e endereços com facilidade
                    através de uma interface limpa.
                </p>

            </div>
            """
        )

    with coluna2:

        st.image(
            IMAGEM_CLIENTES,
            use_container_width=True
        )


# ============================================================
# CADASTRAR CLIENTE
# ============================================================

elif menu == "+ Cadastrar Cliente":

    st.html(
        """
        <div class="page-title">
            Novo Cliente
        </div>

        <div class="page-subtitle">
            Adicione um novo cliente à sua base de dados.
        </div>
        """
    )

    with st.form(
        "cadastro_cliente",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)

        with col1:

            nome = st.text_input(
                "Nome / Razão Social"
            )

            cpf_cnpj = st.text_input(
                "CPF / CNPJ"
            )

            telefone = st.text_input(
                "Telefone / WhatsApp"
            )

            email = st.text_input(
                "E-mail"
            )

        with col2:

            cidade = st.text_input(
                "Cidade"
            )

            endereco = st.text_input(
                "Endereço"
            )

            tipo = st.selectbox(
                "Tipo de Cliente",
                [
                    "Pessoa Física",
                    "Pessoa Jurídica"
                ]
            )

            observacoes = st.text_area(
                "Observações"
            )

        cadastrar = st.form_submit_button(
            "CADASTRAR CLIENTE"
        )

        if cadastrar:

            if (
                nome.strip()
                and cpf_cnpj.strip()
                and telefone.strip()
            ):

                novo_cliente = pd.DataFrame(
                    [{
                        "Nome": nome.strip(),
                        "CPF_CNPJ": cpf_cnpj.strip().upper(),
                        "Telefone": telefone.strip(),
                        "Email": email.strip(),
                        "Cidade": cidade.strip(),
                        "Endereco": endereco.strip(),
                        "Tipo": tipo,
                        "Observacoes": observacoes.strip()
                    }]
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

            else:

                st.warning(
                    "Preencha Nome, CPF/CNPJ e Telefone."
                )


# ============================================================
# CLIENTES CADASTRADOS
# ============================================================

elif menu == "Clientes Cadastrados":

    st.html(
        """
        <div class="page-title">
            Clientes Cadastrados
        </div>

        <div class="page-subtitle">
            Consulte e pesquise todos os clientes cadastrados.
        </div>
        """
    )

    if df.empty:

        st.html(
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
            """
        )

    else:

        busca = st.text_input(
            "Pesquisar cliente",
            placeholder=(
                "Digite nome, CPF/CNPJ, telefone, "
                "e-mail, cidade ou tipo..."
            )
        )

        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
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

        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )

        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )

        opcoes_clientes = df.index.tolist()

        cliente_excluir = st.selectbox(
            "Selecione um cliente para excluir",
            options=opcoes_clientes,
            format_func=lambda indice:
                f"{df.loc[indice, 'Nome']} - "
                f"CPF/CNPJ: "
                f"{df.loc[indice, 'CPF_CNPJ']}"
        )

        if st.button(
            "EXCLUIR CLIENTE"
        ):

            df = (
                df
                .drop(cliente_excluir)
                .reset_index(drop=True)
            )

            salvar_dados(df)

            st.success(
                "Cliente excluído com sucesso!"
            )

            st.rerun()


# === RODAPÉ ===

st.html(
    """
    <div class="footer">
        TechClientes PRO<br>
        Gestão inteligente de clientes
    </div>
    """
)
