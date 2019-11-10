import yaml

objdict = {}

class Prompt:
    """A class that contains a prompt message, acceptable responses,
    and a next_prompt"""
    def __init__(self, message, next_prompt, generated=False):
        self.message = message
        self.next_prompt = next_prompt # a dict that looks like {'kill': ['yes', 'i think so']}
        self.generated = generated # Whether or not the response needs to be generated using the NLP black magic

    def next_name(self, contains): # a function that takes a word and returns the NAME of the next prompt based on that
        for promptname, keywords in self.next_prompt.items():
            if contains in keywords:
                return promptname

def load(filename):
    with open(filename) as f:
        d = yaml.load(f)
    for key, value in d.items():
        objdict[key] = Prompt(value['message'], value['next_prompt'], value['generated'])

def get_obj(key): # we have a dictionary of prompts; return a prompt given a key
    if not objdict:
        load('data.yml')
    return (objdict[key])
