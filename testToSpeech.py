from gtts import gTTS
import base64
from datetime import datetime

def text2Speech(data):
    my_text = data
    tts = gTTS(text=my_text,lang='en',slow=False)

    filename = f"convertedfile_{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.mp3"
    
    tts.save(filename)
    with open(filename,'rb') as file:
        mystring = base64.b64encode(file.read())
    return mystring

