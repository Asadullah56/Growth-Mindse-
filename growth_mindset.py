import streamlit as st

# Set page configuration (only once, at the top)
st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐")

st.title("Growth Mindset Challenge: Web App with Streamlit 🚀")

st.header("Welcome to Your AI Growth Journey! 🚀")
st.write("Embark on a path of innovation, learning, and limitless possibilities. Together, let's explore the power of AI and shape the future!")

# Quote section
st.header("🌱 Today’s Growth Mindset Quote 🌱")
st.write("💡 Success starts with a mindset—keep learning, keep growing, and never stop evolving! 🚀🔥")

# Challenge section
st.header("🎯 What’s Your Challenge Today? 🎯")
user_input = st.text_input("Describe a Challenge:")

if user_input:
    st.success(f"🎯 You are facing: {user_input}. Keep pushing forward toward your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.header("📝 Reflection on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")

# Achievements section
st.header("🎉 Celebrate Your Wins! 🎉")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🌟 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share now.")

# Footer
st.write("--------------------")
st.write("💪 Every expert was once a beginner. Keep learning, keep pushing, and success will follow! 🚀✨")
st.write("©️ Created by Asadullah ✨")
