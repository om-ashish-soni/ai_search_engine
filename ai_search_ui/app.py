# IMPORTING 
from util import generate_context,display_footer,write_answer
from LLM import infer
import streamlit as st
from dotenv import load_dotenv
from search import search_request
import os
import time
from trans import speak

load_dotenv()


# SOME STATIC VARIABLES
k=10
max_line_length = 80

# language_choices = {
#     'English': 'en',
#     'Hindi': 'hi',
#     'Gujarati': 'gu',
#     'Marathi': 'mr',
#     'Tamil': 'ta',
#     'Telugu': 'te',
#     'Kannada': 'kn',
#     'Bengali': 'bn',
# }

def display_sources_with_delay(search_results, delay_ms):
    st.markdown("### Sources of Information:")
    st.markdown("---")

    for source_index, search_link in enumerate(search_results, start=1):
        placeholder = st.empty()
        placeholder.markdown(f"{source_index}. [{search_link}]({search_link})")

        # Delay before displaying the next source
        time.sleep(delay_ms / 1000)  # Convert milliseconds to seconds

        # Clear the placeholder
        placeholder.empty()
        
# MAIN METHOD TO SET PAGE CONFIG
def main():
    
    st.set_page_config(
        page_title="Anusandhan AI",
        page_icon="✨",
    )
    
if __name__ == "__main__":
    main()



# UI
st.title("Anusandhan - AI Search Engine 🌟")
# st.subheader("AI for spritual matters")
st.markdown(
    """
    <style>
        .reportview-container {
            width: 90%;
        }
    </style>
    """,
    unsafe_allow_html=True
)
query = st.text_input("Search any query : ")

# SELECTING LANGUAGE
# language=language_choices[st.selectbox("Select Language:", list(language_choices.keys()))]
# print("language : ",language)

def ask(IsContinue=False):
    placeholder = st.empty()
    placeholder.image("searching.gif")

    search_results=search_request(query)

    Context=generate_context(search_results)

    Answer=infer(query,Context)

    placeholder.empty()

    st.markdown("### AI Powered Search Results :")
    st.markdown("---")

    write_answer(Answer,max_line_length)

    st.markdown("### Sources of Information:")
    st.markdown("---")
    source_index=0
    for search_link in search_results:
        if source_index>0:
            st.markdown(f"{source_index}. [{search_link}]({search_link})")
        source_index+=1
        time.sleep(0.4)
    pass
    speak(Answer)

if st.button('Search'):
    st.session_state['PreviousAnswer']=''
    st.session_state['Answer']=''
    st.session_state['ShouldContinue']=False
    ask()
    
display_footer()