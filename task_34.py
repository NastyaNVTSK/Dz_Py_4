def check_rhythm(poem):
    lines = poem.split(" ")

    def count_vowels(word):
        vowels = "аеёиоуыэюя"
        return sum(1 for letter in word if letter.lower() in vowels)

    return "Парам пам-пам" if all(count_vowels(line) == count_vowels(lines[0]) for line in lines) else "Пам парам"

poem = input("Введите стихотворение, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами: ")
result = check_rhythm(poem)
print(result)