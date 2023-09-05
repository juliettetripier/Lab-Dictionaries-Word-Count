"""Count words in file."""


# put your code here.
def load_data(filename):
    file = open(filename)
    all_lines = []

    for line in file:  
        each_line = line.rstrip(".?,;:!_-\n").split(" ")

        for word in each_line:
            all_lines.append(word)

    return all_lines

all_lines = load_data("twain.txt")

#print(load_data("test.txt"))

def count_words():
    word_counts = {}
    for word in all_lines:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

print(count_words())

# """Count letters in phrase.
