## Приложение, считающее частоту слов во входном потоке


#### Технологии

Python 3.5


#### Запуск

```sh
$ cd /path/to/woco
$ python woco.py -p 2 -i test.txt
```

* Где в:
  * -p или --processes, указывается количество запускаемых процессов(по-умолчанию 1)
  * -i или --input_file, указывается путь до файла(по-умолчанию test.txt)

Команда выше, запустит подсчет частоты слов в файле test.txt, используя 2 процесса