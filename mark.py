import streamlit as st
st.markdown("# Título principal")
st.markdown("## subtítulo")
st.markdown("texto **negrito** e *itálico*")
st.markdown("- Item 1\n- Item 2\n- Item 3\n- Item 4\n- Item 5")
st.markdown("texto ~~riscado~~")
st.markdown("[visite meu site](https://www.entra.com.br)")
st.markdown("""
            ```java
            import java.util.Scanner;
            public class main{
                public static void main(String[]args){
                    System.out.println("Hello world");
                    Scanner input = new Scanner(System.in);
                    Salario = input.nextInt();
                    System.out.println(Salario)
                }
            }
            """)
col1,col2=st.columns(2)
with col1:
    st.markdown("###Coluna 1")
    st.markdown("- Item A\n- Item B")
with col2:
    st.markdown("###Coluna 2")
    st.markdown("- Item C\n- Item D")

st.markdown('<h1 style="color:blue;">Título Azul</h1',unsafe_allow_html=True)