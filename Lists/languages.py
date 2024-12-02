languages = ["lingala", "french", "german", "english", "swedish", "korean", "spanish", "portuguese", "mandarin"]
print(languages)

print(languages[4])
print(languages[-2])

print(languages[1].title())

message = "My first language is " + languages[3].title() + "."
print(message)

languages[0] = "kikongo"
print(languages)

languages.append("lingala")
print(languages)

languages.insert(3, "swiss german")
print(languages)

del languages[3]
print(languages)

popped_languages = languages.pop(-1)
print(languages)
print(popped_languages)

hard = languages.pop(-1)
message = hard.upper() + " is the most difficult language to learn."
print(message)

print(languages)
languages.remove('portuguese')

print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

print(sorted(languages))

print(sorted(languages, reverse=True))
print(languages)

languages.reverse()
print(languages)

print(len(languages))