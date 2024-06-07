import random


def load_text():
    with open("the_little_prince.txt", "r") as file:
        return file.readlines()


def clear_text(text):
    return ' '.join([line.strip().lower() for line in text if line.strip()])


def tokenize(text):
    for char in text:
        if char in ["!", "?", "'", ".", ",", ":", ";", "”", "“"]:
            text = text.replace(char, '')
    return text.split()


def creating_dictionary(tokens):
    word_dictionary = {}
    for i in range(len(tokens) - 1):
        current_word = tokens[i]
        next_word = tokens[i + 1]
        if current_word not in word_dictionary:
            word_dictionary[current_word] = [next_word]
        else:
            word_dictionary[current_word].append(next_word)
    return word_dictionary


def markov_chain(word_dictionary):
    first_word = random.choice(list(word_dictionary.keys()))
    generated_text = [first_word.capitalize()]
    for i in range(199):
        next_words = word_dictionary[first_word]
        first_word = random.choice(next_words)
        generated_text.append(first_word)
    return ' '.join(generated_text)


def main():
    text = load_text()
    cleared_text = clear_text(text)
    tokenized = tokenize(cleared_text)
    word_dictionary = creating_dictionary(tokenized)
    print(markov_chain(word_dictionary))


main()