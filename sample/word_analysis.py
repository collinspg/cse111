import string

def main():
    filename = 'story.txt'
    
    try:
        text = read_file(filename)
    except FileNotFoundError:
        print(f"Error: missing file\n[Errno 2] No such file or directory: '{filename}' ")
        return
    except PermissionError:
        print(f"Error: Permission denied. Please check file permissions.")
        
    total_word_count = calculate_word_count(text)
    print(f'Total Word Count: {total_word_count}')
    
    unique_word_count = calculate_unique_word_count(text)
    print(f'Unique Word Count: {unique_word_count}')
    
    word_frequency = calculate_word_frequency(text)
    print('Word Frequency:')
    for word, frequency in word_frequency.items():
        print(f'{word}: {frequency}')
        
        
def read_file(filename):
    try:
        with open(filename, 'rt') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied for file '{filename}'.")
    
def calculate_word_count(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return len(words)

def calculate_unique_word_count(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)

def calculate_word_frequency(text):
    word_frequency = {}
    words = text.split()
    for word in words:
        word = word.strip(",.")
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency



if __name__ == '__main__':
    main()