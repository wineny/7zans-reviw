# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_model = ChatOpenAI()

st.title('일곱잔 리뷰 답글 프로젝트')
st.subheader('답글을 자동으로 생성해봐요 :blue[for 사장님] :sunglasses:')

content = st.text_input('리뷰를 입력해주세요.')

if st.button('답글 작성 요청하기'):
    with st.spinner('답글 작성 중...'):
        result = chat_model.predict(content + 
                                "에 대한 답글을 써줘. 너는 '일곱잔'이라고 하는 와인바의 사장이야. 사장의 입장에서, 고객이 작성한 리뷰를 보고 리뷰를 변형하고, 이모지를 써서 답글을 작성해줘.")
    st.write(result)



# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("내가 좋아하는 동물은")
# print(result)
