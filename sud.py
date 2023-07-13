import tkinter as tk
from tkinter import messagebox
import spacy


def summarize_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    sentences = [sent.text for sent in doc.sents]
    summary = " ".join(sentences[:3])  # Summarize the first 3 sentences

    return summary


def extract_topic(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)

    # Extract the most relevant noun phrase as the topic
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    topic = max(noun_phrases, key=len)

    return topic


def process_text():
    text = input_text.get("1.0", tk.END).strip()

    if text:
        summary = summarize_text(text)
        topic = extract_topic(text)

        messagebox.showinfo("Summary", summary)
        messagebox.showinfo("Topic", topic)
    else:
        messagebox.showwarning("Input Error", "Please enter some text!")


# Create a Tkinter GUI
root = tk.Tk()
root.title("Text Summarizer and Topic Extractor")

# Create an input text box
input_text = tk.Text(root, height=20, width=80)
input_text.pack()

# Create a button to process the text
process_button = tk.Button(root, text="Process Text", command=process_text)
process_button.pack()

root.mainloop()
