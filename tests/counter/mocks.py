def count_word_ocurrences(path, word):
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.count(word)
    return word_count
