import argparse
from pytorch_lightning import Trainer
from model import Model
import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s", datefmt="%a, %d %b %Y %H:%M:%S")
logger = logging.getLogger(__name__)


def get_args():
    parser = argparse.ArgumentParser()
    # args for program meta-data like data_path, etc.
    parser.add_argument('--seed', type=int, default=42,
                        help='random seed for reproducibility')

    # args for model specific hyper-parameters
    parser = Model.add_model_specific_arguments(parser)

    # args for Trainer options
    parser = Trainer.add_argparse_args(parser)

    # add other model-specific hyperparameters here

    args = parser.parse_args()
    return args
