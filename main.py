                    # Домашняя работа по уроку "Пространство имён"

calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string):
    count_calls()
    a = len(string), string.upper(), string.lower()
    print(a)
    return string

def is_contains(string, list_to_search):
    count_calls()
    str_upper = string.upper()
    list_upper = [item.upper() for item in list_to_search]
    return str_upper in list_upper

string_info('Capybara')
string_info('Armageddon')
string_info('Urban')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)