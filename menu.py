import streamlit as st
st.set_page_config(
    page_title = "Senac Ceará",
    page_icon = "👻",
    layout="wide"
)
st.title("Senac Ceará - Laboratório de Tecnologia")
col1,col2,col3= st.columns([1,1,1])
with col1:
    botao_inicio = st.button("Inicio")
with col2:
    botao_sobre_nos = st.button("Sobre Nós")
with col3:
    botao_contato = st.button("Contato")

if botao_inicio:
    st.title("Iniciar")
    st.image("https://registrodemarca.arenamarcas.com.br/wp-content/uploads/2020/05/Hist%C3%B3ria-do-Cear%C3%A1-Sporting-Club.jpg",width=500)
    st.write("Bem vindos a nossa página do Senac, conheça melhor sobre nosso trabalho ")
    Slider_value = st.slider("Quanto você está mal humorado hoje?",0,100,100)
    st.header("Cursos disponíveis")
    st.write("Programador de Sistemas, Formação em Python, Excel básico e avançado, Informática Básica,excel expert, ferramentas de marketing digital, Power BI")
    box = st.selectbox("escolha seu curso",["Programador de sistemas","formação em python","Excel básico e avançado","informática básica","excel expert","Ferramentas de marketing digital, Power BI"])
if botao_sobre_nos:
    st.write("Empresa fundada em 2024, estamos a 10 minutos no mercado")
else:
    st.write("Entre em contato conosco")
    st.write("Telefone:8598587-1995")
    st.write("Email:denissilva@ce.senac.br")
    st.text("texto")
    caixa_de_texto=st.text_area("Digite seu texto")
    st.write(caixa_de_texto)
    numero = st.number_input("digite um número",min_value=0,max_value=500,value=10,format="%d")
    fruta = st.radio("Diga uma fruta",options=["Morango","Laranja","Abacaxi","Maçã","Murici"])
    st.multiselect(label="escolha 2 times",options=["Ceará","Fortaleza","Flamengo","São Paulo","palmeiras","Santos","Corinthians"],default=["Ceará","São Paulo"])
    texto="A aula terminou!"
    st.download_button(label="clique para baixar",data=texto,file_name="texto.txt",mime="text/plain")
