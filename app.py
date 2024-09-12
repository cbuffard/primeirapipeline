import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError  # para error de insercao nos campos (contrato)
from contrato import Vendas  # importando a classe Vendas de contratos.py (contrato)
from database import salvar_no_postgres
import contrato  # biblioteca para contrato.py

def main():
    st.title('Sistema de CRM e Vendas da Zapflow - Frontend Simples')
    email = st.text_input('Campo de texto para inserção do email Vendedor')
    data = st.date_input('Data da compra', datetime.now())
    hora = st.time_input('Hora da Compra', value=time(9, 0))  # Valor padrão: 9:00
    valor = st.number_input('Valor de venda', min_value=0.0, format='%.2f')
    quantidade = st.number_input('Quantidade de produtos', min_value=1, step=1)
    produto = st.selectbox('Produto', options=['ZapFlow com Gemini', 'ZapFlow com Chatgpt', 'ZapFlow com Llama3.0'])

    if st.button('Salvar'):
        try:
            data_hora = datetime.combine(data, hora)
            
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            
            st.write(venda)
            salvar_no_postgres(venda)  # Passing the instance instead of the class #pego do database.py
        except ValidationError as e:
            st.error(f'Deu erro: {e}')

if __name__ == '__main__':
    main()
