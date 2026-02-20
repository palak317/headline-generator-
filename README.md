# ✍️ Catchy Headline Generator
**An AI-powered utility to instantly transform topics into 10 click-worthy, high-CTR titles.**

## 📌 Project Overview
Crafting the perfect headline is often the hardest part of content creation. This tool leverages the **Gemini 3 Flash** model to generate engaging titles for YouTube videos and blogs, ensuring your content stands out and drives engagement.

### 🚀 Key Features
- **AI-Powered Generation:** Leverages deep learning to understand topic context and generate unique headlines.
- **Multi-Style Output:** Automatically generates titles in several high-performing styles:
  - **Listicle:** (e.g., "10 Secrets to...")
  - **How-to:** (e.g., "How to Master...")
  - **Mystery/Curiosity:** (e.g., "Why I Stopped...")
  - **Controversial:** (e.g., "The Truth About...").
- **SEO Optimized:** All generated titles are restricted to under 70 characters for maximum visibility on search engines and social platforms.

---

## 🛠️ Tech Stack
- **Web Interface:** [Streamlit](https://streamlit.io/)
- **AI Intelligence:** [Google Gemini API](https://aistudio.google.com/) (Model: `gemini-3-flash-preview`)
- **Language:** Python 3.10+

---

## 🏗️ How it Works
1. **Input Topic:** Enter any subject (e.g., "Stock Market Analysis" or "Python for Beginners").
2. **AI Processing:** The Gemini API analyzes trending headline formulas and viral hooks.
3. **Instant Output:** 10 curated headlines are displayed, ready to be copied and used.

---

## 🏃 Installation & Setup

### 1. Clone & Environment
```bash
git clone [https://github.com/palak317/headline-generator.git](https://github.com/palak317/headline-generator.git)
cd headline-generator
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
