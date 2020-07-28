import argparse
from pytorch_lightning import Trainer


def get_args():
    parser = argparse.ArgumentParser()
    
    # args for pl Trainer
    parser = Trainer.add_argparse_args(parser)

    # add other model-specific hyperparameters here

    args = parser.parse_args()
    return args