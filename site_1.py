import streamlit as st
import time
def main():
    st.set_page_config(
        page_title="site do Denis",
        page_icon ="😎",
        layout="wide"
    ) # icone da página e rótulo
    st.title("Título principal da página") #titulo principal
    #texto na página
    st.write("Estamos aprendendo streamlit em python e já tivemos 2 bugs por conta da versão do python")
    st.header("Esportes") #Título no tópico
    st.subheader("Jogos de ontem") #subtópico
    st.header("Input de texto")
    var = st.text_input("Digite seu texto aqui") #caixa de entrada
    if var:
        st.write(var)
    st.header("caixa de seleção")
    box= st.selectbox("sexo",["Masculino","Feminino"]) #caixa de seleção
    if box=="Masculino":
        st.write("Boy")
    elif box=="Feminino":
        st.write("Girl")
    st.image("C:/Users/Aluno/Pictures/animal.jpg",width=500) #Imagem
    st.header("Slider")
    valor_slider = st.slider("escolha um volume",0,100,50)
    st.write("Volume atual: ",valor_slider)
    st.header("checkbox")
    checkbox_estado = st.checkbox("marque para ativar")
    if checkbox_estado==True:
        st.write("Excelente escolha")
    st.header("Botão")
    if st.button("clique aqui"):
        st.write("você clicou no botão")
    st.header("Aguarde")
    with st.spinner("aguardando..."):
        time.sleep(3)
    st.success("carregado com sucesso!")
    #Texto de aviso
    st.warning("você está vacilando muito")
    #texto de perigo
    st.error("A vida não é uma caixinha de surpresas, é um container de decepções")
    #enviar arquivo
    enviar_arquivo = st.file_uploader("Escolha um arquivo",type=["pdf","mp4"])
    #salvar em uma pasta do computador
    if enviar_arquivo is not None:
        with open(f'./{enviar_arquivo.name}','wb') as f:
            f.write(enviar_arquivo.getbuffer())
        st.success("arquivo enviado com sucesso!")
    #trabalhar com data
    data= st.date_input("escolha uma data")
    st.write(data)
    hora = st.time_input("escolha uma hora")
    st.write("hora escolhida: ",hora)
    cor = st.color_picker("escolha uma cor")
main()