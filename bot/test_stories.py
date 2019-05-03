from rasa_core.evaluate import _generate_trackers, collect_story_predictions

from rasa_core import utils
from rasa_core.utils import AvailableEndpoints
from rasa_core.run import load_agent
from rasa_core.interpreter import NaturalLanguageInterpreter
import re
import os
from os import listdir
from os.path import isfile, join

from prompt_toolkit.styles import Style
import argparse


PASSED_COLOR = utils.bcolors.OKGREEN
FAILED_COLOR = utils.bcolors.FAIL
BOLD_COLOR = utils.bcolors.BOLD
CORE_DIR = 'models/dialogue'
NLU_DIR = 'models/nlu/current'


parser = argparse.ArgumentParser()

parser.add_argument(
    '--stories', '-s', type=str, default='',
    help='Stories directory (default: tais)'
)
parser.add_argument(
    '--e2e', '--end-to-end', action='store_true',
    help='Use end-to-end evaluation (default: False)'
)

args = parser.parse_args()


files_results = {}


def is_an_intent_line(line):
    if re.search('^\*', line):
        return True
    else:
        return False

def process_failed_story(failed_story):
    print('\n')
    for line in failed_story.splitlines():
        if re.search('<!--.*-->', line):
            error_prediction = re.search('<!--(.*)-->', line).group(1).strip().split(':')
            error_message = ''
            
            if is_an_intent_line(line):
                error_message += '  Intent failed: Predicted intent' + ('{} for message \'{}\''.format(error_prediction[1], error_prediction[2]) if len(error_prediction) == 3 else error_prediction[1])
            else:
                error_message += '      Utter failed: Predicted utter' + error_prediction[1]

            line = re.sub('<!--(.*)-->', '', line)

            utils.print_color("-" * len(error_message), FAILED_COLOR)
            utils.print_color(line, FAILED_COLOR)
            utils.print_color(error_message, FAILED_COLOR)
            utils.print_color("-" * len(error_message), FAILED_COLOR)
        else:
            print(line)

def run_evaluation(stories_to_evaluate,
              fail_on_prediction_errors=False,
              max_stories=None,
              use_e2e=False):

    _endpoints = AvailableEndpoints.read_endpoints(None)
    _interpreter = NaturalLanguageInterpreter.create(NLU_DIR)
    _agent = load_agent(CORE_DIR,
                        interpreter=_interpreter,
                        endpoints=_endpoints)

    completed_trackers = _generate_trackers(stories_to_evaluate, _agent,
                                        max_stories, use_e2e)
    story_evaluation, _ = collect_story_predictions(completed_trackers, _agent,
                                                fail_on_prediction_errors,
                                                use_e2e)
    _failed_stories = story_evaluation.failed_stories

    _num_stories = len(completed_trackers)
    _file_result = [_num_stories, len(_failed_stories), []]

    file_message = "Evaluating stories for file {}".format(stories_to_evaluate)
    utils.print_color('\n' + '#' * 80, BOLD_COLOR)
    utils.print_color(file_message, BOLD_COLOR)

    files_results[stories_to_evaluate] = _file_result

    if len(_failed_stories) == 0:
        success_message = 'All the stories have passed for {}!!'.format(stories_to_evaluate)
        utils.print_color('\n' + '=' * len(success_message), PASSED_COLOR)
        utils.print_color(success_message, PASSED_COLOR)
        utils.print_color('=' * len(success_message), PASSED_COLOR)
    else:
        for failed_story in _failed_stories:
            process_failed_story(failed_story.export_stories())
            story_name = re.search('## (.*)', failed_story.export_stories()).group(1)
            files_results[stories_to_evaluate][2].append(story_name)

    utils.print_color('#' * 80 + '\n', BOLD_COLOR)

def print_files_results():
    utils.print_color('EVALUATION RESULTS:', BOLD_COLOR)

    for stories_file, file_result in files_results.items():

        _total_stories = str(file_result[0])
        _passed_stories = str(file_result[0] - file_result[1])

        utils.print_color('\n' + 'File - ' + stories_file, BOLD_COLOR)
        utils.print_color('Passed: '+ _passed_stories + '/' + _total_stories, BOLD_COLOR)

if __name__ == '__main__':
    stories_path = parser.parse_args().stories
    use_e2e = parser.parse_args().e2e

    stories_to_evaluate = []

    if os.path.isdir(stories_path):
        if not stories_path.endswith('/'):
            stories_path += '/'

        stories_files = [f for f in listdir(stories_path) if
                         isfile(join(stories_path, f))]

        for file in stories_files:
            run_evaluation(stories_path + file, False, None, use_e2e)
    else:
        run_evaluation(stories_path, False, None, use_e2e)

    print_files_results()
