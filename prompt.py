import yaml

objdict = {}

class Prompt:
    """A class that contains a prompt message, acceptable responses,
    and a next_prompt"""
    def __init__(self, message, acceptable_responses, next_prompt):
        self.message = message
        self.acceptable_responses = acceptable_responses
        self.next_prompt = next_prompt # a string that matches a key in objdict 

def load(filename):
    with open(filename) as f:
        d = yaml.load(f)
    for key, value in d.items():
        objdict[key] = Prompt(value['message'], value['acceptable_responses'], value['next_prompt'])

def prompt_list(key):
    if not objdict:
        load('data.yml')
    return (objdict[key])
