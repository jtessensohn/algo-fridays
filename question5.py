
def valid_anagram():
    word1 = input(str("First word: "))
    word2 = input(str("Second word: "))
    if(sorted(word1) == sorted(word2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

valid_anagram()