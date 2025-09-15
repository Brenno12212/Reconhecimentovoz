import speech_recognition as sr
import pyttsx3

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def ouvir():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ajustando para o ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        print("Pode falar!")
        try:
            audio = recognizer.listen(source)
        except sr.WaitTimeoutError:
            msg = "Nenhuma fala detectada. Tente novamente."
            print(msg)
            falar(msg)
            return ""
    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"{texto}")
        falar(texto)
        return texto
    except sr.UnknownValueError:
        msg = "Não entendi o que você disse."
        print(msg)
        falar(msg)
        return ""
    except sr.RequestError:
        msg = "Erro ao conectar ao serviço de reconhecimento."
        print(msg)
        falar(msg)
        return ""

if __name__ == "__main__":
    while True:
        frase = ouvir()
        if frase:
            if frase.lower() in ["sair", "exit", "quit"]:
                falar("Até logo!")
                break
            falar(frase)
