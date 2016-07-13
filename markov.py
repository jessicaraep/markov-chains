from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    corpus = open(file_path).read()
    return corpus



def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    # chains = {}
    # words = text_string.split()

    # for word in words:
    #     chains[(words[i], words[i+1])] = [words[i+2]]
    # return chains

    # create an empty dictionary
    chains = {}
    # going through file and spliting every word into diff.objects
    words = text_string.split()

    # use iterate to go over every index but stop two words before the end
    for i in range(len(words)-2):
        # pass our key(tuple) to a variable key
        key = (words[i], words[i+1]) 
        # iterate over every key(tuple) and using .get function to see if the key exists,
        # re-assign the key and use .get function to go over every key, if it does exist,
        # return the key if it doesn't exist return an empty list.
        chains[key] = chains.get(key, [])
        # if key in chains appendto its value.
        chains[key].append(words[i+2])
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    # your code goes here

    return text


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
