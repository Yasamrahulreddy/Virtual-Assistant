import webbrowser
import speech_recognition as sr
import os
import subprocess
import pyttsx3
import datetime
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print()
print("!!!!!.......Welcome to my Virtual World........!!!")

pyttsx3.speak("Welcome to Virtual World ")
print()
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    pyttsx3.speak("Good Morning!")

elif hour>=12 and hour<17:
    pyttsx3.speak("Good Afternoon!")

else:
    pyttsx3.speak("Good Evening!")
pyttsx3.speak("Hello Rahul..I am SARA, What are you looking for?")

print("What are you looking for?... ", end='')
#ch=input()

r = sr.Recognizer() 
try:			
  with sr.Microphone() as source: #mic connection
      print("\n")
      print('please start saying')
      pyttsx3.speak("please start saying ,we are recognizing")
      print("\n")
      audio = r.listen(source)	#storage of voice and listen
      print('we got it...')
      pyttsx3.speak("we got it....")
except sr.UnknownValueError:
      print("No clue what you said, listening again... \n")
      
ch = r.recognize_google(audio)
print(ch)


if  ("launch" in ch) and ( "Chrome" in ch):
  pyttsx3.speak("launching chrome for you")
  os.system("chrome")
  pyttsx3.speak("closing chrome")

elif  ("launch in ch ") and ("notepad" in ch):
  pyttsx3.speak("launching notepad for you ")
  os.system("notepad")
  pyttsx3.speak("closing notepad")

elif("launch in ch") and  ("paint" in ch) or ("paint" in ch):
  pyttsx3.speak("launching paint for you")
  os.system("mspaint")
  pyttsx3.speak("closing paint")

elif "recorder" in ch:
	pyttsx3.speak("launching recorder")
	os.system('psr')
	pyttsx3.speak("closing recorder")

elif ('open' in ch) and ('stack' in ch) and ('overflow' in ch):
  pyttsx3.speak("opening stack overflow")
  webbrowser.open("https://stackoverflow.com/") 
  pyttsx3.speak("closing stack overflow")

elif ("open" in ch) and ("YouTube") in ch:
  pyttsx3.speak("opening youtube for you")
  webbrowser.open("https://www.youtube.com/?gl=IN&tab=r11")
  pyttsx3.speak("closing youtube")

elif ("open" in ch) and ("Windows Media Player" in ch):
  pyttsx3.speak("launching windows media player for you")
  os.system("wmplayer")
  pyttsx3.speak("closing windows media player")

elif ("sticky notes" in ch):
  pyttsx3.speak("opening sticky notes for you")
  os.system("StikyNot")
  pyttsx3.speak("launching sticky notes for you")

elif ("snipper" in ch) :
	pyttsx3.speak("launching SnippingTool")
	os.system('SnippingTool')
	pyttsx3.speak("closing SnippingTool")

elif ("my github account " in ch):
  webbrowser.open('https://github.com/Yasamrahulreddy')

elif("vlc" in ch) and ("mediaplayer" in ch ):
	pyttsx3.speak("launching vlc media player")
	os.system('vlc')
	pyttsx3.speak("closing vlc media player")

elif (("launch" in ch) or("open" in ch ))and ("reader" in ch) :
	pyttsx3.speak("opening adobe reader")
	subprocess.call(['C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe'])
	pyttsx3.speak("closing adobe reader")

elif (("launch" in ch) or  ("open" in ch )) and ("calculator" in ch) or ("calculator" in ch) :
	pyttsx3.speak("opening calculator")
	subprocess.Popen('C:\\Windows\\System32\\calc.exe')

elif  ("exit" in ch)  or ("quit" in ch) or ("close" in ch):
	pyttsx3.speak("Byeee !Thank You Have a nice day ")
	print("Byeee !Thank You Have a nice day ")
	

elif("open" in ch) and ("remote desktop" in ch):
	pyttsx3.speak("launching remote desktop")
	os.system('mstsc')
	pyttsx3.speak("closing remote desktop")

elif("open" in ch) and ("system" in ch) and("information" in ch) or ("info" in ch):
	pyttsx3.speak("launching system information")
	os.system('msinfo32')
	pyttsx3.speak("closing system information")

elif("open" in ch) and ("task manager" in ch):
	pyttsx3.speak("launching task manager")
	os.system('Taskmgr')
	pyttsx3.speak("closing task manager")

else:
  print("not understand,Please Try once again")
  pyttsx3.speak("not understand , Please Try once again")
