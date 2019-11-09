import prompt

# Initial value for our linked list
p = prompt.prompt_list('start')
while (0 not in p.next_prompt.keys()):
    user_in = input(p.message + '\n').lower()
    words = user_in.split(" ")
    choice = None
    for word in words:
        choice = p.next(word)
        if choice is not None:
            break
    if choice is None:
        print("Sorry, I didn't understand that.", end=" ")
    else:
        p = prompt.prompt_list(choice) # p = next value based on user input

print(p.message + '\n')
