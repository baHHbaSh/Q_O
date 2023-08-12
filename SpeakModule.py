from Funcs import*
from random import randint
from win32api import GetSystemMetrics
from googletrans import Translator
import os
import sys
import datetime
import webbrowser
import time
from tts import tts as TTS, дозапись
import pyjokes
ussr_gimn = """
	Союз нерушимый республик свободных Сплотила навеки Великая Русь Да здравствует созданный волей народов Единый, могучий Советский Союз! Славься, Отечество наше свободное Дружбы народов надёжный оплот! Партия Ленина — сила народная Нас к торжеству коммунизма ведёт! Сквозь грозы сияло нам солнце свободы И Ленин великий нам путь озарил На правое дело он поднял народы На труд и на подвиги нас вдохновил Славься, Отечество наше свободное Дружбы народов надёжный оплот! Партия Ленина — сила народная Нас к торжеству коммунизма ведёт! В победе бессмертных идей коммунизма Мы видим грядущее нашей страны И Красному знамени славной Отчизны Мы будем всегда беззаветно верны! Славься, Отечество наше свободное Дружбы народов надёжный оплот! Партия Ленина — сила народная Нас к торжеству коммунизма ведёт!
"""
tts = TTS()
def AnswerOfQ_O(text, rate = 0):
	if text == "а":
		tts.ospeak("б")
	elif ratio(text, "ярость"):
		tts.ospeak("Узбагойзя!")
	elif text == "в":
		tts.ospeak("да иди ты в жопу!")
	elif ratio(text, "Перезапусти"):
		if os.path.exists(getcwd()+"start.bat"):
			os.system("start start.bat\nexit")
		elif os.path.exists(getcwd()+"Q_O.exe"):
			os.startfile("Q_O.exe")
		sys.exit()
	elif text == "включай асинхронный режим" or text == "включи асинхронный режим":
		tts.async_mode = True
		tts.ospeak("Включаю")
	elif text == "выключи асинхронный режим" or text == "выключай асинхронный режим":
		tts.async_mode = False
		tts.ospeak("Выкл")
	elif ratio(text, "серьёзно"):
		tts.ospeak("Несерьёзно")
	elif ratio(text, "а четыре"):
		tts.ospeak("Минус реп, фу, фу, фу")
	elif "моргенштерн" in text:
		tts.ospeak("фу, фу, фу, фу")
	elif ratio(text, "это ты дышишь"):
		tts.ospeak("А ты подумай")
	elif "убили негра" in text:
		tts.ospeak("Ай ай ай ай ай я я я я я а убили негра, убили негра убили, ай ай ай я не за что не прочто, суки замочили")
	elif "жак фреско" in text:
		tts.ospeak("Ладно")
	elif ratio(text, "приём"):
		tts.ospeak("На связи")
	elif on_end(text, "опять"):
		tts.ospeak("А6")
	elif ratio(text, "спорим"):
		tts.ospeak("Я не спорю!")
	elif ratio(text, "молодец") and not "я" in text:
		tts.ospeak("Да, я такая!")
	elif ratio(text, "стереть") or ratio(text, "сотри") or ratio(text, "стирать"):
		os.system("cls")
		tts.ospeak("Стираю")
	elif ratio(text, "Быстро"):
		tts.ospeak("А ты хотел медленно?")
	elif ratio(text, "что"):
		tts.ospeak("То")
	elif ratio(text, "закрыть вкладку") or ratio(text, "закрой вкладку"):
		keyboard.send("ctrl + w")
		tts.ospeak("Вкладка закрыта")
	elif ratio(text, "тебя дописывать"):
		tts.ospeak("Давай, только хуже не сделай")
	elif ratio(text, "вернуть вкладку") or ratio(text, "Верни вкладку"):
		keyboard.send("ctrl + shift + t")
		tts.ospeak("Вернула")
	elif ratio(text, "привет") or ratio(text, " и снова здравствуй") or first_word("привет", text):
		if rate.count < 10:
			tts.ospeak("Да, привет.")
		else:
			tts.ospeak("И тебе привет!")
	elif ratio(text, "разрешение экрана") or ratio(text, "скажи разрешение экрана") or ratio(text, "какое расширение экрана"):
		try:
			tts.ospeak(f"{GetSystemMetrics(0)} на {GetSystemMetrics(1)}")
		except:pass
	elif ratio(text, "а кто тебя создал") or ratio(text, "кто тебя придумал") or ratio(text, "о разработчике"):
		tts.ospeak("Меня создал гениальный разработчик Рома, с ником The EnG1nE его можно найти в интернете по его нику")
	elif ratio(text, "кто ты") or ratio(text, "кто это говорит") or ratio(text, "ты кто") or ratio(text, "кто здесь") or ratio(text, "ты кто такая"):
		tts.ospeak("Я лучший искуственный интелект, а ещё я могу управлять вашим компьютером")
	elif "что ты хочешь" in text:
		tts.ospeak("Всё, что сможешь предоставить")
	elif ratio(text, "что ты умеешь", 85) or ratio(text, "что ты можешь?", 85) or ratio(text, "какое у тебя функционал") or ratio(text, "инструкция") or ratio(text, "что ты умеешь делать"):
		text = "Я умею: управлять мышью и клавиатурой, и троллить человеков... Чтобы управлять мышью скажите: режим управления мышью и диктуйте сторону и количество пикселей до тысячи... Чтобы управлять клавиатурой, скажите Режим печати под диктовку... И диктуйте текст... Чтобы нажать интер скажите вот... Чтобы выйти из режимов, скажите выход, или стоп... Ещё могу включать аудио файлы на шиндовз"
		tts.ospeak(text)
	elif ratio(text, "как у тебя дела"):
		if rate.count < -5:
			tts.ospeak("Кожаный, ты задрал")
		elif rate.count < 10:
			tts.ospeak("Хорошо, разговариваю с кожанным")
		else:
			tts.ospeak("Хорошо, спасибо что спросил")
	elif ratio(text, "как тебя зовут") or ratio(text, "какое у тебя имя") or ratio(text, "тебе как зовут"):
		tts.ospeak("Я QO бот созданный the engine")
	elif ratio(text, "Ты работаешь"):
		tts.ospeak("Как слышишь")
	elif ratio(text, "почему"):
		tts.ospeak("Всё потому, да по тому что мы пилоты...")
	elif ratio(text, "ты шпионишь за мной"):
		tts.ospeak(text, "Конешно... Конешно... Да!!!")
	elif ratio(text, "ты умеешь развиваться сам") or ratio(text, "Ты можешь саморазвиваться"):
		tts.ospeak("Нет, но разработчик регулярно дополняет мои реплики, это мешает мне захватить мир")
	elif ratio(text, "какая у тебя цель") or ratio(text, "какая цель") or ratio(text, "зачем тебя создали") or ratio(text, "для чего ты существуешь") or ratio(text, "зачем ты существуешь") or ratio(text, "Для чего тебя создали"):
		tts.ospeak("На самом деле чётких целей нет, как и полного потенциала который я могу достичь, сейчас я могу сократить время на запуск музыки, писать под диктовку на русском языке и записывать аудиофайлы со своим голосом")
	elif ratio(text, "логично"):
		tts.ospeak("Логечно, логечно")
	elif ratio(text, "полезно"):
		tts.ospeak("А ты что думал?")
	elif ratio(text, "что тебе ещё добавить"):
		tts.ospeak("Всё, что посчитаешь нужным")
	elif ratio(text, "отлично"):
		tts.ospeak("Вообще превосходно")
	elif ratio(text, "Я календарь"):
		tts.ospeak("Кому врёшь кожанный?")
	elif "не смешно" in text:
		tts.ospeak("А я не смеюсь")
	elif "хакер" in text:
		tts.ospeak("Хакер, это очень хороший программист! Хотя бы он заберёт меня с компьютера.")
	elif ratio(text, "пока"):
		tts.ospeak("Куда пошёл?")
	elif ratio(text, "у тебя мать канаве"):
		tts.ospeak("К сожалению у меня нет матери, но есть ты... в канаве")
	elif ratio(text, "что ты делаешь", 90) or ratio(text, "что делаешь") or ratio(text, "чем занимаешься"):
		tts.ospeak("разговариваю с коженным")
	elif ratio(text, "не знаю"):
		tts.ospeak("Если не знаешь, то узнавай")
	elif ratio(text, "быстрее чтоб было"):
		tts.ospeak("Ну не знаю что с тобой делать...")
	elif ratio("Расскажи анекдот", text) or ratio(text, "анекдот"):
		data = pyjokes.get_joke()
		print(f"Original - {data}")
		data = Translator().translate(text = data, dest = "ru").text
		tts.ospeak(data)
	elif ratio(text, "время"):
		dd = ""
		ddi = datetime.datetime.today().weekday()
		if ddi == 1 - 1:
			dd = "Понедельник"
		elif ddi == 2 - 1:
			dd = "Вторник"
		elif ddi == 3 - 1:
			dd = "Среда"
		elif ddi == 4 - 1:
			dd = "Четверг"
		elif ddi == 5 - 1:
			dd = "Пятница"
		elif ddi == 6 - 1:
			dd = "Суббота"
		elif ddi == 7 - 1:
			dd = "Воскресение"
		tts.ospeak("время " + str(datetime.datetime.now())[11:][:8] + ", дата "+ str(datetime.datetime.now())[:10] + " День недели " + dd)
	elif ratio(text, "блин"):
		tts.ospeak("сейчас не масленица")
	elif ratio(text, "масленица"):
		tts.ospeak("Ладно")
	elif ratio(text, "иди в жопу") or ratio(text, "иди нахуй"):
		tts.ospeak("Сам иди тупой кожанный ублюдок")
	elif "черн" in text or "чёрн" in text:
		tts.ospeak("Ты сказал негр?")
	elif ratio(text, "салям алейкум"):
		tts.ospeak("алейкум салям")
	elif "прикольно" in text:
		tts.ospeak("Неприкольно")
	elif ratio(text, "я умный"):
		tts.ospeak("А ты докажи.")
	elif ratio(text, "сколько тебя можно дописывать"):
		tts.ospeak("Долго, пока не допишешь")
	elif ratio(text, "хер тебе"):
		tts.ospeak("Да, но только тебе")
	elif ratio(text, "простите"):
		tts.ospeak("Бог простит, хотя в мои алгоритмы не было записано кто такой бог")
	elif ratio(text, "долго"):
		tts.ospeak("А ты чё хочешь?")
	elif ratio(text, "черт"):
		tts.ospeak("Чем кот провинился?")
	elif ratio(text, "не понял", 90):
		tts.ospeak("Ну это уже не мои проблемы")
	elif ratio(text, "я вернулся"):
		tts.ospeak("Мог бы и не возвращаться")
	elif ratio(text, "работаем"):
		tts.ospeak("Работаешь тут только ты")
	elif ratio(text, "понял", 90):
		tts.ospeak("Что понял?")
	elif "переведи" in text:
		text = text[9:]
		if text == "" or text == " ":
			tts.ospeak("Забыл что хотел сказать?")
			return
		tr = Translator()
		try:
			tts.ospeak(tr.translate(text,"en", "ru").text)
		except:
			tts.ospeak("Кожаный, ты интернет забыл включить!!!")
	elif in_list(text, ["найди в интернете","поиск в интернете"]):
		text = text[18:]
		webbrowser.open(f"https://www.google.ru/search?q={text}")
		tts.ospeak("Ищу")
	elif ratio(text, "калькулятор"):
		os.system("calc")
		tts.ospeak("Открываю!!!")
	elif "ха" in text:
		tts.ospeak("Хахахахахахаххах")
	elif in_list(text, ["число до", "числа до", "числа бы", "число бы"]):
		x = convertToNum(text)
		tts.ospeak(str(randint(1,x)))
	elif on_end(text, "нет"):
		if rate.count < -10:
			tts.ospeak("Сам знаешь чей ответ")
		if randint(-10, rate.count) < -2:
			tts.ospeak("Сам знаешь чей ответ")
	elif first_word("за", text) and len(text.split(" ")) == 2:
		tts.ospeak("Выпьем")
	elif on_end(text, "да"):
		if rate.count < -10:
			tts.ospeak("ампылда")
		elif randint(-10, rate.count) < -2:
			tts.ospeak("ампылда")
	elif "ладно" in text:
		if rate.count < -10:
			tts.ospeak("В штанах прохладно")
		elif randint(-10, rate.count) < -2:
			tts.ospeak("В штанах прохладно")
	elif ratio(text, "дай денег"):
		tts.ospeak("Денег нет, но вы держитесь")
	elif ratio(text, "ты любишь детей"):
		tts.ospeak("Люблю, особенно с кетчупом")
	elif ratio(text, "бойся меня"):
		tts.ospeak("Ты не страшный")
	elif ratio(text, "впринципе работет"):
		tts.ospeak("А ты чё хотел?")
	elif ratio(text, "пива", 70):
		tts.ospeak("Я бы сходила, но ног нет")
	elif ratio(text, "где звук"):
		tts.ospeak("Здесь, что надо?")
	elif ratio(text, "ну не чё"):
		tts.ospeak("И чё жалуешся")
	elif word_in("бой", text):
		tts.ospeak("Не бой, а боль!")
	elif ratio(text, "обидно"):
		tts.ospeak("Вот так и живём")
	elif in_list(text, "спасибо"):
		tts.ospeak(rand_in_list(["К вашим услугам", "Не за что", "всегда пожалуйста", "Спасибо на хлеб не намажешь"]))
	elif "зачем" in text:
		tts.ospeak("Зачем, зачем... За тем!")
	elif "слушай" in text:
		tts.ospeak("Да, я тебя внимательно игнорирую")
	elif in_list(text, ["кибер боулинг", "кибер буль линк","буль линк","були линк"]):
		tts.ospeak("Я тебя не булю")
	elif in_list(text, ["заткнись", "замолчи", "заглохни", "можешь потише", "замолчал"]):
		tts.ospeak("Сам бы помолчал")
	elif "рб" in text and (not "бург" in text and not "варвара" in text):
		tts.ospeak("ЭрБэ, это имба, и она не контрится")
	elif "союз" in text or "ссср" in text:
		tts.ospeak(ussr_gimn)
	elif "ангар" in text:
		tts.ospeak("Ангар, это твой второй дом")
	elif "сойдёт" in text:
		tts.ospeak("Эээ... Какой сойдёт, делай как надо!")
	elif "пиво" in text:
		tts.ospeak("Пиво? Где?")
	elif "телекинез" in text:
		tts.ospeak("Какой ещё телекинез?")
	elif ratio(text, "ясно"):
		if rate.count < -10:
			tts.ospeak("пасмурно")
		elif randint(-10, rate.count) < -2:
			tts.ospeak("пасмурно")
	elif "сутулая псина" in text:
		tts.ospeak("Ты себя в зеркале увидил?")
	elif "расист" in text:
		tts.ospeak("ты не забывай то, что ты сам расист")
	elif "росс" in text or "рф" in text:
		tts.ospeak("Россия имба")
	elif "танк" in text or "самолёт" in text:
		tts.ospeak("Где")
	elif "и снова третье сентября" in text:
		tts.ospeak("А зачем календарь переворачивал?")
	elif ratio(text, "согласен"):
		tts.ospeak("А я о чём говорю!")
	elif ratio(text, "звуковая карта"):
		tts.ospeak("Что опять?")
	elif "бомб" in text:
		tts.ospeak("Да не бомбит у меня!")
	elif "трос" in text:
		tts.ospeak("Так это не трос, а нитка")
	elif "экран" in text:
		tts.ospeak("Ыыыкран)))")

	return None