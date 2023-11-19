
import os, random,sys

try:
    import openai
except:
    os.system("pip install openai")
    import openai
try:
    import rich
except:
    os.system("pip install rich")
    import rich

from rich import print
from rich import print_json
from rich import pretty
from rich.panel import Panel
from rich.markdown import Markdown 
pretty.install()
os.system("xdg-open https://t.me/PY_LEARNER")

try:
    import gtts
except:
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)

def dual(text,file):
    create_(text,file)
    play_audio(file)
logo="""
[bold violet]  ___  _  _   __  ____     ____  _  _ 
 / __)/ )( \ / _\(_  _)___(  _ \( \/ )
( (__ ) __ (/    \ )( (___)) __/ )  / 
 \___)\_)(_/\_/\_/(__)    (__)  (__/  
 """
develop={
"FACEBOOK":"HERON AFRIDI",
"MAIN WORK":"Data Analyst",
"TEAM":"ELITE",
}
welcome=["Give cradite for Team Elite","Hello world, my name is Kaitlyn.","System Started successfuly","hey, learner welcome to CHat-PY","Welcome ,I am A.I"]






#------------------------------------------------#
# todo Authorization 👇
#openai.api_key_path ="/sdcard/key.txt"
#openai.api_key =""


def heron_afridi():
    os.system("clear")
    print(Panel.fit(logo))
    print_json(data=develop)
    print(Markdown("\n- This Tool Is Only For __Learning__ Anything\n- Use It For **Fatch** Information & Data "))
    jk=random.choice(welcome)
    dual(jk,"n.mp3")
    while True:
        prompt = input ("\n\n\n[ Give Question ? ] >")
        response = openai.Completion.create(engine="text-davinci-002",prompt=prompt,max_tokens=1024,n=1,stop=None,temperature=0.5,)
        generated_text = response["choices"][0]["text"]
        reply=Markdown("# "+prompt.upper())
        print("\n\n")
        print(reply)
        print(f"\n\n[bold green] {generated_text}")
        dual(generated_text,"n.mp3")

heron_afridi()
