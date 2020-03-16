palindrome_word = 'Malayalam'


def is_palindrome(word):

    left = 0
    right = len(word) - 1
    word = word.lower()

    while left < right:
        if word[left] != word[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


print(is_palindrome(palindrome_word))
