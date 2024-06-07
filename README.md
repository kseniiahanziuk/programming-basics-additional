# Simple Text Generation Task

during this task you will be coding a fun little task
from my field, natural language processing. you will be
implementing a simple traditional model called markov
chain model for the task of text generation.  

**task description:**  

- Choose a book that you like (Keep it under 3mb)  
  - Download the book in .txt format  
- Create a python file. In it:  
  - Open the book file  
  - (optional) Clean the text file, e. g. lowercase
  everything etc.  
  - Split the text into a list of its tokens (i. e.
  words and punctuation). You may use native python
  methods or consult other libraries  
  - Create a dictionary object, where:  
    - the keys are the unique tokens  
    - the values are lists of the next following 
    words that occur after the key token (1 next
    word for every occurrence)  
  - Generate text. Make it so that:  
    - the program chooses the first word randomly
    from the keys and prints it (you can use  random
    library for this)  
    - then it consults the occurrence list from the
    dictionary you created to randomly choose the
    next word to print out (you can use  random
    library for this)  
    - repeat 5.2 200 times  
