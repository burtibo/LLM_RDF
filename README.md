# README: RDF Triple Understanding with Large Language Models

## Project Overview
This project investigates the ability of large language models (LLMs) to perform link prediction and relation prediction on knowledge graphs without fine-tuning. It compares open-source LLAMA models against GPT-4 using two benchmark datasets: WN18RR and FB15k-237.

## Repository Structure
```
📂 data/            # Contains all datasets and exploratory analysis
📂 survey/          # Preprocessing scripts for survey data
📂 src/             # Core scripts for experiments and automation
    ├── nb_fb15k/  # Code for link prediction & relation prediction tasks for fb15k237 dataset
    ├── nb_wn18rr/  # Code for link prediction & relation prediction tasks for wn18rr dataset
    ├── negative_sampling.py  # Generates negative samples for link prediction
    ├── relation2text_simplify.py  # Clusters FB15k-237 relations for prediction
📂 results/         # Stores results of link and relation prediction tasks
```

## Running the Experiments
To replicate the experiments and generate results, follow these steps:

### Step 1: Generate Negative Samples
Run the negative sampling script for each dataset before proceeding:
```bash
python src/negative_sampling.py --dataset WN18RR
python src/negative_sampling.py --dataset FB15k237
```

### Step 2: Simplify Relations (For FB15k-237 Dataset Only)
For the FB15k-237 dataset, run the clustering script to simplify relations:
```bash
python src/relation2text_simplify.py
```

### Step 3: Execute the Link and Relation Prediction Notebooks
Once preprocessing is complete, execute the notebooks for link and relation prediction. Update the API key and model in the scripts before running:

#### link prediction & relation prediction tasks for fb15k237 dataset:
```bash
jupyter notebook src/nb_fb15k.ipynb
```

#### link prediction & relation prediction tasks for wn18rr dataset:
```bash
jupyter notebook src/nb_wn18rr.ipynb
```

## Automation and Configuration
The scripts are designed to be modular and automated:
- The `src/` folder contains dataset-specific scripts for both tasks.
- Simply changing the API and model settings allows for running the same code with different models.
- Results are automatically saved in the `results/` directory.

## Requirements
- Python 3.8+
- Jupyter Notebook
- Required Python libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

## Citation
If you use this project, please cite:
> Stańczyk, O. (2025). *The Understanding of RDF Triples by Large Language Models: A Comparative Analysis of LLAMA 3 and GPT-4*. Master’s Thesis.

## Contact
For questions or collaborations, feel free to reach out!

