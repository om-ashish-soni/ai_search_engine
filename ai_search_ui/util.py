# import os
# import tempfile
# import datetime
# import random
# import string
# import torch
import streamlit as st
import time
import textwrap
# from translator import translate

# def speaking_icon(speaking_thread):
#     while speaking_thread.is_alive():  # This will run indefinitely until stopped
#         st.write("Speaking...")
#         time.sleep(0.5)

def write_answer(Answer,max_line_length,language='en'):
    # spliting into paragraphs
    paragraphs=Answer.split('\n\n')
    TranslatedAnswer=''

    # writing each paragraph and translating if it is other than 'en'
    for paragraph in paragraphs:
        translated_paragraph=paragraph

        if language != 'en':
            translated_paragraph=translate(paragraph,'en',language)

        TranslatedAnswer+=translated_paragraph+'\n\n'

        # text wrap for screen
        wrapped_text = textwrap.fill(translated_paragraph, width=max_line_length)

        # streaming the text
        placeholder = st.empty()

        prev_text=''
        for char in wrapped_text:
            prev_text=prev_text+char
            placeholder.text(prev_text)
            time.sleep(0.001)  # Adjust the sleep duration as needed
        st.write('\n\n')
  

# Define a function to dynamically set the device
# def get_device():
#     return torch.device("cuda" if torch.cuda.is_available() else "cpu")

# def create_vivechan_ai_folder():
#     # Get the system's temporary directory path
#     temp_dir = tempfile.gettempdir()

#     # Create the full path for "vivechan-ai" folder
#     vivechan_ai_path = os.path.join(temp_dir, "vivechan-ai")

#     # Check if the folder already exists
#     if not os.path.exists(vivechan_ai_path):
#         # If it doesn't exist, create the folder
#         os.makedirs(vivechan_ai_path)

#     return vivechan_ai_path

# def generate_unique_audio_filename():
#     vivechan_ai_path=create_vivechan_ai_folder()

#     # Generate a random string of letters and digits
#     random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

#     # Get the current date and time
#     current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

#     # Combine the random string and current time to create a unique filename
#     unique_filename = f"audio_{current_time}_{random_string}.mp3"

#     audio_file_path = os.path.join(vivechan_ai_path, unique_filename)

#     return audio_file_path


# def delete_temp_audio(audio_file_path):
#     # Delete the temporary audio file
#     if os.path.exists(audio_file_path):
#         os.remove(audio_file_path)
#         print("Deleted temporary audio file:", audio_file_path)
#     else:
#         print("File does not exist:", audio_file_path)

def display_footer():
    st.markdown(
        """
        <style>
            
            .footer {
                bottom:0
                background-color: #f8f9fa;
                padding: 20px 0;
                color: #495057;
                text-align: center;
                border-top: 1px solid #dee2e6;
            }
            .footer a {
                color: #007bff;
                text-decoration: none;
            }
            .footer a:hover {
                color: #0056b3;
                text-decoration: underline;
            }
        </style>
        <div class="content">
            <!-- Your main app content goes here -->
        </div>
        <div class="footer">
            <p class="mb-0">Made with 🙏 designed by Om Ashishkumar Soni</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
def generate_context(search_results):
    print("going to generate context")
    Context=""
    
    for link_url,data in search_results.items():
        Context+="From "+link_url+" => "+data

    return Context
