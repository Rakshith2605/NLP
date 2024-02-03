 [TRY THE CODE HERE](https://colab.research.google.com/drive/1RmfBPra0td3G_1MtCXNBED0DeQ28u0Hq?usp=sharing) 

This code is a simple text summarization tool using a frequency-based approach. Let's break it down:

1. **Text Processing:**
   - The script first imports the necessary libraries, such as Tkinter for the GUI, regular expressions (re) for text cleaning, and NLTK for natural language processing.

2. **Global Variables:**
   - The global variable `article_text` is initialized to store the input text.

3. **Text Summarization Function (`generate_summary`):**
   * This function removes whitespace and non-alphanumeric characters from the article text.
   * As a next step, it breaks the cleaned text down into words and phrases using tokenization.
   * Scores sentences according to word frequencies after calculating and normalizing them.
   * Uses the five most highly rated sentences to create the summary.
   * The function sets the title of the window and updates the Tkinter text widget with the created summary.

4. **Input Handling Function (`get_input`):**
   - Retrieves the input article text from the Tkinter text widget.
   - Calls the `generate_summary` function to generate and display the summary.

5. **GUI Setup (`tkinter` Window):**
   - Creates a Tkinter window with a specified size.
   - Includes a text widget for input and a button to trigger the summarization process.

6. **Example Usage:**
   - User pastes or types an article into the provided text box.
   - Clicks the `Summarize` button.
   - The script processes the input, analyzes word frequencies, scores sentences, and displays a concise summary in the text box.

**Key Points:**
   - The summarization is based on the frequency of words, giving importance to words occurring more frequently.
   - It's a straightforward tool that provides a quick summary of the input text.
   - The GUI allows for a user-friendly interaction.

This script is a basic introduction to text summarization and can be enhanced with more advanced techniques for better accuracy and effectiveness.
