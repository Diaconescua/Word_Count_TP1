# fonction qui divise la phrase en mots, puis returne le nombre de mots
def word_count(str):
    return len(str.split())


words = input("write: ")
# je print le nombre de mots
print("You just wrote", word_count(words), "words.")