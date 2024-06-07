# Simple Text Generation Task

during this task you will be coding a fun little task
from my field, natural language processing. you will be
implementing a simple traditional model called markov
chain model for the task of text generation.

**task description:**

**1.** Choose a book that you like (Keep it under 3mb)
  *1.* Download the book in .txt format
**2.** Create a python file. In it:
  *1.* Open the book file
  *2.* (optional) Clean the text file, e. g. lowercase
  everything etc.
  *3.* split the text into a list of its tokens (i. e.
  words and punctuation). You may use native python
  methods or consult other libraries
  *4.* Create a dictionary object, where:
    *1.* the keys are the unique tokens
    *2.* the values are lists of the next following
    words that occur after the key token (1 next
    word for every occurrence)
  *5.* Generate text. Make it so that:
    *1.* the program chooses the first word randomly
    from the keys and prints it (you can use  random
    library for this)
    *2.* then it consults the occurrence list from the
    dictionary you created to randomly choose the
    next word to print out (you can use  random
    library for this)
    *3.* repeat 5.2 200 times
