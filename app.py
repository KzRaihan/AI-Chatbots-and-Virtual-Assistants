### ============================================
#            NLP MEGA PROJECT APP
# ============================================

# === Import necessary libraries ===
import google.generativeai as genai
from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader


# === Load environment variables ===
load_dotenv()


# ============================================
#               Base Model Class
# ============================================
class NLPModel:
    def get_model(self):
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY_N"))
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        except Exception as e:
            st.error(f"Error configuring model: {e}")
            return None


# ============================================
#          Streamlit Page Configuration
# ============================================
st.set_page_config(
    page_title="NLP Project UI",
    page_icon="🤖",
    layout="wide"
)


# ============================================
#                Main Function
# ============================================
def main():

    # ---------------- Welcome Section ----------------
    st.title("🤖 Welcome to NLP Application")
    st.markdown("### Your All-in-One AI Powered NLP Assistant 🚀")
    st.markdown("---")

    # --------------- Initialize Session State ----------------
    if 'database' not in st.session_state:
        st.session_state.database = {}

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

    # --------------- Sidebar ----------------
    with st.sidebar:
        st.header("🔐 User Authentication")

        if not st.session_state.logged_in:
            option = st.radio("Choose Option", ["Login", "Register"])
        else:
            user_name = st.session_state.database[st.session_state.current_user]['name']
            st.success(f"Welcome, {user_name} 👋")
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.current_user = None
                st.rerun()

    # ============================================
    #        If User NOT Logged In
    # ============================================
    if not st.session_state.logged_in:

        if option == "Register":
            st.subheader("📝 Create New Account")

            with st.form("register_form"):
                name = st.text_input("Name")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Register")

                if submit:
                    if email in st.session_state.database:
                        st.error("Email already exists!")
                    elif name and email and password:
                        st.session_state.database[email] = {
                            "name": name,
                            "password": password
                        }
                        st.success("Registration successful! Please login.")
                    else:
                        st.warning("Please fill in all fields.")

        elif option == "Login":
            st.subheader("🔑 Login to Your Account")

            with st.form("login_form"):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")

                if submit:
                    if email in st.session_state.database:
                        if st.session_state.database[email]['password'] == password:
                            st.session_state.logged_in = True
                            st.session_state.current_user = email
                            st.success("Login Successful!")
                            st.rerun()
                        else:
                            st.error("Incorrect Password")
                    else:
                        st.error("Email not found. Please register first.")

    # ============================================
    #           If User Logged In
    # ============================================
    else:

        st.subheader("🧠 NLP app Features")

        feature = st.selectbox(
            "Select a Service",
            [
                "Sentiment Analysis",
                "Language Translation",
                "Language Detection",
                "Text Summarization",
                "PDF Upload & Summarize",
                "Study Assistant"
            ]
        )

        # Initialize Model
        nlp = NLPModel()
        model = nlp.get_model()

        # ---------------- Sentiment Analysis ----------------
        if feature == "Sentiment Analysis":
            st.info("Analyze the sentiment of a sentence.")
            user_text = st.text_area("Enter text")

            if st.button("Analyze Sentiment"):
                if user_text:
                    with st.spinner("Analyzing..."):
                        response = model.generate_content(
                            f"Give me the sentiment of this sentence: {user_text}"
                        )
                        st.write("### Result:")
                        st.write(response.text)
                else:
                    st.warning("Please enter some text.")

        # ---------------- Language Translation ----------------
        elif feature == "Language Translation":
            st.info("Translate text to Hindi.")
            user_text = st.text_area("Enter text")

            if st.button("Translate"):
                if user_text:
                    with st.spinner("Translating..."):
                        response = model.generate_content(
                            f"Translate this sentence into Hindi: {user_text}"
                        )
                        st.write("### Result:")
                        st.write(response.text)
                else:
                    st.warning("Please enter some text.")

        # ---------------- Language Detection ----------------
        elif feature == "Language Detection":
            st.info("Detect the language of text.")
            user_text = st.text_area("Enter text")

            if st.button("Detect Language"):
                if user_text:
                    with st.spinner("Detecting..."):
                        response = model.generate_content(
                            f"Detect the language of this sentence: {user_text}"
                        )
                        st.write("### Result:")
                        st.write(response.text)
                else:
                    st.warning("Please enter some text.")

        # ---------------- Text Summarization ----------------
        elif feature == "Text Summarization":
            st.info("Summarize long text.")
            user_text = st.text_area("Enter text")

            if st.button("Summarize"):
                if user_text:
                    with st.spinner("Summarizing..."):
                        response = model.generate_content(
                            f"Summarize the following text in 3-5 clear sentences:\n{user_text}"
                        )
                        st.write("### Summary:")
                        st.write(response.text)
                else:
                    st.warning("Please enter some text.")

        # ---------------- PDF Summarization ----------------
        elif feature == "PDF Upload & Summarize":
            st.info("Upload PDF and generate summary.")
            uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

            if uploaded_file is not None:
                if st.button("Summarize PDF"):
                    with st.spinner("Processing PDF..."):
                        try:
                            pdf_reader = PdfReader(uploaded_file)
                            extracted_text = ""

                            for page in pdf_reader.pages:
                                extracted_text += page.extract_text()

                            if extracted_text.strip():
                                response = model.generate_content(
                                    f"Summarize this document clearly:\n{extracted_text[:8000]}"
                                )
                                st.write("### PDF Summary:")
                                st.write(response.text)
                            else:
                                st.warning("Could not extract text.")
                        except Exception as e:
                            st.error(f"Error: {e}")

        # ---------------- Study Assistant ----------------
        elif feature == "Study Assistant":
            st.info("AI Study Assistant")

            study_option = st.selectbox(
                "Choose Mode",
                [
                    "Explain Concept",
                    "Summarize Topic",
                    "Generate Practice Questions",
                    "Create Study Plan"
                ]
            )

            user_text = st.text_area("Enter topic")

            if st.button("Get Help"):
                if user_text:
                    with st.spinner("Generating..."):

                        if study_option == "Explain Concept":
                            prompt = f"Explain this concept clearly: {user_text}"

                        elif study_option == "Summarize Topic":
                            prompt = f"Summarize this topic into key points: {user_text}"

                        elif study_option == "Generate Practice Questions":
                            prompt = f"Generate 5 practice questions with answers for: {user_text}"

                        elif study_option == "Create Study Plan":
                            prompt = f"Create a 7-day study plan for: {user_text}"

                        response = model.generate_content(prompt)

                        st.write("### Response:")
                        st.write(response.text)
                else:
                    st.warning("Please enter a topic.")


# ============================================
#                 Run App
# ============================================
if __name__ == "__main__":
    main()