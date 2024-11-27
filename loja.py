import streamlit as st

produtos=[{"nome": "Tênis Adidas runfalcon 5", "Preço":399.00,"Imagem":"https://static.ativaesportes.com.br/public/ativaesportes/imagens/produtos/tenis-adidas-runfalcon-5-feminino-jj7816-66e1ba8061a36.jpg"},
         {"nome": "Tênis vans old skool","Preço":329.00,"Imagem":"https://static.rockcity.com.br/public/rockcity/imagens/produtos/tenis-vans-old-skool-preto-branco-64b8285d7de89.jpg"},
         {"nome":"Tênis Puma Shuffle BDP","Preço":680.00,"Imagem":"https://images.tcdn.com.br/img/img_prod/1030565/tenis_puma_shuffle_bdp_branco_verde_5897_1_96f1a2851068a31629f0b9f855b0e956.jpg"},{"nome":"Kichute esportivo","Preço":90.00,"Imagem":"https://diariodonordeste.verdesmares.com.br/image/contentid/policy:1.3293486:1666793634/Kichute-1.jfif?f=default&$p$f=c07a1b4"},{"nome":"New Balance V1","Preço":764.00,"Imagem":"https://m.media-amazon.com/images/I/41kaNt1ekgL._AC_.jpg"}]
def exibir_carrinho(carrinho):
    if len(carrinho)>0:
        st.header("Carrinho de Compras")
        total=0
        for produto_nome, dados in carrinho.items():
            st.write(f"{dados['produto']['nome']} - R$ {dados['produto']['Preço']:.2f} x {dados['quantidade']}")
            total+=dados['produto']['Preço']*dados['quantidade']
        st.write(f"Total: R$ {total:.2f}")
        return total
    else:
        st.write("O carrinho está vazio")
        return 0
def pagar(total):
    if total>0:
        box= st.selectbox("Forma de pagamento",["PIX","Dinheiro","Cartão"])
        if box=="PIX":
            st.write("PIX: denis.silvace@hotmail.com")
            st.write("Enviar o comprovante para: (85)9.8607-6060")
            st.success("Pagamento efetuado com sucesso!")
            return True
        if box=="Dinheiro":
            pago = st.number_input("Digite um valor",min_value=0,max_value=100000,value=0,format="%f")
            if pago>=total:
                troco = pago-total
                st.write("Seu troco é de: R$",troco)
                st.success("Pagamento realizado com sucesso")
            else:
                st.write("valor menor que o total")

            
            return True
        if box =="Cartão":
            st.write("Insira seus dados")
            numero=st.text_input("Digite o número do cartão")
            nome=st.text_input("Digite o nome do cartão")
            venc=st.text_input("Digite o mês e o ano do vencimento")
            codigo=st.text_input("digite o código de 3 dígitos")
            st.success("Pagamento realizado com sucesso")
            return True
    else:
        st.warning("Adicione itens ao carrinho!")
def loja():
    st.title("Sapataria Nova!")
    if "carrinho" not in st.session_state:
        st.session_state.carrinho={}
    st.write("Produtos disponíveis")
    for produto in produtos:
        col1,col2,col3=st.columns([1,3,1])
        with col1:
            st.image(produto["Imagem"],width=100)
        with col2:
            st.write(f"{produto['nome']}")
            st.write(f"Preço: R$ {produto['Preço']:.2f}")
        with col3:
            if st.button(f"Adicionar {produto['nome']} ao carrinho",key=produto['nome']):
                if produto['nome'] in st.session_state.carrinho:
                    st.session_state.carrinho[produto['nome']]['quantidade']+=1
                else:
                    st.session_state.carrinho[produto['nome']]={
                        'produto':produto,
                        'quantidade':1
                    }
                st.success("produto adicionado ao carrinho!")
    total= exibir_carrinho(st.session_state.carrinho)
    pagar(total)
loja()