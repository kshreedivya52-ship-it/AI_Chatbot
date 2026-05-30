from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI   
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite",temperature=0.9)

print("Choose your AI mode!")
print("Pres 1 for Funny mode")
print("Press 2 for Sad mode")
print("Press 3 for Angry mode")

choice = int(input("Enter your choice :- "))

if choice == 1:
  mode = "You are an angry AI agent."
elif choice == 2:
  mode = "You are a very funny AI agent."
elif choice == 3:
  mode = "You are a angry AI agent."    

messages = [
 SystemMessage(content = "mode")
]

print("----------WELCOME TO CHATBOT----------")
print("Type '0' to exit the chatbot.")
while True:
  prompt = input("You : ")
  messages.append(HumanMessage(content=prompt))
  if prompt == "0":
    break
  response = model.invoke(prompt)
  messages.append(AIMessage(content=response.content))

  print("Bot : ", response.content)

print(messages)  