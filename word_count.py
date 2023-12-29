search_words = ["python", "c", "oop", "hello", "java"]


for word in search_words:
    file_path = open("input.txt", "r")
    content = file_path.read().lower()
    word_count = {word: content.count(word)}
    for word, count in word_count.items():
        print(f"'{word}' in 'input.txt': {count}")

file_path.close()
