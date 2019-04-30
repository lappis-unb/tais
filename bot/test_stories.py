from rasa_core.evaluate import _generate_trackers, collect_story_predictions

from rasa_core.utils import AvailableEndpoints
from rasa_core.run import load_agent
from rasa_core import utils
from rasa_core.interpreter import NaturalLanguageInterpreter
import re

from prompt_toolkit.styles import Style
import argparse


PASSED_COLOR = utils.bcolors.OKGREEN
FAILED_COLOR = utils.bcolors.FAIL
CORE_DIR = 'models/dialogue'
NLU_DIR = 'models/nlu/current'


parser = argparse.ArgumentParser()

parser.add_argument(
    '--stories', '-s', type=str, default='',
    help='Stories directory (default: tais)'
parser.add_argument(
    '--e2e', '-e', type=str, default='False',
    help='Use end-to-end evaluation (default: False)'
)

args = parser.parse_args()


def process_failed_stories(failed_story):
    #if not re.search(re.search("<!--.*-->", failed_story)):
    #    print("DEUUUU BOMOMMMM")            
    #else:
    utils.print_color(failed_story, FAILED_COLOR)
        #for line in failed_story.splitlines():
        #    print("\n\n")
        #    print(line)
        #    print("\n\n")

def run_tests(stories_to_evaluate,
              fail_on_prediction_errors=False,
              max_stories=None,
              use_e2e=True):

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

    if len(_failed_stories) == 0:
        utils.print_color("="*25, PASSED_COLOR)
        utils.print_color("All stories have passed!!", PASSED_COLOR)
        utils.print_color("="*25, PASSED_COLOR)

    #for failed_story in _failed_stories:
    #    process_failed_stories(failed_story.export_stories())

if __name__ == '__main__':
    stories = parser.parse_args().stories
