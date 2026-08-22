# ! String operation - строки тоже можно складывать, добавлять какой-то контент
# ! между двумя строками. Но однако есть пару забавный вещей:
multipleString_01 = 3 * 'abc'               # ? 'abcabcabc'
multipleString_02 = "a1b2" * 4              # ? 'a1b2a1b2a1b2a1b2'
multipleString_03 = ('ab' * 2) + ('1213')   # ? 'abab1213'

# ! Также к любому символу через индекс мы можем обратиться
txt = 'abcde' # ?, где txt[1] => b, где txt[-1] выведет 'e'
# ! Мы можем также узнать длину строки
txt = 'abc'
print(len(txt)) #? 3

# ? Другие полезные фичи работы со строками

# ! \"...\" - Позволяет добавлять кавычки между словами
escapeDoubleQuote_1 = "Hi \"Python\" "
escapeDoubleQuote_2 = 'Hi "Python"'
# ! \\ - Позволяет добавить \ (backslash)
useRealBackslash = "Path: С:\\Users\\mulwo"
# ! \n - Добавляет новую строку, где 1n - это добав одной строки
addNewLine = "Message1\n\nMessage2\n"
# ! \t - Добавляет пробел
addTab = "Valera\tвыйди\tв\tокно"

print(escapeDoubleQuote_1, "or", escapeDoubleQuote_2, useRealBackslash, addNewLine, addTab)

task_01 = "Your learning path:\n\t - Python Basics\n\t-Data Engineering\n\t - AI"
# ! """ - Triple quotes - Позволяет писать текст длинные текста
task_02 = """"
Your learning path:
\n\t - Python Basics
\n\t-Data Engineering
\n\t - AI
"""
task_03 = """"Your learning path:
\t - Python Basics
\t-Data Engineering
\t - AI
"""
print(task_01, task_02, task_03)
