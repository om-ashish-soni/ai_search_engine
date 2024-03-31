from gtts import gTTS
import streamlit as st
import base64
import io


# filename=generate_unique_audio_filename()
# print("filename",filename)
playback_speed=1.25

def speak(text,language='en'):
    try:
        # text to speak code
        tts = gTTS(text, lang=language, slow=False)
        
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)  # Move the pointer to the start of the BytesIO object
        b64 = base64.b64encode(mp3_fp.read()).decode('utf-8')

        # displaying audio in html
        md = f"""
                <audio controls autoplay="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <script>
                    var audio = document.querySelector('audio');
                    audio.playbackRate = {playback_speed};
                </script>
                """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


    except Exception as e:
        st.error(f"An error occurred: {e}")
