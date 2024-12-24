items = ['Привет', 'Здарова', 'Здравствуйте', 'hello']

while True:
    print("\nМеню:")
    print("1. Показать список")
    print("2. Добавить элемент")
    print("3. Удалить элемент")
    print("4. Изменить элемент")
    print("5. Выход")

    choice = input("выбери действие (1-5): ")
    if choice == "1":
        print(items)
    elif choice == "2":
        add_elem = input("введите что вы хотите добавить в список: ")
        items.append(add_elem)
        print(items)
    elif choice == "3":
        remove_elem = int(input("введите индекс элемента для удаления: "))
        items.pop(remove_elem)
        print(items)
    elif choice == "4":
        remove_elem = int(input("введите индекс элемента для замены: "))
        replace_elem = input("введите что вы хотите добавить в замен на прошлый элемент списка: ")
        items.pop(remove_elem)
        items.insert(remove_elem, replace_elem)
        print(items)
    elif choice == "5":
        break




