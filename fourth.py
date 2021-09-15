import requests
from ipywidgets import (HTML, Button, Password,
                        HBox, VBox, Layout)
from functools import wraps


def request_token(ipython):
    input = Password(
        value='',
        placeholder='Введи OAuth токен',
    )
    button = Button(description='Установить')
    warning_string = HTML('')

    def on_submit(button):
        ...

    button.on_click(on_submit)

    grid = HBox([
        VBox([input, warning_string]),
        button
    ])
    display(grid)

def request_token(ipython):
    input = Password(
        value='',
        placeholder='Введи OAuth токен',
    )
    button = Button(description='Установить')
    warning_string = HTML('')

    def on_submit(button):
        value = input.value
        
        if value:
            # Здесь должно быть реальное сохранение
            # настройки к конфиг
            ipython.user_ns['TOKEN'] = value
            input.value = ''
            warning_string.value = (
                '<b>секрет сохранён</b>, '
                'попробуй выполнить ячейку заново')
            
    button.on_click(on_submit)

    grid = HBox([
        VBox([input, warning_string]),
        button
    ])
    display(grid)
    

def decorate_showtraceback(ipython, func):
    @wraps(func)
    def wrapper(etype, evalue, traceback):
        if etype is requests.HTTPError:
            return request_token(ipython)
        else:
            return func(etype, evalue, traceback)
    return wrapper

    
def load_ipython_extension(ipython):
    print('Loading "fourth" extension')

    ipython._showtraceback = decorate_showtraceback(
        ipython,
        ipython._showtraceback
    )
