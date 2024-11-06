def count_letters (text):
    letters_dict={
        "а": 0,
        "б": 0,
        "в": 0,
        "г": 0,
        "д": 0,
        "е": 0,
        "ё": 0,
        "ж": 0,
        "з": 0,
        "и": 0,
        "й": 0,
        "к": 0,
        "л": 0,
        "м": 0,
        "н": 0,
        "о": 0,
        "п": 0,
        "р": 0,
        "с": 0,
        "т": 0,
        "у": 0,
        "ф": 0,
        "х": 0,
        "ц": 0,
        "ч": 0,
        "ш": 0,
        "щ": 0,
        "ъ": 0,
        "ы": 0,
        "ь": 0,
        "э": 0,
        "ю": 0,
        "я": 0,
    }
    text = text.lower()
    for letter in text:
        if letter.isalpha():
            letters_dict [letter] = letters_dict.get(letter) + 1
    return letters_dict


def calculate_frequency(letter_dict):
    counter = 0
    letters_list = letter_dict.values()
    for num in (letters_list):
        counter += num
    freq = []
    for num in (letters_list):
        freq.append((round(num/counter,2)))
    i=0
    for letters in letter_dict:
        letter_dict[letters] =  freq[i]
        i +=1
    return letter_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,!
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

for item in calculate_frequency(count_letters(main_str)).items():
    print(f"{item[0]}: {item[1]}")