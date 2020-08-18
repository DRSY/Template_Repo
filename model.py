import transformers
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR
import pytorch_lightning as pl
from typing import *
from torch import Tensor, add, log
import argparse

from modules import *


class Model(pl.LightningModule):
    """
    Main LightningModule Class
    """

    def __init__(self) -> None:
        super().__init__()
        # instantiate needed modules here

    @staticmethod
    def add_model_specific_arguments(parent_parser):
        parser = argparse.ArgumentParser(
            parents=[parent_parser], add_help=False)
        parser.add_argument('--layers', type=int, default=3)
        # add model specific arguments here
        # parser.add_argument()
        return parser

    def forward(self, *args, **kwargs):
        """
        define forward propagation
        """
        pass

    def training_step(self, batch, batch_idx) -> Union[int, Dict[str, Union[Tensor, Dict[str, Tensor]]]]:
        pass

    def validation_step(self, batch, batch_idx) -> Dict[str, Tensor]:
        pass

    def validation_epoch_end(self, outputs: Union[List[Dict[str, Tensor]], List[List[Dict[str, Tensor]]]]) -> Dict[str, Dict[str, Tensor]]:
        pass

    def test_step(self, batch, batch_idx) -> Dict[str, Tensor]:
        pass

    def test_epoch_end(self, outputs: Union[List[Dict[str, Tensor]], List[List[Dict[str, Tensor]]]]) -> Dict[str, Dict[str, Tensor]]:
        pass

    def configure_optimizers(self): 
        pass
