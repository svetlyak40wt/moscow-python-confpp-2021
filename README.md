Установка
---------

Для установки зависимостей потребуется [pipenv](https://pipenv.pypa.io/en/latest/):

    pipenv install

Как запутить Jupyter
--------------------

    pipenv run jupyter notebook

Как установить кастомное ядро
-----------------------------

    pipenv run jupyter \
           kernelspec install \
           ./custom-kernel \
           --user
