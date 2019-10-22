def count_vowels(passage):
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  return len([i for i in passage if i in vowels])


print(count_vowels("Hello my name is Adam, and I am 25 years of age"))
