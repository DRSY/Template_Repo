# The template code base for a typical NLP research project

## Underpinning Libraries
+ [torch](https://pytorch.org/)
+ [pytorch_lightning](https://github.com/PyTorchLightning/pytorch-lightning)
+ [transformers](https://github.com/huggingface/transformers)
+ [nlp](https://github.com/huggingface/nlp)
+ argparse

## Folder Structure
- config: contains all **hyper-parameters**
- data: util method/class for **dataset** and **dataloader**
- modules: pytorch native modules needed in the project
- model: pytorch-lightning main class
- main: entrance script that controls model training and evaluation

## Tips 
### How to manipulate **flags** for Trainer
- specify your choices in the command line like
```bash
python -u main.py --gpus=0,1, --max_epochs=10 --precision=16 --gradient_clip_val=5 --track_grad_norm=2 ...
```
other flags that are not specified will be set to the default value by Trainer.

### How to set up own early stopping strategy
- create customized EarlyStopping object and pass it to the trainer's initialization method
```python
early_stop_callback = EarlyStopping(
    monitor="val_loss",
    mode="min",
    patience=3,
    verbose=False,
)
trainer = Trainer(early_stop_callback=early_stop_callback)
```