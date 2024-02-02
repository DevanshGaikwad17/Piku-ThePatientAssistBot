import time
import pywhatkit
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import tkinter as tk
from tkinter import PhotoImage


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception:
        return "None"
    return query


print("started successfully")
speak("started successfully")

if __name__ == '__main__':
    class FlowerUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Flower UI")
        
            # Load flower background image
            self.flower_image = PhotoImage(file= "piku symbol.PNG")
        
            # Create a Canvas widget and pack it to fill the window
            self.canvas = tk.Canvas(root, width=1500, height=800)
            self.canvas.pack(fill=tk.BOTH, expand=True)

            # Display flower background 
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.flower_image)
            


if __name__ == "__main__":
    root = tk.Tk()
    flower_ui = FlowerUI(root)
    root.mainloop()


    while True:
        query = takeCommand().lower()
        if 'piku' in query:
            query = query.replace("piku", "")

            if 'tell me about' and 'from wikipedia' in query:
                speak('finding information')
                query = query.replace("tell me about", "")
                query = query.replace("from wikipedia", "")
                results = wikipedia.summary(query, sentences=1)
                speak(results)
                print(results)

            elif 'search' in query:
                speak("ok")
                query = str(query)
                query = query.replace("search", "")
                webbrowser.open('https://www.google.com/search?q=' + query)             

            elif 'tell me' in query:
                speak("ok")
                query = str(query)
                query = query.replace("tell me", "")
                webbrowser.open('https://www.google.com/search?q=' + query)

            elif 'search in youtube' in query:
                speak("ok") 
                query = query.replace("search in youtube", "")
                webbrowser.open('https://www.youtube.com/results?search_query=' + query)
                query = ""

            elif 'chrome' in query:
                query = ""
                speak("ok")
                chr_dir = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(os.path.join(chr_dir))

            elif 'google' in query:
                query = ""
                speak("ok")
                chr_dir = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(os.path.join(chr_dir))

            elif 'edge' in query:
                query = ""
                speak("ok")
                edg_dir = 'C:\\Users\\devan\\OneDrive\\Desktop\\Personal - Edge.lnk'
                os.startfile(os.path.join(edg_dir))

            elif 'browser' in query:
                query = ""
                speak("ok")
                chr_dir = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
                os.startfile(os.path.join(chr_dir))

            elif 'youtube' in query:
                query = ""
                speak("ok")
                webbrowser.open("https://www.youtube.com/watch?v=")

            elif "play" and "chess" in query:
                query = ""
                speak("yes, sure")
                webbrowser.open("https://www.chess.com/play/computer")

            elif 'hello' in query:
                query = ""
                speak("Hello, How are you")

            elif 'sup' in query:
                query = ""
                speak("Sup, whats up")

            elif "what's up" in query:
                query = ""
                speak("I'm good, just Having fun talking with you")

            elif 'bye' in query:
                query = ""
                speak("bye")

            elif 'see you later' in query:
                query = ""
                speak("ok bye")

            elif 'chrome' in query:
                query = ""
                speak("ok")

            elif 'i am fine' in query:
                query = ""
                speak("that's nice")

            elif 'i am good' in query:
                query = ""
                speak("that's really nice")

            elif 'help' in query:
                query = ""
                speak("Sure, I'm here to assist! Just tell me what you need, and I'll do my best to help.")

            elif 'like to talk with me' in query:
                query = ""
                speak("I love to talk with you, so feel free to start a conversation or ask any questions ")

            elif 'you like' in query:
                query = ""
                speak("I like to help people wherever and whenever I can")

            elif 'likings' in query:
                query = ""
                speak("I like to help people wherever and whenever I can")

            elif 'favourite singer' in query:
                query = ""
                speak("I like many singers like Arijit Singh,Shreya Ghoshal and Lata Mangeshkar")

            elif 'favourite actor' in query:
                query = ""
                speak("I like Ranveer Singh and Tom Cruise")

            elif 'favourite sports' in query:
                query = ""
                speak("I like watching football and and hockey")

            elif 'how are you' in query:
                query = ""
                speak("I am fine, thanks")

            elif 'thankyou' in query:
                query = ""
                speak("you are welcome")

            elif 'thanks' in query:
                query = ""
                speak("no problem")

            elif 'who created you' in query:
                query = ""
                speak("I was created by RoboMaster")

            elif 'time' in query:
                query = ""
                hour = int(datetime.datetime.now().hour)
                if hour < 12:
                    ab = "am"
                else:
                    ab = "pm"
                strTime = time.strftime("%I:%M" + ab)
                speak(f"the time is {strTime}")

            elif 'date' in query:
                query = ""
                speak(time.strftime("%d-%m-%Y"))

            elif 'play'and 'chess' in query:
                query = ""
                speak("ok lets play chess")
                webbrowser.open("https://quizizz.com/join/topic/4/Science")


            elif 'weather' in query:
                query = ""
                webbrowser.open("https://www.google.com/search?q=weather+in+3G+Homes+Crimson+Layout%2C+Kadugodi%2C+Bengaluru%2C+Karnataka&rlz=1C1CHBD_enIN974IN975&biw=1536&bih=664&sxsrf=ALiCzsZDNc4_DSwa5yD1cKjNP22HrXCXoQ%3A1653116675685&ei=A4-IYpeuKcedseMPhJiH4AY&ved=0ahUKEwjXu-fBg_D3AhXHTmwGHQTMAWwQ4dUDCA4&uact=5&oq=weather+in+3G+Homes+Crimson+Layout%2C+Kadugodi%2C+Bengaluru%2C+Karnataka&gs_lcp=Cgdnd3Mtd2l6EAM6BwgjELADECc6BwgAEEcQsAM6BAgjECc6BAgAEEM6CwgAELEDEIMBEJECOgUIABCRAkoECEEYAEoECEYYAFCxCljCcGDMdGgBcAF4AIABf4gB9gGSAQMwLjKYAQCgAQGgAQLIAQnAAQE&sclient=gws-wiz")

            if 'news' in query:
                query = ""
                speak("yes why not")
                webbrowser.open("https://www.youtube.com/watch?v=Cy_6-_XUW-c")

            elif 'open messenger' in query:
                query = ""
                speak("ok")
                mes_dir = 'C:\\Users\\devan\\AppData\\Local\\Programs\\all-in-one-messenger\\All-in-One Messenger.exe'
                os.startfile(os.path.join(mes_dir))

            elif 'family photos' in query:
                query = ""
                speak("ok")
                webbrowser.open("https://photos.google.com/")

            elif 'your birthday' in query:
                query = ""
                speak("My birthday is on 31st of Jan 2023")

            elif "that's great" in query:
                query = ""
                speak("Thanks")

            elif "it's great" in query:
                query = ""
                speak("Thanks")

            elif "sup" in query:
                query = ""
                speak("Sup, whats up")

            elif "that's awesome" in query:
                query = ""
                speak("Thanks")

            elif "see you later" in query:
                query = ""
                speak("see you later aligator")

            elif "help" in query:
                query = ""
                speak("Sure, I'm here to assist! Just tell me what you need, and I'll do my best to help.")

            elif "like to talk with me" in query:
                query = ""
                speak("I love to talk with you, so feel free to start a conversation or ask any questions")

            elif "likings" in query:
                query = ""
                speak("I like to help people wherever and whenever I can")

            elif "you like" in query:
                query = ""
                speak("I like to help people wherever and whenever I can")

            elif "joke" in query:
                query = ""
                speak("What is the one reason you cannot trust atoms?")
                time.sleep(1)
                speak("They make up everything.")

            elif "like to talk with me" in query:
                query = ""
                speak("Thanks")

            elif "like to talk with me" in query:
                query = ""
                speak("Thanks")

            elif 'play' and 'ganesh aarti' in query:
                query = ""
                speak("ok")
                webbrowser.open("https://www.youtube.com/watch?v=Y32yJ4goe3c")

            elif 'play' and 'music' in query:
                query = ""
                speak("ok")
                music_dir = 'C:\\Users\\devan\\Music\\Playlists'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[1]))

            elif 'That’s wonderful' in query:
                query = ""
                speak("Thankyou")

            elif 'send whatsapp message' in query:
                swin = query.replace("send whatsapp message", "")
                query = ""
                speak("to whom do you want to message")
                pywhatkit.sendwhatmsg_instantly(query, swin)

            elif 'whatsapp' and 'call' in query:
                swin = query.replace("whatsapp", "")
                swin = query.replace("call", "")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'exercise routine' in query:
                if 'cancer' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=cc435ONdnFY")

                if 'diabetes' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=i0H82s70k34")

                if 'arthritis' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=L-0juIM2aCI")

                if 'asthma' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=dpTNUGwXbTU")

                if 'dementia' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=9nDBY2tH3lI")

            elif 'diet plan' in query:
                if 'cancer' in query:
                    speak("Cancer patients should maintain a balanced diet, consulting healthcare teams for personalized plans. Prioritize diverse, nutrient-rich foods and ensure adequate protein from sources like poultry and nuts. Stay hydrated with water and consider smaller, frequent meals. Manage weight, control portions, and address nutrient deficiencies. Limit processed foods, consult on supplements, and adapt the diet to preferences. Collaborate with healthcare professionals to manage side effects like nausea, recognizing the uniqueness of each situation.")

                if 'diabetes' in query:
                    speak(" For effective diabetes management through diet, collaborate with healthcare professionals, especially a dietitian, for a personalized approach. Focus on a balanced intake of carbohydrates from low glycemic sources, lean proteins, and healthy fats. Emphasize fiber-rich foods, control portion sizes, and limit saturated and trans fats. Maintain consistent meal timing, stay hydrated, and avoid added sugars. Regular blood sugar monitoring is crucial, and the plan should be tailored to individual preferences, lifestyle, and health considerations.")

                if 'arthritis' in query:
                    speak("For arthritis management, focus on an anti-inflammatory diet with foods like fatty fish, nuts, seeds, and colorful fruits and vegetables. Incorporate omega-3 sources such as fish oil, flaxseeds, and walnuts. Choose whole grains, lean proteins like poultry and tofu, and ensure sufficient calcium and vitamin D intake. Limit processed foods, sugars, and saturated fats, stay hydrated, and consider moderate alcohol consumption. Weight management is essential. Consult with healthcare professionals, including a dietitian, for personalized advice tailored to your needs and any medication considerations.")

                if 'asthma' in query:
                    speak("For asthma management, focus on an anti-inflammatory diet with antioxidant-rich foods like fruits, vegetables, and nuts. Include omega-3 sources such as fatty fish and flaxseeds, ensure adequate vitamin D from fortified foods, and consume magnesium-rich items like leafy greens. Incorporate vitamin C-rich foods and be cautious of sulfites in processed foods. Stay hydrated, choose healthy fats, and maintain a healthy weight. Individual responses to foods vary, so consult with healthcare professionals, including a dietitian, for personalized guidance aligned with overall asthma management.")

                if 'dementia' in query:
                    speak("Creating a dementia-friendly diet involves prioritizing nutrient-dense foods like fruits, vegetables, whole grains, lean proteins, and healthy fats. Omega-3 fatty acids from sources like fish and nuts support brain health, while antioxidants in berries and greens combat oxidative stress. The plan minimizes processed foods, moderates caffeine and sugar intake, and encourages hydration through water and hydrating foods. Cultural preferences are considered for a more enjoyable experience. Regular communication with healthcare providers is crucial for monitoring and adjusting the diet based on individual needs, potentially including supplements under professional guidance.")


            elif 'introduce yourself' in query:
                query = ""
                speak("Sure, My name is piku, and I am  a smart robot, created by RoboMaster to assist paitents in their daily routine.. I am a companion for paitents and I engage, entertain, support,and help them connect to the social world and I can engage with patient through voice and app and help them remain active. I schedule their routine exercise through display and instructions to keep them fit. I read news and give weather updates and keep them updated. I Play Music and run programs they like. I keep them happy through entertainment through fun games. I assist them by providing medicine and water. Remind them of events and appointments. I control the home with smart touch and provide comfort. I keep them connected with the near and dear ones with voice call and whatsapp message. I help them Call their dear ones in case of emergency. ")

            elif 'good evening' in query:
                query = ""
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak("Good Morning")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon")

                else:
                    speak("Good Evening")

            elif 'good afternoon' in query:
                query = ""
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak("Good Morning")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon")

                else:
                    speak("Good Evening")

            elif 'good morning' in query:
                query = ""
                hour = int(datetime.datetime.now().hour)
                if hour >= 0 and hour < 12:
                    speak("Good Morning")

                elif hour >= 12 and hour < 18:
                    speak("Good Afternoon")

                else:
                    speak("Good Evening")

            elif 'good night eco' in query:
                query = ""
                speak("good night")

            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            if hour == 23 and min == 00 and sec > 00 and sec < 8:
                speak("hey, its time to sleep")

            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            if hour == 7 and min == 0 and sec > 00 and sec < 8:
                speak("hey, its time to wake up")

            hour = int(datetime.datetime.now().hour)
            min = int(datetime.datetime.now().minute)
            sec = int(datetime.datetime.now().second)
            if hour == 9 and min == 57 and sec > 00 and sec < 8:
                speak("hey, its exersize time")

