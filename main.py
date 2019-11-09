import prompt
PROMPTS=["Hello! Thank you for contacting the suicide hotline. First off, you've made the right decision.\nWhile waiting for a volunteer to become available, could you answer some important questions for us?", 
        "Do you have a plan to attempt suicide?", 
        "When were you planning to kill yourself?", 
        "Where would you do it?", 
        "What would you use?", 
        "Where is the weapon? How many pills do you have? Gun loaded?", 
        "Have you ever tried to take your life before? When? What happened?", 
        "What's happened in your life that makes you want to end everything?", 
        "Who have you talked with about wanting to end your life?", 
        "On a scale of 1-10, (1 being normally upbeat, 10 being extremely depressed or hopeless) how would you say you feel?", 
        "What might you feel your suicide would help you to do?", 
        "Do you know someone who has died by suicide?", 
        "Are you currently drinking alcohol or using drugs?", 
        "Okay. Thank you for responses, they will allow us to give you more personalized care. We are about to connect you with a volunteer. It'll be about 3 more minutes."]

responses = []
# Initial value for our linked list
p = prompt.LIST[0]
while (p.next_prompt != -1):
    user_in = input(p.message + '\n')
    while (user_in not in p.acceptable_responses):
        print("Invalid response")
        s = p.message + "("
        for r in p.acceptable_responses:
            s += (r + '/') 
        s += ")\n"
        user_in = input(s)
    p = prompt.LIST[p.next_prompt] # p = next value in our linked list
