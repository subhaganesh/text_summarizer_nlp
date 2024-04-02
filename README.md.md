

![App Screenshot](https://krvia.ac.in/wp-content/uploads/2021/02/Essential-Books.jpg)


 # Text summarizer For Conversation 

The Text Summarization for conversation is a sophisticated tool designed to extract key insights from chat conversations quickly and efficiently. With the aim of enabling users to grasp the main idea of a conversation without reading through the entire transcript, this project leverages cutting-edge natural language processing (NLP) techniques.


## Key Features:

* **Efficient Summarization:** Condense lengthy chat conversations into concise summaries, facilitating rapid understanding of the main points and key insights.

* **Powered by Distilled PEGASUS Model:** The summarizer is trained using a distilled PEGASUS model, renowned for its ability to generate high-quality abstractive summaries.

* **Pre-trained Model:** Utilizes a pre-trained model on the Samsum dataset, which contains conversations between two or more people, ensuring accurate summarization of multi-party discussions.

* **Modular Coding for Easy Deployment:** Designed with modular coding principles, enabling seamless deployment and integration into various applications. The project structure ensures ease of maintenance and facilitates integration into CI/CD pipelines for automated testing and deployment.

## Usage:
* **Input:** Provide the chat conversation you wish to summarize.

* **Output:** Receive a succinct summary capturing the essence of the conversation, allowing for quick comprehension and analysis.







## Installation:

Look for a file named README.md in the repository. This file usually contains instructions on how to install and use the project. Read through it to find installation instructions specific to the project.


### 1. Navigate to the Project Directory: 

 Change your current directory to the project directory using   the  cd command.

     cd repository

### 2. Clone the Repository: 

* Open your terminal or command prompt.
* Use the git clone command followed by the URL of the GitHub repository to clone the repository to your local machine.

      git clone https://github.com/subhaganesh/text_summarizer_nlp.git

### 3. Set Up virtual Environment (if necessary): ###

Some projects require virtual environment variables to be set up. Through this we can update our required packages for installation.
     

### 4. Install Dependencies (if any): ###

Check if the project has any dependencies that need to be installed.
If the project uses a package manager like  pip (for Python projects), you can install dependencies using the appropriate command. For example:

     pip install -r requirements.txt    # for pip

###  5. Run the Project:

Once everything is set up, you can run the project using the appropriate command.
For example, if it's a web application using streamlit, you might run:

     streamlit run app.py    # for Python








## Packages Required:

* transformers
* transformers[sentencepiece]
* datasets
* sacrebleu 
* rouge_score 
* py7zr
* pandas
* nltk
* tqdm
* PyYAML
* matplotlib
* torch
* notebook
* boto3
* mypy-boto3-s3
* python-box==6.0.2
* ensure==1.0.2
* fastapi==0.78.0
* uvicorn==0.18.3
* Jinja2==3.1.2
* streamlit


## Roadmap:

* setup.py
* template.py 

__workflows:__

1. update config.yaml

2. update params.yaml

3. update entity

4. update the configuration manager in src config

5. update the components
6. data ingestion
7. data validation
8. data transformation
9. model training
10. model evaluation
11. prediction pipeline
12. update the pipeline
13. update the main.py
14. update app.py


## Deployment:

To deploy this project run

```python
  streamlit run app.py
```


## Acknowledgements:

 - [Krish naik](https://www.linkedin.com/in/naikkrish/)

 - [Boktiar Ahmed Bappy](https://www.linkedin.com/in/boktiarahmed73/)

 - [Awesome README](https://github.com/matiassingers/awesome-readme)



## Authors:

- [Subhaganesh](https://github.com/subhaganesh)

