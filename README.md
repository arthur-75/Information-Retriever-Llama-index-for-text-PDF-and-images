# Information Retriever text,PDF and images using LLM

This web application allows users to retrieve text and relevant images based on their queries using LLAMA2 LLM model and CLIP.

<img src="https://github.com/arthur-75/Information-Retriever-Llama-index-for-text-PDF-and-images/blob/main/static/ex.png" width="600" height="600">

## Features

- Retrieve text from PDF, TXT, and other formats.
- Retrieve relevant images based on user queries.
- Simple user interface with a query box.

## Installation and Setup

1. Clone the repository:
git clone https://github.com/arthur-75/Information-Retriever-Llama-index-for-text-PDF-and-images.git
cd Information-Retriever-Llama-index-for-text-PDF-and-images

2. Install dependencies:
pip install -r requirements.txt

3. Ensure you have the necessary files:
- `main.ipynb`
- `app.py`
- `llama_index` package (ensure it's available in your project directory)

4. Create a `qdrant_db` folder for your vector database and ensure the required templates for HTML are in the `templates` folder.

## Usage

1. Run the Flask application in terminal:

python app.py


2. Access the web application by navigating to `http://localhost:5001` in your web browser.

3. Enter your query in the provided box and click submit to retrieve text and images relevant to your query.

## Files and Directories

- `app.py`: Main Flask application file.
- `main.ipynb`: Jupyter Notebook file for main functionalities.
- `llama_index`: Package containing schema, embeddings, vector stores, and other necessary functionalities.
- `qdrant_db`: Folder for vector database.
- `templates`: Folder containing HTML templates for the web application.

## Authors

- [Arthur SATOUF](https://www.linkedin.com/in/arthur-satouf/)

## License

This project is licensed under the [MIT License](LICENSE).
