import streamlit as st
import requests
import speech_recognition as sr
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
st.set_page_config(page_title="Hospital RAG Assistant", layout="centered")

st.title("🏥 Hospital AI Assistant")
st.write("Ask questions from your hospital document")

API_URL = "http://127.0.0.1:8000"

# Upload Section
st.header("📤 Upload Document")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    
    with st.spinner("Uploading and processing..."):
        response = requests.post(f"{API_URL}/upload", files={"file": uploaded_file})

    if response.status_code == 200:
        st.success("✅ Document uploaded successfully!")
    else:
        st.error("❌ Upload failed")


# Query Section
if "question" not in st.session_state:
    st.session_state.question = ""
st.header("❓ Ask a Question")

st.session_state.question = st.text_input(
    "Enter your question:",
    value=st.session_state.question
)

if st.button("🎤 Speak"):
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎙 Listening...")
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            st.success(f"You said: {text}")
            st.session_state.question = text  # set question from voice
        except:
            st.error("Could not understand audio")
if st.button("Get Answer"):
    if st.session_state.question:
        with st.spinner("Thinking..."):
            response = requests.post(
                f"{API_URL}/query",
                json={"question": st.session_state.question}
            )

        if response.status_code == 200:
            data = response.json()

            # ✅ Store in memory
            st.session_state.chat_history.append({
                "question": st.session_state.question,
                "answer": data["answer"],
                "sources": data["sources"]
            })
        

            st.subheader("📄 Sources:")

            for src in data["sources"]:
                st.markdown(f"📁 **{src['filename']} | Page {src['page']}**")

                # Clean highlight (optional)
                keyword = st.session_state.question.split()[0].lower()

                content = src["content"]
                highlighted = content.replace(
                    keyword,
                f"<mark>{keyword}</mark>"
                )

                st.markdown(
                    f"""
                    <div style="background-color:#f5f5f5; padding:12px; border-radius:10px; margin-bottom:10px; color:black;">
                        {highlighted}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                
        else:
            st.error("Error getting response")
st.header("💬 Chat History")

for chat in reversed(st.session_state.chat_history):
    st.markdown(f"**🙋 Question:** {chat['question']}")
    st.markdown(f"**🤖 Answer:** {chat['answer']}")

    st.markdown("📄 Sources:")
    for src in chat["sources"]:
        st.markdown(f"- Page {src['page']} ({src.get('filename', '')})")

    st.markdown("---")