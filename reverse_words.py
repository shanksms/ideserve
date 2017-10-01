#write code


def reverse_words(input_words):
    word_list = input_words.split(' ')
    word_list.reverse()
    print(" ".join(word_list))

if __name__ == '__main__':
    reverse_words(input())
