

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

def main():
    while True:
        name = input('Введите имя файла:')
        if name == 'newsafr.json':
            print('Идет обработка файла ...')
            top_10 = top_words(count_word(read_files(name)))
            for i in top_10.values():
                print(i[1], ': ', i[0])
        elif name == 'exit':
            break
        else:
            print('Некорректный ввод, повторите.')

main()