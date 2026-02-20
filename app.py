import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Headline Master", page_icon="✍️")
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

st.title("✍️ Catchy Headline Generator")
st.write("Transform any topic into 10 click-worthy YouTube or Blog titles.")

# --- 2. INPUT ---
topic = st.text_input("Enter your topic:", placeholder="e.g., Python Coding, Stock Market, Fitness")

def generate_headlines(user_topic):
    model = genai.GenerativeModel('gemini-3-flash-preview')
    prompt = f"""
    Act as an expert YouTube strategist and copywriter. 
    Generate 10 catchy, click-worthy, and high-CTR headlines for the topic: '{user_topic}'.
    Mix different styles: 'How-to', 'Mystery/Curiosity', 'Listicle', and 'Controversial'.
    Ensure they are under 70 characters for SEO.
    """
    response = model.generate_content(prompt)
    return response.text

# --- 3. UI LOGIC ---
if st.button("Generate Headlines"):
    if topic:
        with st.spinner(f"Analyzing trends for '{topic}'..."):
            headlines = generate_headlines(topic)
            st.subheader(f"🔥 Top 10 Headlines for {topic.title()}")
            st.markdown(headlines)
            st.balloons()
    else:
        st.warning("Please enter a topic first!")