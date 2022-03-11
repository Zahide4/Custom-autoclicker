import speech_recognition as sr
import pyaudio 
import googletrans

r1 = sr.Recognizer()


def audioListener():
	with sr.Microphone() as source:
		print("Speak Anything: ")
		audio = r1.listen(source)
		try:
			audioListener.text = r.recognize_google(audio)
			print("You said: ", audioListener.text)
		except:
			print("Try again: ")

def Translator1():
	translatedText = translator.translate(audioListener.text, scr = "en", dest = "es")
	print("Translated to spanish: ", translatedText)
audioListener()
Translator1()
