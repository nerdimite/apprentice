# Apprentice

### Udacity Machine Learning Engineer Nanodegree Capstone Project

Apprentice is an automatic test assessment engine made as part of the Capstone Project in Udacity's Machine Learning Engineer Nanodegree.

The Project Report can be found [here](Project_Report.pdf)

## Setup

### Libraries Required

- Tensorflow 2.0 (Preferably GPU version)
- Tensorflow-Hub
- Scikit Learn
- Numpy
- Pandas
- tqdm
- Matplotlib
- Anvil-Uplink (`pip install anvil-uplink`)

## Usage

### Inference

The pretrained model can be used to perform inference and make predictions with the web app.

1. Run all the cells in [Inference.ipynb](Inference.ipynb)
2. Open the Web Application at https://apprentice.anvil.app/. The input text boxes in the web app are prefilled to give an example.

### Train

If you wish to re-train the model, you can refer [Train.ipynb](Train.ipynb) notebook.

## References
* Dataset: https://www.quora.com/q/quoradata/First-Quora-Dataset-Release-Question-Pairs
* Benchmark Models: https://towardsdatascience.com/finding-similar-quora-questions-with-bow-tfidf-and-random-forest-c54ad88d1370
