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
        chains[key].append(words[i+2])
    return chains

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    #creates empty list
    words = []
    #picks random key and stores in variable
    current_key = choice(chains.keys())
    #unpacks tuple and moves each word of the key into words list
    for item in current_key:
        words.append(item)
    #concatenates strings into one string and stores in variable
    text = words[0] + " " + words[1]
    #using current key, we call list of values. Choice randomly chooses 
    #one value and stores in value as string
    chosen_word = choice(chains[current_key])
    #concatenate chosen word to text (string)
    text += " " + chosen_word

    while True: 
        #creates new key(tuple) with the second word in current_key
        #and chosen word
        new_key = (current_key[1], chosen_word)
        #if the new_key is the last two words of all the words in the
        #file, break from the loop
        if chains.get(new_key) == None:
            break
        #use new key to call values and randomly choose one and store 
        #the randomly chosen value in chosen_word    
        chosen_word = choice(chains[new_key])
        #updates current_key with the contents of new_content
        current_key = new_key
        #adds the chosen_word to the string text
        text += " " + chosen_word

    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
