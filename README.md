Этот проект написан на джанго

Важно! Загрузите фикстуры из data.json, это необходимо для корректной работы сайта, там находятся группы с разрешениями и site.

Для корректной работы добавте в папку config - yandex.ini с настройками вашего почтового smtp сервера

Шаблон:
[yandex]
host=host
port=port
connecttype=TLS
hostuser=hostuser@yandex.ru

Если вы не хотите что бы письма приходили на настоящую почту тогда можете в setting.py разкомментировать поле:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
Тогда все письма будут приходить в консоль