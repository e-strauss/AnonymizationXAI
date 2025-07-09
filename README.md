<div align="left">
    <div style="display: inline-block;">
        <h2 style="display: inline-block; vertical-align: middle; margin-top: 0;">ANONYMIZATIONXAI</h2>
        <p>
	<em><code>❯ REPLACE-ME</code></em>
</p>
        <p>
	<img src="https://img.shields.io/github/license/e-strauss/AnonymizationXAI?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/e-strauss/AnonymizationXAI?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/e-strauss/AnonymizationXAI?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/e-strauss/AnonymizationXAI?style=default&color=0080ff" alt="repo-language-count">
</p>
        <p><!-- default option, no dependency badges. -->
</p>
        <p>
	<!-- default option, no dependency badges. -->
</p>
    </div>
</div>
<br clear="left"/>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>❯ REPLACE-ME</code>

---

##  Features

<code>❯ REPLACE-ME</code>

---

##  Project Structure

```sh
└── AnonymizationXAI/
    ├── 1_DataCharacteristics
    │   ├── DataAnalysisAnonymisationDictionary.ipynb
    │   ├── DataAnalysisTokensGlobal.ipynb
    │   └── DataExploration.ipynb
    ├── 2_ModelTraining
    │   ├── ExperimentalLocalModelTraining.ipynb
    │   ├── final_distilbert_training.py
    │   ├── new_dataset_creation.py
    │   └── splitting.py
    ├── 3_ExplanationMethods
    │   ├── CustomAdversarialAttackForAnonymisation.ipynb
    │   ├── FeatureImportanceGradient.ipynb
    │   ├── LLMClassification.ipynb
    │   ├── NaturalLanguageExplanations.ipynb
    │   └── textattack_probe.py
    ├── 4_ExplanationResults
    │   ├── LLM_classsification_results.txt
    │   ├── bracketed_words_with_clean_text.csv
    │   ├── eval_df_with_explations.csv
    │   ├── eval_df_with_explations_new.csv
    │   ├── global_analysis_added_tokens_top_1K.csv
    │   ├── global_analysis_removed_tokens_top_1K.csv
    │   └── top-k-words-gradient.csv
    ├── 5_Evaluation
    │   ├── EvaluationGradientBasedImportance.txt
    │   ├── EvaluationGradientFeatureImportance.ipynb
    │   └── FeatureImportanceGradientWithEval.ipynb
    ├── DB-bio
    │   ├── anonymized_text_train.csv
    │   ├── anonymized_text_val.csv
    │   ├── combined_train_and_train_sft_anonymized.jsonl
    │   ├── combined_val_and_val_sft_anonymized.jsonl
    │   ├── test.jsonl
    │   ├── train.jsonl
    │   ├── train_dpo.jsonl
    │   ├── train_sft.jsonl
    │   ├── val.jsonl
    │   ├── val_dpo.jsonl
    │   └── val_sft.jsonl
    └── utils
        ├── explainer.py
        └── read_jsonl.py
```


###  Project Index
<details open>
	<summary><b><code>ANONYMIZATIONXAI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			</table>
		</blockquote>
	</details>
	<details> <!-- 1_DataCharacteristics Submodule -->
		<summary><b>1_DataCharacteristics</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/1_DataCharacteristics/DataAnalysisAnonymisationDictionary.ipynb'>DataAnalysisAnonymisationDictionary.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/1_DataCharacteristics/DataAnalysisTokensGlobal.ipynb'>DataAnalysisTokensGlobal.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/1_DataCharacteristics/DataExploration.ipynb'>DataExploration.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- 3_ExplanationMethods Submodule -->
		<summary><b>3_ExplanationMethods</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/3_ExplanationMethods/FeatureImportanceGradient.ipynb'>FeatureImportanceGradient.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/3_ExplanationMethods/CustomAdversarialAttackForAnonymisation.ipynb'>CustomAdversarialAttackForAnonymisation.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/3_ExplanationMethods/textattack_probe.py'>textattack_probe.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/3_ExplanationMethods/NaturalLanguageExplanations.ipynb'>NaturalLanguageExplanations.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/3_ExplanationMethods/LLMClassification.ipynb'>LLMClassification.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- DB-bio Submodule -->
		<summary><b>DB-bio</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/val_sft.jsonl'>val_sft.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/train.jsonl'>train.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/test.jsonl'>test.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/train_sft.jsonl'>train_sft.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/combined_train_and_train_sft_anonymized.jsonl'>combined_train_and_train_sft_anonymized.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/val_dpo.jsonl'>val_dpo.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/combined_val_and_val_sft_anonymized.jsonl'>combined_val_and_val_sft_anonymized.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/val.jsonl'>val.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/DB-bio/train_dpo.jsonl'>train_dpo.jsonl</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- 5_Evaluation Submodule -->
		<summary><b>5_Evaluation</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/5_Evaluation/FeatureImportanceGradientWithEval.ipynb'>FeatureImportanceGradientWithEval.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/5_Evaluation/EvaluationGradientFeatureImportance.ipynb'>EvaluationGradientFeatureImportance.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/5_Evaluation/EvaluationGradientBasedImportance.txt'>EvaluationGradientBasedImportance.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- utils Submodule -->
		<summary><b>utils</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/utils/explainer.py'>explainer.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/utils/read_jsonl.py'>read_jsonl.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- 4_ExplanationResults Submodule -->
		<summary><b>4_ExplanationResults</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/4_ExplanationResults/LLM_classsification_results.txt'>LLM_classsification_results.txt</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- 2_ModelTraining Submodule -->
		<summary><b>2_ModelTraining</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/2_ModelTraining/splitting.py'>splitting.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/2_ModelTraining/ExperimentalLocalModelTraining.ipynb'>ExperimentalLocalModelTraining.ipynb</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/2_ModelTraining/final_distilbert_training.py'>final_distilbert_training.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/e-strauss/AnonymizationXAI/blob/master/2_ModelTraining/new_dataset_creation.py'>new_dataset_creation.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with AnonymizationXAI, ensure your runtime environment meets the following requirements:

- **Programming Language:** JupyterNotebook


###  Installation

Install AnonymizationXAI using one of the following methods:

**Build from source:**

1. Clone the AnonymizationXAI repository:
```sh
❯ git clone https://github.com/e-strauss/AnonymizationXAI
```

2. Navigate to the project directory:
```sh
❯ cd AnonymizationXAI
```

3. Install the project dependencies:

echo 'INSERT-INSTALL-COMMAND-HERE'



###  Usage
Run AnonymizationXAI using the following command:
echo 'INSERT-RUN-COMMAND-HERE'

###  Testing
Run the test suite using the following command:
echo 'INSERT-TEST-COMMAND-HERE'

---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/e-strauss/AnonymizationXAI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/e-strauss/AnonymizationXAI/issues)**: Submit bugs found or log feature requests for the `AnonymizationXAI` project.
- **💡 [Submit Pull Requests](https://github.com/e-strauss/AnonymizationXAI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/e-strauss/AnonymizationXAI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/e-strauss/AnonymizationXAI/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=e-strauss/AnonymizationXAI">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---