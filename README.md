 [TRY THE CODE HERE](https://colab.research.google.com/drive/1RmfBPra0td3G_1MtCXNBED0DeQ28u0Hq?usp=sharing) 

This code is a simple text summarization tool using a frequency-based approach. Let's break it down:

1. **Text Processing:**
   - The script first imports the necessary libraries, such as Tkinter for the GUI, regular expressions (re) for text cleaning, and NLTK for natural language processing.

2. **Global Variables:**
   - The global variable `article_text` is initialized to store the input text.

3. **Text Summarization Function (`generate_summary`):**
   - Using this function, whitespace and characters that are not comprised of alphabetic characters are removed from the article text.
   - The cleaned text is then tokenized, which is the following step in the process, which breaks the text down into individual words and phrases.
   - After calculating and normalizing the sentences, it assigns a score based on the frequency of the words in the sentences.
   - When creating the summary, it makes use of the five sentences that received the highest ratings.
   - This function is responsible for setting the title of the window and updating the Tkinter text widget with the summary that was prepared.


5. **Input Handling Function (`get_input`):**
   - Retrieves the input article text from the Tkinter text widget.
   - Calls the `generate_summary` function to generate and display the summary.

6. **GUI Setup (`tkinter` Window):**
   - Creates a Tkinter window with a specified size.
   - Includes a text widget for input and a button to trigger the summarization process.

7. **Example Usage:**
   - User pastes or types an article into the provided text box.
   - Clicks the `Summarize` button.
   - The script processes the input, analyzes word frequencies, scores sentences, and displays a concise summary in the text box.

**Key Points:**
   - Summarization is based on word frequency, with more frequently occurring words given more weight.
   - It's an easy-to-use tool that summarises the entered text quickly.
   - An interface that is easy to use is provided by the GUI.


This script is a fundamental introduction to the process of text summarization, and it has the potential to be improved with more complex techniques in order to achieve more precision and efficiency.

