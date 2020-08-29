from config import get_args
from data import get_data_loader

from pprint import pprint

import torch
import pytorch_lightning as pl
from pytorch_lightning import Trainer, seed_everything
from pytorch_lightning.callbacks import EarlyStopping, ModelCheckpoint
from pytorch_lightning.loggers import TensorBoardLogger


import logging
logging.basicConfig(format="%(filename)s:%(lineno)d - %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S",
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def main(args):
    logger.info("Training start")
    # seed all
    seed_everything(args.seed)

    # get train/val/test dataloader
    # train_loader, val_loader, test_loader = get_data_loader

    # get model
    # model = MainClass(*args)

    # init trainer
    trainer = Trainer.from_argparse_args(args)

    # usage
    # trainer.fit(model, train_loader, val_loader)
    # trainer.test(model, test_loader)


if __name__ == "__main__":
    args = get_args()
    pprint(vars(args))
    main(args)
# 