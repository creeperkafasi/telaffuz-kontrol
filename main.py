from gtts import gTTS
import speech_recognition as sr
import comparestrings as cs
r = sr.Recognizer()
def checkpronunciation():
    truetext = input("Telaffuzunu kontrol etmek istediğiniz sözcüğü giriniz:").strip()
    with sr.Microphone() as source:
        print("Dinliyorum...\n")
        audio = r.listen(source)
        rtext = str(r.recognize_google(audio,language = "tr"))
        print(rtext)
        mp = round(cs.match_percent(truetext,rtext),4)
        print("Telaffuzunuz %",mp*100,"doğru")
        if mp!=1:
            # Hatalı yerleri göster
            pass
print("Merhaba!\n")

cikis = False
while cikis == False:
    checkpronunciation()
    while True:
        p = input("Yeniden denemek ister misiniz? (e/h)")
        if p == "h" or p == "e":
            cikis = int(p=="h")
            break

print("Program kapatılıyor...")