def main(file):
    book_report = generate_book_report(file)
    for line in book_report:
        print(line)

def generate_book_report(book):
    report = []
    book_contents = read_book(book)
    report.append(f'--- Begin report of {book} ---')

    word_count = count_words(book_contents)
    report.append(f'{word_count} words found in the document')
    report.append('')

    letter_count = count_letters(book_contents)
    letters_found = list(letter_count)
    letters_found.sort()
    for character in letters_found:
        count = letter_count[character]
        report.append(f"The '{character}' character was found {count} times")

    report.append('--- End report ---')
    return report

def read_book(book):
    with open(book) as f:
        return f.read()

def count_words(book_contents):
    words = book_contents.split()
    return len(words)

def count_letters(book_contents):
    letter_counts = dict()
    contents_without_whitespace = ''.join(book_contents.split())
    sanitized_contents = contents_without_whitespace.lower()

    for character in sanitized_contents:
        if character.isalpha():
            letter_counts[character] = letter_counts.get(character, 0) + 1

    return letter_counts

main('books/frankenstein.txt')