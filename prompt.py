import yaml

objdict = {}

class Prompt:
    """A class that contains a prompt message, acceptable responses,
    and a next_prompt"""
    def __init__(self, message, next_prompt):
        self.message = message
        self.next_prompt = next_prompt # a dict that looks like {'kill': ['yes', 'i think so']}

    def next(self, contains): # a function that takes a word and returns the next prompt based on that
        for promptname, keywords in self.next_prompt.items():
            if contains in keywords:
                return promptname

def load(filename):
    with open(filename) as f:
        d = yaml.load(f)
    for key, value in d.items():
        objdict[key] = Prompt(value['message'], value['next_prompt'])

def prompt_list(key):
    if not objdict:
        load('data.yml')
    return (objdict[key])
