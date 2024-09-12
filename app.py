import streamlit as st
from datetime import datetime, time
import contrato  # biblioteca para contrato.py


def main():
    st.title('Sistema de CRM e Vendas da Zapflow - Frontend Simples')
    email = st.text_input('Campo de texto para insercao do email Vendedor')
    data = st.date_input('Data da compra', datetime.now())
    hora = st.time_input('Hora da Compra', value=time(9,0)) # Valor padrao: 9:00 
    valor = st.number_input('Valor de venda', min_value=0.0, format='%.2f')
    quantidade = st.number_input('Quantidade de produtos', min_value=1, step=1)
    produto = st.selectbox('Produto', options=['ZapFlow com Gemini', 'ZapFlow com Chatgpt', 'ZapFlow com Llama3.0'])

    if st.button('Salvar'):

        data_hora = datetime.combine(data, hora)
        st.write('**Dados de Venda:**')
        st.write(f'Email do Vendedor: {email}')
        st.write(f'Data e Hora da Compra:{data_hora}')
        st.write(f'Valor da Venda: R$ {valor:.2f}')
        st.write(f'Quantidade de Produtos: {quantidade}')
        st.write(f'Produto: {produto}')

if __name__=='__main__':
    main()