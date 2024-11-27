import streamlit as st
from cryptography.fernet import Fernet
#função para gerar uma chave criptográfica
def gerar_chave():
    chave =Fernet.generate_key()
    with open("chave.key","wb") as chave_arquivo:
        chave_arquivo.write(chave)
    return chave
#carrear a chave do arquivo
def carregar_chave():
    return open("chave.key","rb").read()
#Função para criptografar uma mensagem
def criptografar_mensagem(mensagem,chave):
    fernet = Fernet(chave)
    mensagem_criptografada= fernet.encrypt(mensagem.encode())
    return mensagem_criptografada
#Função para descriptografar uma mensagem
def descriptografar_mensagem(mensagem_criptografada, chave):
    fernet = Fernet(chave)
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
    return mensagem_descriptografada
st.title("Dados do funcionário")
fun = st.text_input("Digite o nome do funcionário")
setor =st.text_input("Digite o setor")
salario =st.text_input("Digite seu salário")
if st.button("Confirmar funcionário"):
    chave1 = gerar_chave()
    chave2 = gerar_chave()
    chave3 = gerar_chave()
    mensagem_criptografada1 = criptografar_mensagem(fun,chave1)
    mensagem_criptografada2 = criptografar_mensagem(setor,chave2)
    mensagem_criptografada3 = criptografar_mensagem(salario,chave3)
    mensagem_original1 = descriptografar_mensagem(mensagem_criptografada1,chave1)
    mensagem_original2 = descriptografar_mensagem(mensagem_criptografada2,chave2)
    mensagem_original3 = descriptografar_mensagem(mensagem_criptografada3,chave3)
    st.write(mensagem_criptografada1)
    st.write(mensagem_criptografada2)
    st.write(mensagem_criptografada3)
    st.write(mensagem_original1)
    st.write(mensagem_original2)
    st.write(mensagem_original3)