import os
import playsound
import speech_recognition as sr
import psutil
import subprocess
import pyautogui as pg
from gtts import gTTS
from word2number import w2n

again = True


def speak(text11):
    a = gTTS(text=text11, lang='tl')
    file = "voice1.mp3"
    a.save(file)
    playsound.playsound(file)
    os.remove('voice1.mp3')

def input_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as s:
            print("Exception" + str(s))
    return said

while again:

    text = input_audio()
    if "nandiyan" in text:
        speak("nandito ako")

    elif "exit" in text:
        speak("BYE! out na ako")
        again = False

    elif "pangalan" in text:
        speak("pangalan ko ay Jinx")


    elif "compute" in text:
        speak("what operation?")
        #  true_again = True
        # while true_again:
        print('****')
        text1 = input_audio()
        if "add" in text1:
            speak("enter first number")
            print('***')
            listen = input_audio()
            if listen != '':
                first = w2n.word_to_num(listen)
                speak('enter second number')

                listen1 = input_audio()
                if first != 0:
                    second = w2n.word_to_num(listen1)
                    speak('calculating.')

                    answer = first + second

                    print(answer)
                    converted_ans = str(answer)
                    speak('Ang sagot ay ' + converted_ans)
        elif "minus" in text1:
            speak('enter first number')
            print('***')
            listen2 = input_audio()
            if listen2 != '':
                first1 = w2n.word_to_num(listen2)
                speak('enter second number')
                listen22 = input_audio()
                if first1 != 0:
                    second1 = w2n.word_to_num(listen22)
                    speak('calculating.')

                    answer1 = first1 - second1
                    print(answer1)
                    converted_ans1 = str(answer1)
                    speak('Ang sagot ay ' + converted_ans1)



    elif 'chrome' in text:
        speak('opening.')
        subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
        open_chrome = "chrome.exe" in (i.name() for i in psutil.process_iter())
        if open_chrome:
            text2 = input_audio()
            if 'facebook' in text2:
                pg.typewrite('www.facebook.com', 0.02)
                pg.press('enter')
            elif 'youtube' in text2:
                pg.typewrite('www.youtube.com', 0.02)
                pg.press('enter')
            elif 'anime' in text2:
                pg.typewrite('www.gogoanime.tv', 0.02)
                pg.press('enter')
    elif 'search' in text:
        subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
        open_chrome = "chrome.exe" in (i.name() for i in psutil.process_iter())
        speak('please state what your looking for.')
        new_audio = input_audio()

        if open_chrome:
            pg.typewrite(new_audio)
            pg.press('enter')
    elif 'photoshop' in text:
        speak('opening')
        subprocess.call('D://photoshop//Adobe Photoshop CC 2019//Photoshop.exe')
