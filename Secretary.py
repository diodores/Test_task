documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def get_a_name(num_doc):
    """Принимает номер документа и возвращает имя обладателя
    Takes the document number and returns the owner's name
    """

    for document in documents:
        if num_doc in document.values():
            owner = (document["name"])
            return owner
        else:
            return 'Неверный номер'


def get_shelf_number(num_doc):
    """Принимает номер документа и возвращает номер полки на которой он находится
    Takes a document number and returns the number of the shelf it is on
    """

    for shelf_number, list_of_documents in directories.items():
        if num_doc in list_of_documents:
            return shelf_number
    return 'Документа под таким номером нет в архиве'


def get_a_list_of_documents():
    """Выводит список всех документов (Вывод по значению без ключа)
    List of all documents (output by value without a key)
    """

    for document in documents:
        print(document["type"], document["number"], document["name"])


def shelf(num_shelf):
    """Вспомогательная функция проверяет существует ли запрашиваемая полка
    Helper function checks if the requested shelf exists
    """

    for x in directories:
        if num_shelf in x:
            return x
    return 'Нету такой полки'


def add_document():
    """Создает новый перечень документов и добавляет номер документа на выбранную полку
    Creates a new list of documents and adds the document number to the selected shelf
    """

    number_doc = input('Введите номер нового документа: ')
    doc = {}
    a = get_shelf_number(num_doc=number_doc)
    print(a)
    if a == 'Документа под таким номером нет в архиве':
        type_doc = input('Укажите тип документа: ')
        name_doc = input('Введите Имя и Фамилию: ')
        doc["number"] = number_doc
        doc["type"] = type_doc
        doc["name"] = name_doc
        documents.append(doc)
        num_shelf = input('Введите номер полки: ')
        b = shelf(num_shelf=num_shelf)
        if b == 'Нету такой полки':
            print(b)
        else:
            directories[num_shelf].append(number_doc)
            print('Документ добавлен')
    else:
        print(f'Документ под номером {number_doc} уже существует')


def main():
    """Основной модуль программы
    """

    print('Данная программа умеет работать со следующими командами: \n\
    \t"p" – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n\
    \t"s" – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n\
    \t"l"– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"\n\
    \t"a" – add – команда, которая добавит новый документ в каталог и в перечень полок. \n\
    \t"d" – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок.\n\
    \t"m" – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.\n\
    \t"as" - add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.\n\
    \t"stop" - остановка и выход из программы.')

    while True:
        command = input('Введите интерисующую вас команду: ').lower().strip()
        if command == 'stop':
            break
        elif command == 'p':
            num_doc = input('Введите номер запрашиваемого документа: ').strip()
            res = get_a_name(num_doc=num_doc)
            print(res)
        elif command == 's':
            num_doc = input('Введите номер запрашиваемого документа: ').strip()
            res = get_shelf_number(num_doc=num_doc)
            print(f'Полка: №{res}')
        elif command == 'l':
            get_a_list_of_documents()
        elif command == 'a':
            add_document()
        elif command == 'd':
            num_doc = input('Введите номер документа, который необходимо удалить: ').strip()
            del_document(num_doc=num_doc)
        elif command == 'm':
            num_doc = input('введите номер документа который необходимо перенести: ')
            num_shelf = input('Выберите полку куда перенести документ, введите ее номер: ')
            document_transfer(num_doc=num_doc, num_shelf=num_shelf)
        elif command == 'as':
            num_shelf = input('Введите номер полки, для добавления ее в перечень: ')
            add_shelf(num_shelf=num_shelf)


def del_document(num_doc):
    """Удаляет документ из каталога и полок по его номеру
    Removes a document from the catalog and shelves by its number
    """
    res = get_shelf_number(num_doc)
    if res != 'Документа под таким номером нет в архиве':
        for num_shelf, num_docs in directories.items():
            if num_doc in num_docs:
                num_docs.remove(num_doc)
        for i, doc in enumerate(documents):
            if num_doc in doc.values():
                del documents[i]
    else:
        print(res)


def document_transfer(num_doc, num_shelf):
    """Принимает номер документа и полки куда перенести это документ. Переносит.
    Accepts the document number and the shelf where to transfer this document. Moves
    """

    get_document = get_shelf_number(num_doc)
    if get_document == 'Документа под таким номером нет в архиве':
        print('Введен номер несуществующего документа')
    elif get_document != 'Документа под таким номером нет в архиве':
        shelf_ = shelf(num_shelf)
        if shelf_ == 'Нету такой полки':
            print(shelf_)
        elif shelf_ != 'Нету такой полки':
            for x in directories.values():
                for i, num in enumerate(x):
                    if num_doc in num:
                        del x[i]
    directories[num_shelf].append(num_doc)


def add_shelf(num_shelf):
    x = shelf(num_shelf)
    if x == 'Нету такой полки':
        directories[num_shelf] = []
    else:
        print('Запрашиваемая вами полка уже существует, посмотреть содержимое полок, поможет команда: "l"')


if __name__=='__main__':
    main()
