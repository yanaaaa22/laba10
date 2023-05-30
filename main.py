import json
def zad1():
    with open("1.json", "r", encoding ="utf-8") as f:
        pr = json.load(f)
    for i in pr["products"]:
        print("название ", i["name"])
        print("цена ", i["price"])
        print("вес ", i["weight"])
        print("в наличии" if i["available"] else 'нет в наличии', '\n')



def zad2():
    with open("1.json", "r",encoding ="utf-8") as f:
        pr = json.load(f)
    for i in pr["products"]:
        print("название ", i["name"])
        print("цена ", i["price"])
        print("вес ", i["weight"])
        print("в наличии" if i["available"] else 'нет в наличии', '\n')

    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Продукт в наличии? (да/нет): ").lower() == 'да'

    pr['products'].append({
        'name': name,
        'price': price,
        'weight': weight,
        'available': available
    })

    with open('products.json', 'w') as f:
        json.dump(pr, f)

    with open("products.json", "r") as f:
        pr = json.load(f)
        for i in pr["products"]:
            print("название ", i["name"])
            print("цена ", i["price"])
            print("вес ", i["weight"])
            print("в наличии" if i["available"] else 'нет в наличии', '\n')

def zad3():
    ru_en_dict = {}

    with open('en-ru.txt', 'r',encoding ="utf-8") as f:
        data = f.readlines()

    for line in data:
        words = line.strip().split(' - ')
        words.reverse()
        reversed_words = words[0].split(', ')

        reversed_words.reverse()
        print(reversed_words)
        for word in reversed_words:
            if word in ru_en_dict:
                ru_en_dict[word] += ', ' + words[0]
            else:
                ru_en_dict[word] = words[-1]
    with open('ru-en.txt', 'w', encoding="utf-8") as f:
        for word, translation in sorted(ru_en_dict.items()):
            f.write(f"{word} - {translation}\n")


zad3()