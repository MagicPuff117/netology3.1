

def read_files(name):
    import json
    from pprint import pprint
    with open(name, 'r', encoding='utf8') as f:
        data = f.read()
        data = json.loads(data)
        # pprint(data)
        original_text = ''
        for items in data['rss']['channel']['items']:
            original_text +='' + items['description']
        # pprint(original_text)
        return original_text

# read_files('newsafr.json')

def count_word(original_text):
    list = original_text.split(' ')
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

def read_file(name):
    import xml.etree.ElementTree as ET
    tree = ET.parse(name)
    root = tree.getroot()
    # items = root.findall('channel/item')
    # print(items)
    for news in root.findall('channel/item'):
        return news.find('description').text


# read_file()

def count_word_xml(news):
    list = news.split(' ')
    word_value = {}
    for word in list:
        if len(word) > 6:
            if word in word_value:
                word_value[word] += 1
            else:
                word_value[word] = 1
    return word_value

def top_words_xml(word_value):
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
        j = 'newsafr.json'
        x = 'newsafr.xml'
        name = input('Введите имя файла:')
        if name == 'j':
            print('Идет обработка файла ...')
            top_10 = top_words(count_word(read_files('newsafr.json')))
            for i in top_10.values():
                print(i[1], ': ', i[0])
        elif name == 'x':
            print('Идет обработка файла ...')
            top_10_xml = top_words_xml(count_word_xml(read_file('newsafr.xml')))
            for i in top_10_xml.values():
                print(i[1], ': ', i[0])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')

main()