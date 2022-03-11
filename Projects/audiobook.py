import pyttsx3
import PyPDF2

book = open('Tutorial_EDIT.pdf', 'rb')

pdfreader = PyPDF2.PdfFileReader(book)

speaker = pyttsx3.init()
speaker.say("What the fuck!")
speaker.runAndWait()