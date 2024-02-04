import tkinter as tk
from bs4 import BeautifulSoup
import requests
import re
import nltk
import heapq

nltk.download('stopwords')
nltk.download('punkt')

article_text = ""

def generate_summary():
    global article_text
    clean_text = re.sub('[^a-zA-Z]', ' ', article_text.lower())
    clean_text = re.sub('\s+', ' ', clean_text)
    sentence_list = nltk.sent_tokenize(article_text)

    stopwords = nltk.corpus.stopwords.words('english')
    word_frequencies = {}
    for word in nltk.word_tokenize(clean_text):
        if word not in stopwords:
            if word not in word_frequencies:
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequency = max(word_frequencies.values())
    for word in word_frequencies:
        word_frequencies[word] = word_frequencies[word] / maximum_frequency

    sentence_scores = {}
    for sentence in sentence_list:
        for word in nltk.word_tokenize(sentence):
            if word in word_frequencies and len(sentence.split(' ')) < 30:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

    summary = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
    summary_text.delete("1.0", "end")
    summary_text.insert(tk.END, " ".join(summary))
    window.title("Summarized Article")

def get_article_content(article_link):
    try:
        response = requests.get(article_link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            article_content = soup.get_text()
            return article_content
        else:
            print(f"Error: Unable to fetch content. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_input():
    global article_text
    article_link = link_input.get("1.0", "end-1c").replace("\n", " ")
    article_text = get_article_content(article_link)
    generate_summary()

window = tk.Tk()
window.title("Article Summarizer")

link_input = tk.Text(window, height=2, width=70)
link_input.pack()
summarize_button = tk.Button(window, text="Summarize", command=get_input)
summarize_button.pack()

summary_text = tk.Text(window, height=15, width=70)
summary_text.pack()

window.mainloop()

