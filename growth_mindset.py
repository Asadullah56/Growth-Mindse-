import streamlit as st

st.set_page_config(page_title = "growth mindset project", project_icon = "⭐")
st.title("Growth Mindset Challenge: Web App with Streamlit 🚀")

st.header("Welcome to Your AI Growth Journey! 🚀")
st.write("Embark on a path of innovation, learning, and limitless possibilities. Together, let's explore the power of AI and shape the future")


#quote section
st.header("🌱 Today’s Growth Mindset Quote 🌱")
st.write("💡Success starts with a mindset—keep learning, keep growing, and never stop evolving! 🚀🔥")

st.header("🎯 What’s Your Challenge Today? 🎯")
user_input = st.text_input("Describe a Challange ")

if user_input:
    st.success(f"🎯You are facing: {user_input}. Keep pushing forwar towards your goal!🚀")
else:
    st.warning("Tell us about your Challange to get Started ")

#reflexing
#
st.header("Reflection on Your learning")
reflection = st.text_area("Write your reflection here: ")
if reflection:
    st.success(f"Great Instlight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share yor difficlties ")

#acheivements
st.header("🎉 Celebrate Your Wins! 🎉")
acheivement = st.text_input("Share Something you'have recently accomplished: ")

if acheivement:
    st.success(f'🌟 Amzing! You acheived: {acheivement} ')
else:
    st.info(f'Big or Small ,Every Acheivement Counts! Share Now')

#Footer
st.write("--------------------")
st.write("💪 Every expert was once a beginner. Keep learning, keep pushing, and success will follow! 🚀✨")
st.write("©️ Create by Asadullah ✨")