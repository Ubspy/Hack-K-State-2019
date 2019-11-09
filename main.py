import prompt

# Initial value for our linked list
p = prompt.prompt_list('start')
while (p.next_prompt != 0):
    user_in = input(p.message + '\n')
    while (user_in not in p.acceptable_responses):
        print("Invalid response")
        s = p.message + "("
        for r in p.acceptable_responses:
            s += (r + '/') 
        s += ")\n"
        user_in = input(s)
    p = prompt.prompt_list(p.next_prompt) # p = next value in our linked list
