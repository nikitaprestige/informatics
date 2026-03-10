# объем дискеты
disk_size_mb = 1.44

# параметры книги
pages = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# перевод объема дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# количество символов в одной книге
total_chars_per_book = pages * lines_per_page * chars_per_line

# объем одной книги
book_size_bytes = total_chars_per_book * bytes_per_char

# количество книг
number_of_books = int(disk_size_bytes // book_size_bytes)

print("Количество книг, помещающихся на дискету:", number_of_books)