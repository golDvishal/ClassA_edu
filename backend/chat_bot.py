import openai 

Api_Key =""

openai.api_key= Api_Key

def chat_bot(command):
    response = openai.ChatCompletion.create(
        model = " gpt-3.5-turbo",
        message = [{"role":"user","content":command}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        question = input("you: ")
        if question.lower() in ["quit","close","exit","bye"]:
            break

        response = chat_bot(question)
        print("bot: ",response)