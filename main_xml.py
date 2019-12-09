# import xml.etree.ElementTree as ET
# tree = ET.parse(r'newsafr.xml')
# root = tree.getroot()
# # print(root.attrib)

# title = root.findall('channel/item/description')



def read_file(name):
    import xml.etree.ElementTree as ET
    tree = ET.parse(name)
    root = tree.getroot()
    items = root.findall('channel/item')
    # print(items)
    for news in items:
        return news.find('description').text


# read_file()

def count_word(news):
    list = news.split(' ')
    word_value = {}
    for word in list:
        if len(word) > 6:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value

def top_words(word_value):
    l = lambda word_value: word_value[1]
    sort_list = sorted(word_value.items(), key= l, reverse=True)
    count = 1
    top_10 = {}
    for word in sort_list:
        top_10[count] = word
        count += 1
        if count == 10:
            break
    return top_10

def main():
    while True:
        name = input('Введите имя файла:')
        if name == 'newsafr.xml':
            print('Идет обработка файла ...')
            # read_file(name)
            top_10 = top_words(count_word(read_file(name)))
            for i in top_10.values():
                print(i[1], ': ', i[0])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')

main()