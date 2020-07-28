from .config import get_args
from .data import get_data_loader

from pprint import pprint

import torch
import pytorch_lightning as pl
from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint
from pytorch_lightning.loggers import TensorBoardLogger


def main(args):
    # seed all
    seed_everything(args.seed)

    # get train/val/test dataloader

    # get model

    # init trainer
    trainer = Trainer.from_argparse_args(args)


if __name__ == "__main__":
    args = get_args()
    pprint(vars(args))
    main(args)
