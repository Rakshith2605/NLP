import tkinter as tk
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
    article_input.delete("1.0", "end")
    article_input.insert(tk.END, " ".join(summary))
    window.title("Summarized Article")

def get_input():
    global article_text
    article_text = article_input.get("1.0", "end-1c").replace("\n", " ")
    generate_summary()

window = tk.Tk()
window.title("Paste Your Article to Summarise")
window.geometry("1000x600")  

article_input = tk.Text(window, height=15, width=70)  
article_input.pack()
summarize_button = tk.Button(window, text="Summarize", command=get_input)
summarize_button.pack()

window.mainloop()
