# automl-itmo

## Steps to reproduce
- clone repo `git clone https://github.com/grk717/automl-itmo.git`
- pull data and weights `git lfs pull`
- install requirements from requirements.txt `pip install -r requirements.txt`
- run EDA notebook `icebergs_eda.ipynb`, it will create some data used in future 
- run LAMA notebook `icebergs_lama.ipynb`, it will create some data used in future 
- run `icebergs_manual.ipynb`, follow the instructions in the notebook

## Competition

Link to the competition:
https://www.kaggle.com/competitions/statoil-iceberg-classifier-challenge/

Metric for the competition is [LogLoss](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.log_loss.html)

## Results 

Made 4 submission, 3 of them are covered in this repo:
- LAMA with no EDA features (not covered) - 0.35363 on private data
- LAMA with EDA features  - 0.33921 on private data
- LAMA with EDA features (added LGBM to blending, changed visual encoder backbone)  - 0.32255 on private data
- YOLOv8 nano classifier - 0.26574 on private data