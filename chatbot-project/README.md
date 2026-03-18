# AI Chatbot using Endee

## Overview

This project is a simple AI-powered chatbot built using **semantic search**.
It retrieves the most relevant answer from a dataset by understanding the meaning of the user’s query rather than matching exact keywords.

##  How It Works

* Text data is converted into **vector embeddings** using Sentence Transformers
* User queries are also converted into embeddings
* Similarity is computed using **dot product**
* The most relevant response is returned

##  Features

* Interactive command-line chatbot
* Semantic search (context-based answers)
* Fast and lightweight implementation
* Easy to extend with custom data

## Tech Stack

* Python
* Sentence Transformers
* NumPy
* Endee (conceptual vector database integration)

## Project Structure

endee/
│── chatbot-project/
│   ├── app.py
│   ├── data.txt
│   └── venv/
│
└── README.md


## How to Run

### 1. Clone the repository

git clone https://github.com/Basavarah1611/endee.git

### 2. Navigate to project

cd endee/chatbot-project

### 3. Create virtual environment

python -m venv venv
venv\Scripts\activate

### 4. Install dependencies

pip install sentence-transformers numpy streamlit

### 5. Run the chatbot

python app.py

## Sample Queries

* What is Python?
* Explain AI
* What is Machine Learning?

## Note

Endee is used as a **vector database conceptually**, where embeddings are stored and retrieved for semantic search.


## Future Improvements

* Add Streamlit UI for better user interaction
* Integrate with a real vector database
* Use advanced LLMs for dynamic response generation


## Author
BASAVARAJ HATTI

---

