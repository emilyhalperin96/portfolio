import streamlit as st 

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

