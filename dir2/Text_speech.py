from gtts import gTTS
import os
file=open("sample.txt","r")
text = file.read().replace("\n"," ")
language="en"
output = gTTS(text=text,lang=language,slow=False)
output.save("result.mp3")
os.system("result.mp3")

