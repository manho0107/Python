ori_word = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_word = list()

for word in ori_word:
    if len(word) >= 1:
        newword = new_word.append(word)

print(new_word)