#chatbot...
from dotenv import load_dotenv 
import os
from groq import Groq
load_dotenv()
groq_key=os.getenv("groq_api_key")
c=True

history=[{"role":"system","content":"speak 1 word"}]
client=Groq(api_key=groq_key)
while c==True:
    user=input("User: ")
    history.append({"role":"user","content":user})
    response=client.chat.completions.create( messages=history, model="llama-3.3-70b-versatile")     #send user response to bot and get its reply   you are a healthcare assistant who will take data and make a prediction if person will be readmitted"
    bot=response.choices[0].message.content
    history.append({"role":"assistant","content":bot})
    if len(history)>6:
        _=history.pop(1)
        _=history.pop(1)
    print('Bot: ',bot)
    c=input("Continue? y/n")
    c=False if c=='n' else True


print(history)
