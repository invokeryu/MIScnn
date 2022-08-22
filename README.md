
**Step-by-Step workflow:**

Download the code repository via git clone to your disk. Afterwards, install all required dependencies, download the dataset and setup the file structure.

```sh
git clone https://github.com/muellerdo/covid19.MIScnn.git
cd covid19.MIScnn/

pip3 install -r requirements.txt
python scripts/download_data.py
```

Optionally, you can run the data exploration, which give some interesting information about the dataset.

```sh
python3 scripts/data_exploration.py
python scripts/data_exploration.py
```

For the training and inference process, you initialize the cross-validation folds by running the preprocessing. This setups a validation file structure and randomly samples the folds.

The most important step is running the training & inference process for each fold. This can be done either sequential or parallized on multiple GPUs.

```sh
python3 scripts/run_preprocessing.py
python scripts/run_preprocessing.py
CUDA_VISIBLE_DEVICES="2" python scripts/run_miscnn.py --fold 0
python3 scripts/run_miscnn.py --fold 1
python3 scripts/run_miscnn.py --fold 2
python3 scripts/run_miscnn.py --fold 3
python3 scripts/run_miscnn.py --fold 4
```

Finally, the evaluation script computes all scores, visualizations and figures.

```sh
python3 scripts/run_evaluation.py
```


```

