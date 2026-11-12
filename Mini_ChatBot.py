print("Welcome To Your Ai Chatbot Buddy")
print("You Can Ask Me Basic Questions , Type 'bye' To Exit From The Bot.")

#Chatbot Memory Creation
responses = {
    "hello":"Hi, Welcome. How Can I Help You ?",
    "how are you":"I'm Fine Thankyou.",
    "who are you":"I,m Your Ai Chatbot Buddy.",
    "motivate me":"Buddy You Need To Believe In Yourself.",
    "bye":"Thank you, I Had A Great Experience Helping You."
}

def getRes(str):
    str = str.lower()
    for i in responses:
        if i in str:
            return responses[i]
    return "Abhi Mujhe Ye Nhi Aata"

#Take User Input
while True :
    user = input("Please ask your question : ")
    reply = getRes(user)
    print("Bot Response :",reply)

    if "bye" in user.lower():
        break
