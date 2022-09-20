import streamlit as st
import pandas as pd
from PIL import Image
col1,col2 = st.columns(2)

with col1:
    st.subheader('自己紹介')
    st.text('pythonにかんするテストです。\n'
            'よろしくお願いします。')
    code = '''
    pip install streamlit
    import streamlit as st
    '''
    st.code(code,language='python')
    with st.form(key='profile_form'):
        name = st.text_input('名前')
        address = st.text_input('住所')

        ege_category = st.radio(
            '年齢層',('子供(18歳未満)','大人(18歳以上)')
        )
        
        hobby = st.multiselect(
            '趣味',
            ('スポーツ','読書','プログラミング','アニメ・映画','釣り','料理')
        )

        submit_btn = st.form_submit_button('送信')
        cancen_btn = st.form_submit_button('キャンセル')
        print(f'submit_bun:{submit_btn}')
        print(f'cancen_btn:{cancen_btn}')
        if submit_btn:
            st.text(f'ようこそ{name}さん!{address}が住所ですね。')
            st.text(f'年齢層:{ege_category}')
            st.text(f'趣味:{",".join(hobby)}')
with col2:
    df = pd.read_csv('./data/東日本営業部.csv',encoding="utf-8")
    st.dataframe(df)
