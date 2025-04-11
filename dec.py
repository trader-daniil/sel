import time
from datetime import datetime



def count_func_time(func):
    def wrapper():
        print('Начался отчет')
        start_time = datetime.now()
        result = func()
        duration_function = datetime.now() - start_time
        print(f'Функция работала {duration_function.microseconds}')
        return result
    return wrapper


def do_smth():
    print('Функция началась')
    time.sleep(1)
    print('Функция закончилась')


def main():
    dec = count_func_time(func=do_smth)
    dec()
    

if __name__ == '__main__':
    main()
