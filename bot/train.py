import logging
import os

from rasa_core import utils, train
from rasa_core.agent import Agent
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer, LabelTokenizerSingleStateFeaturizer,FullDialogueTrackerFeaturizer
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy, AugmentedMemoizationPolicy
from rasa_core.policies.fallback import FallbackPolicy
from fallback import CustomFallbackPolicy

from validator import Validator

logger = logging.getLogger(__name__)
NLU_THRESHOLD = float(os.getenv('NLU_THRESHOLD', 0.6))

TRAINING_EPOCHS = int(os.getenv('TRAINING_EPOCHS', 20))
BATCH_SIZE = int(os.getenv('BATCH_SIZE', 10))
VALIDATION_SPLIT = float(os.getenv('VALIDATION_SPLIT', 0.2))


CORE_THRESHOLD = float(os.getenv('CORE_THRESHOLD', 0.6))
MAX_HISTORY = int(os.getenv('MAX_HISTORY', 2))
FALLBACK_ACTION_NAME = str(os.getenv('FALLBACK_ACTION_NAME', 'utter_default'))

utils.configure_colored_logging(loglevel='DEBUG')


def train_dialogue(domain_file,
                   model_path,
                   training_folder,
                   policy_config):
    return train.train_dialogue_model(domain_file=domain_file,
                                      stories_file=training_folder,
                                      output_path=model_path,
                                      policy_config=policy_config,
                                      kwargs={'augmentation_factor': 20,
                                              'validation_split': VALIDATION_SPLIT,}
                                      )

if __name__ == "__main__":
    validate = Validator('domain.yml','data/intents', 'data/stories/' )
    validate.run_verifications()
    train_dialogue('domain.yml', 'models/dialogue', 'data/stories/', 'policy_config.yml')
