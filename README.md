В файле skreen_translate.py находится код Python-скрипт по переводу текста с выделеной области экрана.
Скрипт работает не в фоновом режими и открывается через командную строку или открытием файла.
Скрипт работает в дополнение к Инструменту обрезки Windows(ctrl+shist+s) и запускается при нажатии упомянутого сочетания клавишь.
После выделения области с текстом, скриншот сохраняется в буфере обмена, скрипт его обрабатывает и с помощью pytesseract определяет текст и язык, и переводит его с помощью google translate, после появляется окно
из 2 областей слева определенный текст, справа переведенный, в верхней части областей есть смена языков и кнопка копирования текста в буфер обмена.
