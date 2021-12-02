### Доклад о возможностях pytest  
Перед началом работы необходимо установить виртуальное окружение и библиотеку pytest:  
```
$ pip3 install -U virtualenv  
$ python3 -m virtualenv venv  
$ source venv/bin/activate  
$ pip install pytest
```
В PyCharm уже встроен pytest. Файлы, которые начинаются с "test" автоматически запускаются pytest.  
Если ввести команду pytest в репозитории, то запустятся все тесты в файлах, которые начинаются со слова test и функции и классы, которые начинаются со слова test
  
Файлы с тестами:
test_func.py - содержит примеры тестовых функций без применения библиотеки pytest  
test_func_markers.py - содержит примеры тестовых функций c маркерами  
test_func_fixtures.py - содержит примеры тестовых функций c фикстурой  
test_func_fixtures.py - содержит примеры тестовых функций c фикстурой  
test_scope.py - пример различных значений scope в фикстуре

Конфигурационные файлы pytest:  
conftest.py  
pytest.ini  
  
Запуск тестов из консоли:
```pytest -v --ff --tb=no test_func.py  
pytest -v --ff --tb=no test_func_markers.py  
pytest -v --ff --tb=no test_func_fixtures.py
```
  
Запуск тестов с опрделенными маркерами:
```pytest -v -m show test_func_markers.py
pytest -v -m main test_func_markers.py
pytest -v -m second test_func_markers.py
```
Пользовательские маркеры описыватся в файле pytest.ini

Показать структуру запуска тестов:  
```
pytest --setup-show test_func_fixtures.py
```

Вывести структуру тестов с использованием различных значений аргумента scope в фикстуре:
```
pytest --setup-show test_scope.py
```

Запуск одного теста из файла. Необходимо указать в формате: <файл>::<функция с тестом>
-vv вводится для того, чтобы pytest показал в чем именно заключается ошибка: 
```
pytest test_func_fixtures.py::test_find_duplicates -vv
```
  
Показать 4 самых медленных теста:  
```
pytest --durations=4 --vv test_func_fixtures.py
```

Ссылки:  
https://habr.com/ru/post/448782/  
https://docs.pytest.org  
