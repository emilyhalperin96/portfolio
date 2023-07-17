import streamlit as st 
import pandas 

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Emily Halperin')
    content = """
        Highly motivated and adaptable Software Engineer with a background in product management and marketing. I bring a strong aptitude for quick learning and a curious mindset. With hands-on experience in back end development, my problem-solving skills and agile/collaborative mindset will make me a valuable asset.
    """
    st.info(content)

content2 = '''

Languages: Python, React, Flask, SQL, Javascript, React Native

Technologies: Github, AWS, Docker, Branch.io, Braze, Jira, Looker, Salesforce, Postman

Education: University of Michigan, Flatiron School

'''
st.write(content2)

content3 = '''

Projects

'''
st.header(content3)


col3, col4 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
