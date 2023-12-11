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
        return
        
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
    # Remove punctuation from the text
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = cleaned_text.split()

    # Return the count of words
    return len(words)


def calculate_unique_word_count(text):
    words = text.split()
    unique_words = set(words)
    return len(unique_words)


def calculate_word_frequency(text):
    word_frequency = {}
    # Remove punctuation from the text
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

    # Split the text into words
    words = cleaned_text.split()

    # Calculate word frequency
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency





if __name__ == '__main__':
    main()