#chatbot...
from dotenv import load_dotenv 
import os
from groq import Groq

load_dotenv()
groq_key=os.getenv("groq_api_key")
c=True

history=[{"role":"system","content":"speak 1 word"}]
long_history=[{"role":"system","content":"speak exactly 1 word only"}]

client=Groq(api_key=groq_key)
count=0
while c==True:
    count+=1

    user=input("User: ")
    history.append({"role":"user","content":user})
    response=client.chat.completions.create( messages=history, model="llama-3.3-70b-versatile")     #send user response to bot and get its reply   you are a healthcare assistant who will take data and make a prediction if person will be readmitted"
    bot=response.choices[0].message.content
    print('Bot: ',bot)

    long_history.append({"role":"user","content":user})
    history.append({"role":"assistant","content":bot})
    long_history.append({"role":"assistant","content":bot})

    if count>5:
        summarize=client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[{"role":"user","content":f"summarise this: {long_history}"}])
        summary=summarize.choices[0].message.content
        history[1]={"role":"system","content":f"summary: {summary}"}

    if len(history)>6:
        history=history[0:2]+history[-5:]
    c=input("Continue? y/n")
    c=False if c=='n' else True


print(history)
