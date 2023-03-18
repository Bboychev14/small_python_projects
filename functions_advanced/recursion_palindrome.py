def palindrome(text, index):
    if index > len(text) / 2:
        return f"{text} is a palindrome"
    left_letter = text[index]
    right_letter = text[-index - 1]
    if left_letter != right_letter:
        return f"{text} is not a palindrome"

    return palindrome(text, index + 1)
