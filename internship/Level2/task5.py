#File Manipulation(word count)

def countWords(file):
    word_count = {}
    try:
        with open(file, "r") as process:
            text = process.read().lower()

        for char in ".,!?;:\"()[]{}":
            text = text.replace(char, "")

        words = text.split()

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        print("\nWord Occurrences (Alphabetical Order):\n")
        for word in sorted(word_count):
            print(f"{word} : {word_count[word]}")

    except FileNotFoundError:
        print("❌ File not found.")


filename = input("Enter file name: ")

countWords(filename)