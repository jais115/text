from django.shortcuts import render


from django.shortcuts import render
from googletrans import Translator
from gtts import gTTS
#from playsound import playsound
#import speech_recognition as sr 
#import pyttsx3
from googletrans import Translator
from gtts import gTTS
import os
import time
import json

#from deep_translator import GoogleTranslator
# import sys
# print(sys.getrecursionlimit())

# Create your views here.

def translator(request):

    
    return render(request, 'translator.html')



def translated(request):
    text = request.GET.get('text')
    lang = request.GET.get('lang')
    print('text :',text, 'lang :',lang)
    

    translator =Translator()

    dt = translator.detect(text)
    dt2 = dt.lang
    translated = translator.translate(text, lang)
    tr = translated.text
    #speak = gTTS(text=tr, lang=lang, slow=False)

    return render(request, 'translated.html', {'translated':tr, 'u_lang':dt2, 't_lang':lang})


# Create your views here.
