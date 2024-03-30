
from gTTS immport gTTS
from playsound import  playsound
audio="speech.mp3"
language='en'
sp=gTTS(text="plese suscribe the python life youtube channel",lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("=====audio is playing=====")
  


  