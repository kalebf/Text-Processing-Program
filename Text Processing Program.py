
def word_count(text): #splits text into list of words and then counts the tokens in list
    words = text.split()
    numwords = len(words)
    return numwords

def find_longest_word(text): #splits text into list of words and compares to them to assign longest word
    words = text.split()
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
        

def count_substring(text, substring): #Uses user input subtring to count its occurances in the text input
    occurances = text.count(substring)
    return occurances

def extract_unique_words(text): #splits text into list of words, checks each word in the list and adds it to a new list of unique words if it does not repeat. 
    words = text.split()
    unique_words_set = []
    repeated_words = set()
    for word in words:
        if word not in repeated_words:
            unique_words_set.append(word)
            repeated_words.add(word)
    
    words_list = list(unique_words_set)
    return words_list




def main():
    print('Welcome to the Text Processing Program!\n')
    text = input('Enter a text: ')
    print()
    print(f'Original Text:\n{text}\n')

    task = 0
    
    while task != 5:
        print('1. Word Count\n2. Longest Word\n3. Count of Substring\n4. Unique Words\n5. Exit')
        task = int(input('Enter the number of the analysis option (1-5): '))
        
        if task == 1:
            print()
            print(f'Word Count: {word_count(text)}\n')
        elif task == 2:
            print()
            print(f'Longest Word: {find_longest_word(text)}\n')
        elif task == 3:
            substring = input('Enter a subtring to count: ')
            print(f'Count of subtring \'{substring}\': {count_substring(text, substring)}\n')
        elif task == 4:
            print()
            print(f'Unique words: {extract_unique_words(text)}\n')
        else:
            print()
            print('Thank you for using the Text Processing Program!',end ='')
    return ''
print(main())
    




    


