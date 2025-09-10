##  Overview

This repository contains the code for the project When Text Anonymization Meets Explainability, organized by the Quality and Usability Lab, TU Berlin. The project was carried out by Elias Strauss, Yoana Tsoneva, Erik Kellenter and Seungcheon Lee.
---



##  Project Structure

- **`ModelTraining/`** – scripts for preprocessing the dataset, creating train/test/validation splits, and training the DistilBERT model.  
- **`ExplanationMethods/`** – implementations of the explainability methods used in the project.  
- **`ExplanationResults/`** – stored outputs and results from the explainability methods.  
- **`Evaluation/`** – scripts for evaluating the explainability methods.  
- **`Survey/`** – files related to the user study conducted in this project.
- **`DB-bio/`** - the original DB-bio dataset.


##  Getting Started

###  Prerequisites

Before getting started with AnonymizationXAI, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python3.10


###  Installation

Install AnonymizationXAI using one of the following methods:

**Build from source:**

1. Clone the AnonymizationXAI repository:
```sh
git clone https://github.com/e-strauss/AnonymizationXAI
```

2. Navigate to the project directory:
```sh
cd AnonymizationXAI
```

3. Install the project dependencies:

```sh
python -m venv .venv 
source .venv/bin/activate
pip install -r requirements.txt
```

---


##  Acknowledgments

- We are grateful to Qianli Wang and Dr. Nils Feldhus for their valuable guidance and support throughout this project.  

---
