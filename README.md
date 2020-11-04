# ParsStick
**Парсер стикеров для ВКонтакте.**
***
***скачивает все стикеры , которые есть в ВКонтакте в формате png***
# Инструкция для TERMUX
**pkg update -y**
**pkg install git -y**
**termux-setup-storage - разрешаем использования внутренней памяти.**
**cd storage**
**cd downloads**
**git clone https://github.com/mishaQ23n/ParsStick**
**cd ParsStick**
**bash install.sh**
# Далее заходим в проводник, заходим в папку download, и ищем папку ParsStick. Заходим  в эту папку, и открываем файл "main.py" с любого текстового редактора. 
и ищем эту строчку. out = open(f'путь где будет сохранятся стики/{b}.png', "wb") Вместо "путь где будет сохранятся стики" пишем путь где будут сохранятся стики пример out = open(f'storage/downloads/{b}.png', "wb") и все готово , теперь заходим в termux и запускаем скрипт
**python main.py**
Готово, по вопросам пишите на [нашу группу](https://vk.com/scripts_xxx)
