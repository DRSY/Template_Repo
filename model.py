import transformers
import torch
import torch.nn as nn
import torch.optim as optim
import pytorch_lightning as pl
from typing import *
from torch import Tensor

from .modules import *


class Model(pl.LightningModule):
    """
    Main LightningModule Class
    """

    def __init__(self) -> None:
        super().__init__()
        # instantiate needed modules here

    def forward(self, *args, **kwargs):
        """
        define forward propagation
        """
        pass

    def training_step(self, *args, **kwargs) -> Union[int, Dict[str, Union[Tensor, Dict[str, Tensor]]]]:
        pass

    def validation_step(self, *args, **kwargs) -> Dict[str, Tensor]:
        pass

    def validation_epoch_end(self, outputs: Union[List[Dict[str, Tensor]], List[List[Dict[str, Tensor]]]]) -> Dict[str, Dict[str, Tensor]]:
        pass

    def configure_optimizers(self) -> Optional[Union[Optimizer, Sequence[Optimizer], Dict, Sequence[Dict], Tuple[List, List]]]:
        pass