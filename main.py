from gtts import gTTS
import speech_recognition as sr
import utils
r = sr.Recognizer()
def checkpronunciation():
    truetext = input("Telaffuzunu kontrol etmek istediğiniz sözcüğü giriniz:").strip()
    with sr.Microphone() as source:
        print("Dinliyorum...\n")
        audio = r.listen(source)
        rtext = str(r.recognize_google(audio,language = "tr"))
        print(rtext)
        mp = round(utils.match_percent(truetext,rtext),4)
        print("Telaffuzunuz %",mp*100,"doğru")
        if mp!=1:
            i = input("Telaffuzunuzdaki hataları görmek ister misiniz?(e/h)")
            while not((i=="e")or(i=="h")):
                i = input("Telaffuzunuzdaki hataları görmek ister misiniz?(e/h)")
            if i=="e":
                utils.check_match(truetext,rtext)
            

print("Merhaba!\n")
cikis = False
while cikis == False:
    checkpronunciation()
    while True:
        p = input("Yeniden denemek ister misiniz? (e/h)")
        if p == "h" or p == "e":
            cikis = int(p=="h")
            break

input("Çıkış için enter tuşuna basınız")