import argparse
from pytorch_lightning import Trainer
from model import Model


def get_args():
    parser = argparse.ArgumentParser()
    # args for program meta-data like data_path, etc.
    # parser.add_argument()

    # args for model specific hyper-parameters
    parser = Model.add_model_specific_arguments(parser)

    # args for Trainer options
    parser = Trainer.add_argparse_args(parser)

    # add other model-specific hyperparameters here

    args = parser.parse_args()
    return args
