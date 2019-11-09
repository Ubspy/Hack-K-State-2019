class Prompt:
    """A class that contains a prompt message, acceptable responses,
    and a next_prompt"""
    def __init__(self, message, acceptable_responses, next_prompt):
        self.message = message
        self.acceptable_responses = acceptable_responses
        self.next_prompt = next_prompt # a function of response

LIST = [
        Prompt("Hello! Thank you for contacting the suicide hotline. First off, you've made the right decision.", [''], 1), # 0
        Prompt("While waiting for a volunteer to become available, could you answer some important questions for us?", ['yes', 'no'], 2), # 1
        Prompt("Do you have a plan to attempt suicide?", ['yes', 'no'], 3), # 2
        Prompt("When were you planning to kill yourself?", ['today', 'tomorrow', "i don't know"], 4), # 3
        Prompt("Where would you do it?", ['house', "i don't know"], -1), # 4
        '''
        Prompt("Where are the <pills, gun, knife>? How many pills do you have? Gun loaded?"), # 5
        Prompt("Have you ever tried to take your life before? When? What happened?"), # 6
        Prompt("What's happened in your life that mkaes you want to end everything?"), # 7
        Prompt("Do you know someone who has died by suicide?"), # 8
        Prompt("Are you currently drinking alcohol or using drugs?"), # 9
        Prompt("Okay. Thank you for your responses, they will allow us to better serve your needs. We are about to connect you with a volunteer. It'll be about 3 more minutes.") # 10
        '''
        ]
