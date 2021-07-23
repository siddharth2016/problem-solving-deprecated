def rec_sum(n):
    if n>0:
        return n + rec_sum(n-1)
    return 0

print(rec_sum(5))

def digit_sum(n):
    if n>0:
        return n%10 + digit_sum(n//10)
    return 0

print(digit_sum(4321))

def word_split(phrase, list_words, output=None):
    
    if output == None:
        output = []
        
    for word in list_words:
        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_words, output)
    return output

print(word_split("themanran", ["the", "ran", "man"]))
print(word_split("themanran", ["clown", "ran", "man"]))