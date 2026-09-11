# 🌍 AI Translator App

An AI-powered web application for translating text between multiple languages using pre-trained AI models. The application also includes a Text-to-Speech feature that allows users to listen to the translated text.

## ✨ Features

- **Simple and User-Friendly Interface:** Built with Streamlit for a clean and modern user experience.
- **AI-Powered Translation:** Uses the `facebook/nllb-200-distilled-600M` model from Hugging Face.
- **Multiple Languages:** Supports Arabic, English, French, Spanish, and German.
- **Text-to-Speech:** Converts translated text into speech using gTTS.
- **Listen to Pronunciation:** Users can listen to the pronunciation of the translated text.
- **Copy Translation:** Quickly copy the translated text.
- **Modern UI:** Customized with a clean Baby Blue theme.

## 🛠️ Tech Stack

- **Python 3**
- **Streamlit** – Web application framework
- **Transformers** – AI model integration
- **PyTorch** – Deep Learning framework
- **Hugging Face** – Pre-trained translation model
- **gTTS** – Google Text-to-Speech
- **SentencePiece** – Tokenization support

## 🤖 AI Model

This project uses:

**Model:** `facebook/nllb-200-distilled-600M`

The NLLB (No Language Left Behind) model is a multilingual translation model developed by Meta AI and available through Hugging Face.

The model supports translation across a large number of languages and provides high-quality multilingual translation.

## 📂 Project Structure

```text
📁 Translation-App/
│
├── 📄 app.py
├── 📄 translation_model.py
├── 📄 requirements.txt
├── 📄 README.md
│
└── 📁 .streamlit/
    └── 📄 config.toml