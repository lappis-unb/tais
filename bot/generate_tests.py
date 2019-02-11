import logging
import os
from os import listdir
from os.path import isfile, join
import argparse
import re

logger = logging.getLogger(__name__) 

parser = argparse.ArgumentParser()

parser.add_argument(
    '--stories', type=str, default='data/stories.md',
    help='Path for the stories file or directory'
) 

parser.add_argument(
    '--intents', type=str, default='data/intents.md',
    help='Path for the intents file or directory'
)

class TestGenerator():

    def __init__(self, intents_path, stories_path):
        self.intents_files = []
        self.stories_files = []
        self.intents_texts = {}

        if os.path.isfile(intents_path):
            self.intents_files.append(intents_path)

        elif os.path.isdir(intents_path):
            if not intents_path.endswith('/'):
                intents_path += '/'

            intent_files = [f for f in listdir(intents_path) if isfile(join(intents_path, f))]
            for file in intent_files:
                self.intents_files.append(intents_path + file)
                     
        if os.path.isfile(stories_path):
            self.stories_files.append(stories_path)

        elif os.path.isdir(stories_path):
            if not stories_path.endswith('/'):
                stories_path += '/'

            stories_files = [f for f in listdir(stories_path) if isfile(join(stories_path, f))]
            for file in stories_files:
                self.stories_files.append(stories_path + file)


    def load_intents_texts(self):
        for intent in self.intents_files:
            f = open(intent, 'r')
            intent_lines = f.readlines()
            f.close()

            intent_key = ''
    
            for line in intent_lines:
                if re.search('## *intent *:',line):
                    s_line = line.split(':')
                    if len(s_line) == 2 and s_line[0] == '## intent':
                        intent_key = s_line[1].strip()
                        self.intents_texts[intent_key] = []
                elif line != '' and intent_key != '':
                    self.intents_texts[intent_key].append(line[2:].strip())

            for intent_name, intent_texts in self.intents_texts.items():
                print("\n\n")
                print("INTENT NAME:",intent_name)
                print(intent_texts)
                print("\n\n")

if __name__ == '__main__':
    stories = parser.parse_args().stories
    intents = parser.parse_args().intents

    test_generator = TestGenerator(intents, stories)
    test_generator.load_intents_texts()
