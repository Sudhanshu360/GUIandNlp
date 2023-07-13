# Project Name

Text Summarization and Topic Assignment with GUI

## Description

This Python project utilizes the power of natural language processing and graphical user interface to summarize a given text and assign a relevant topic to it. The project leverages the Spacy library for text processing tasks and Tkinter for creating an interactive GUI.

The program accepts input in the form of text, which can be a document, an article, or any other textual content. The main objectives of the project are to generate a concise summary of the text and determine its primary topic.

Spacy, a widely used natural language processing library, is employed to analyze and process the input text. It performs tasks such as tokenization, part-of-speech tagging, and named entity recognition. These techniques help break down the text into its constituent parts and analyze their grammatical structure and meaning.

Once the text has been processed, the program applies a summarization algorithm to extract the most important information and condense it into a shorter summary. The specific summarization algorithm used in the project may be based on extractive or abstractive methods, or a combination of both. The goal is to capture the essence of the text while reducing its length.

In addition to summarization, the program utilizes Spacy's capabilities to assign a topic to the text. By analyzing the processed text and considering factors such as word frequency and the presence of specific entities, the program attempts to determine the main subject or theme of the text.

To enhance user experience, the project incorporates Tkinter, a standard GUI toolkit, to display the output. Tkinter provides a range of tools and widgets for building GUI elements such as windows, frames, buttons, and labels. These elements are utilized to present the summarized text and the assigned topic in an interactive and visually appealing manner.

## Features

- Accepts text input and processes it using Spacy's natural language processing capabilities.
- Applies a summarization algorithm to generate a concise summary of the input text.
- Utilizes Spacy's functionality to assign a relevant topic to the text.
- Creates an interactive GUI using Tkinter to display the summarized text and assigned topic.
- Provides a user-friendly interface for inputting text and viewing the output.

## Installation

1. Clone the repository: `git clone https://github.com/your_username/your_project.git`
2. Navigate to the project directory: `cd your_project`
3. Install the required dependencies: `pip install spacy tkinter` (ensure Spacy is properly installed and has downloaded the necessary language models)
4. Run the main program: `python main.py`

## Usage

1. Launch the application by running `main.py`.
2. Enter the text you want to summarize and assign a topic to.
3. Click the "Summarize" button to generate the summary and topic.
4. The summarized text and assigned topic will be displayed in the GUI.
5. Repeat the process with different text inputs as needed.

## Contributing

Contributions to this project are welcome. If you find any bugs or have suggestions for improvements, please open an issue on the project repository. Feel free to fork the repository and submit pull requests to contribute code changes.

LICENSE
GNU General Public License v3.0

