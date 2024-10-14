# Module 4 Practice 2

def test_function(*args):
    a = 14
    if a > 14:
        def inner_function():
            print('Я в области видимости функции "test_function"')
        inner_function()
    else:
        print('Хорошая погода')

test_function('Hello')

# inner_function вне функции test_function не определена