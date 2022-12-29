"""
    Write a function that takes in a string of one or more words, and returns the same string,
    but with all five or more letter words reversed (Just like the name of this Kata). 
    Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

    Examples:

    spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
    spinWords( "This is a test") => returns "This is a test" 
    spinWords( "This is another test" )=> returns "This is rehtona test"
"""

def spin_words(sentence: str) -> str:
    sentence_by_words: list[str] = sentence.split(" ")
    res: str = " ".join(list(map(reverse_if_too_long, sentence_by_words)))
    return res

def reverse_if_too_long(word: str) -> str:
    if len(word) >= 5:
        word = word[::-1]
    return word