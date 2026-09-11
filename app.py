import streamlit as st
from translation_model import translate_text
from gtts import gTTS
import io


st.markdown("""
    <style>
 
    .stApp {
        background-color: #F4FBFD;
    }
   
    h1 {
        color: #2980B9;
        text-align: center;
    }
  
    .stButton>button {
        background-color: #5DADE2;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3498DB;
        color: white;
    }
   
    #root > div:nth-child(1) > div > div > div > div > section > div > div:nth-child(2) > div > div:nth-child(3) > div > div > button {
        background-color: #AED6F1;
        color: #154360;
        border-radius: 15px;
        border: none;
    }
   
    .stTextArea>div>div>textarea {
        border-radius: 15px;
        border: 2px solid #AED6F1;
        background-color: #FDFEFE;
    }
   
    .stSelectbox>div>div {
        border-radius: 15px;
        border: 2px solid #AED6F1;
    }
    </style>
    """, unsafe_allow_html=True)


st.set_page_config(page_title="Text-trans", page_icon="🔄", layout="centered")
st.title("Translator App using AI")


languages = {
    "Arabic": {"nllb": "arb_Arab", "gtts": "ar"},
    "English": {"nllb": "eng_Latn", "gtts": "en"},
    "French": {"nllb": "fra_Latn", "gtts": "fr"},
    "Spanish": {"nllb": "spa_Latn", "gtts": "es"},
    "German": {"nllb": "deu_Latn", "gtts": "de"}
}


col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("Source Language :", list(languages.keys()))

with col2:
    target_lang_name = st.selectbox("Target language :", list(languages.keys()))

text_input = st.text_area("Enter the text you want to translate here :", height=150)


if 'translated_text' not in st.session_state:
    st.session_state.translated_text = ""


if st.button("Translate", type="primary"):
    if text_input.strip():
        with st.spinner("Translating..."):
            src_code = languages[source_lang_name]["nllb"]
            tgt_code = languages[target_lang_name]["nllb"]
            st.session_state.translated_text = translate_text(text_input, src_code, tgt_code)
    else:
        st.warning("Please enter text to translate first")


if st.session_state.translated_text:
    st.subheader("Translated Text:")
    st.code(st.session_state.translated_text, language="")
    
    if st.button("🔊 Listen to Pronunciation"):
        with st.spinner("Generating audio..."):
            try:
                gtts_lang = languages[target_lang_name]["gtts"]
                tts = gTTS(st.session_state.translated_text, lang=gtts_lang)
                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_buffer.seek(0)
                st.audio(audio_buffer, format="audio/mp3")
            except Exception as e:
                st.error(f"Audio error: {e}")