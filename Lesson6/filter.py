palindrome = ["шалаш", "шабаш", "стул", "кухня", "довод", "обезьяна"]


def reverse(palindrome):
    for i in palindrome:
        if i in palindrome == palindrome[::-1]:
            return i
        else:
            return None


print(tuple(filter(reverse, palindrome)))
