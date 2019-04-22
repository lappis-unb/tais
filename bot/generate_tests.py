import logging
import shutil
import random
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


class TestsGenerator():

    def __init__(self, intents_path, stories_path):
        self.intents_files = []
        self.stories_files = []
        self.intents_texts = {}

        if os.path.isfile(intents_path):
            self.intents_files.append(intents_path)

        elif os.path.isdir(intents_path):
            if not intents_path.endswith('/'):
                intents_path += '/'

            intent_files = [f for f in listdir(intents_path) if
                            isfile(join(intents_path, f))]
            for file in intent_files:
                self.intents_files.append(intents_path + file)

        if os.path.isfile(stories_path):
            self.stories_files.append(stories_path)

        elif os.path.isdir(stories_path):
            if not stories_path.endswith('/'):
                stories_path += '/'

            stories_files = [f for f in listdir(stories_path) if
                             isfile(join(stories_path, f))]
            for file in stories_files:
                self.stories_files.append(stories_path + file)

    def load_intents_texts(self):
        for intent in self.intents_files:
            f = open(intent, 'r')
            intent_lines = f.readlines()
            f.close()

            intent_key = ''

            for line in intent_lines:
                if re.search(r'## *intent *:', line):
                    s_line = line.split(':')
                    if len(s_line) == 2 and s_line[0] == '## intent':
                        intent_key = s_line[1].strip()
                        self.intents_texts[intent_key] = []
                elif line != '' and intent_key != '':
                    self.intents_texts[intent_key].append(line[2:].strip())

    def generate_test_stories(self):
        path = 'tests'
        if os.path.exists(path):
            shutil.rmtree(path)

        os.makedirs(path)

        for storie in self.stories_files:
            f = open(storie, 'r')
            storie_lines = f.readlines()
            f.close()

            storie_test_file = open('tests/' +
                                    'test_' + storie.split('/')[-1:][0], 'w+')

            for line in storie_lines:
                if re.search(r'^ *## *', line):
                    line = re.sub('^ *## *', '## Test ', line)
                    storie_test_file.write(line)
                elif re.search(r'^ *\* *', line):
                    intent = re.sub(r'^ *\* *', '', line).strip()
                    intent_line = "* " + intent + ": " + \
                                  random.choice(self.intents_texts[intent]) \
                                  + '\n'
                    storie_test_file.write(intent_line)
                elif re.search(r'^ *- *', line):
                    storie_test_file.write(line)
                else:
                    storie_test_file.write("\n")


if __name__ == '__main__':
    stories = parser.parse_args().stories
    intents = parser.parse_args().intents

    tests_generator = TestsGenerator(intents, stories)
    tests_generator.load_intents_texts()
    tests_generator.generate_test_stories()
