#chatbot...
from dotenv import load_dotenv 
import os
from groq import Groq
import json

load_dotenv()
groq_key=os.getenv("groq_api_key")
c=True

patient_data={"name":"", "age":None, "medical_history":[], "previous_admissions_in_last_yr":None}

history=[{"role":"system","content":"speak 1 word"}]

client=Groq(api_key=groq_key)

def chat():
    user=input("User: ")
    history.append({"role":"user","content":user})

    response=client.chat.completions.create( messages=history, model="llama-3.3-70b-versatile")     #send user response to bot and get its reply   you are a healthcare assistant who will take data and make a prediction if person will be readmitted"
    bot=response.choices[0].message.content
    print('Bot: ',bot)

    history.append({"role":"assistant","content":bot})
    
def convert_to_json(raw):
    modified_update=raw.replace("```json", "")
    modified_update=modified_update.replace("```", "")
    modified_update=modified_update.strip()
    modified_update=modified_update.replace("'",'"')
    return modified_update


def update(patient_data,history):
    updation=client.chat.completions.create(model="llama-3.3-70b-versatile",messages=[{"role":"user","content":f"update data in JSON ONLY (not python): {patient_data}, given recent history: {history[2:]}"}])
    raw_update=(updation.choices[0].message.content)
    modified_update=convert_to_json(raw_update)

    patient_data=json.loads(modified_update)
    print(modified_update, patient_data)

    history[1]={"role":"system","content":f"patient data: {patient_data}"}


count=0
while c==True:
    count+=1
    chat()


    if count>5:
        update(patient_data,history)
        count=0

    if len(history)>6:
        history=history[0:2]+history[-5:]
    c=input("Continue? y/n")
    c=False if c=='n' else True


print(history)
