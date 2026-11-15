items = []

while True:
    print("\n1 — добавить запись")
    print("2 — показать записи")
    print("0 — выйти")
    choice = input("Выберите действие: ").strip()

    if choice == "1":
        name = input("Введите название: ").strip()
        if name:
            items.append(name)
            print("Запись добавлена.")
        else:
            print("Название не может быть пустым.")
    elif choice == "2":
        if items:
            for number, name in enumerate(items, start=1):
                print(number, name)
        else:
            print("Список пока пуст.")
    elif choice == "0":
        break
    else:
        print("Выберите пункт из меню.")
