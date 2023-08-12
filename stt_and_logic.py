try:
	from traceback import format_exc
	from threading import Thread
	from vosk import Model, KaldiRecognizer
	from tts import tts as TTS, дозапись
	from random import randint
	from ListOfMat import list_mat
	from Funcs import*
	from SpeakModule import*
	import mouse, keyboard, sounddevice as sd
	import os
	import json
	import time
	import datetime
	import webbrowser
	import sys
	import queue
except ImportError:
	print("Нехватка модулей")
	print(format_exc())
from str_to_num import convertToNum

with open("start.bat", "w", encoding="utf-8") as file:
	typefile = __file__.split(".")
	file.write(f"cd {getcwd()}\nstart main.{typefile[1]}")
try:
	with open("history.txt", "r", encoding="utf-8") as file:
		file.read()
except Exception as e:
	print(e)
	with open("history.txt", "w", encoding="utf-8") as file:
		file.write("Здесь история ваших сообщений:")

music_list = {}
try:
	import pygame
	pygame.init()
	Music_volume = 100
	for ind in range(len(os.listdir(getcwd().replace(__file__,"")+r"\Misc"))):
		i =          str(os.listdir(getcwd().replace(__file__,"")+r"\Misc")[ind])[:-4]
		j =          str(os.listdir(getcwd().replace(__file__,"")+r"\Misc")[ind])
		print(i)
		music_list[i] = {}
		music_list[i]["music"] = None
		music_list[i]["path"] = getcwd()+"/Misc/" + j
		music_list[i]["num"] = ind
		music_list[i]["value"] = False
		music_list[i]["name"] = i
except Exception as e:print(e)
try:
	model = Model(os.getcwd() + r"\model") # полный путь к модели
except Exception as e:
	tts.ospeak('Модель располагается в другом месте...')
samplerate = 16000
device = 1
q = queue.Queue()
def q_callback(indata, frames, time, status):
	if status:
		print(status, file=sys.stderr)
	q.put(bytes(indata))
def qo_loop():
	with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=device, dtype='int16',
						channels=1, callback=q_callback):
		rec = KaldiRecognizer(model, samplerate)
		os.system("cls")
		while True:
			data = q.get()
			if rec.AcceptWaveform(data):
				x = json.loads(rec.Result())["text"]
				if x != "":
					command(x)
			#else:
			#    print(rec.PartialResult())
class Text_assessment:
	def __init__(self):
		self.count = 0
	def grage(self, text):
		if in_list(text, ["железяка", "железка"] + list_mat):
			self.count -= 1
		if in_list(text, ["пожалуйста", "спасибо", "молодец", "круто", "красавчик", "имба", "ништяк", "простите"]):
			self.count += 1
		if "я рома" in text:
			self.count += 100

rate = Text_assessment()


def command(text):
	global mode, ussr_gimn, music_list, tts, Music_volume
	print(str(datetime.datetime.now().time())[:8] + " Ты: " + text)
	rate.grage(text)
	дозапись("Ты: " + text , "history.txt")
	if ratio(text, "повторяй"):
		mode = "repeating"
	elif "запиши" in text:
		try:
			os.remove("data.mp3")
		except:pass
		print("Запуск")
		time.sleep(1)
		tts.SaveToFile(text[len("запиши"):])
		tts.ospeak("Сделано")
	elif randint(0,1000) == 1 and not mode == "repeating":
		tts.ospeak("Привет, не забывай что всё что ты говоришь сохраняется в истории history.txt на досуге можешь почитать.")
	elif mode == "repeating":
		if ratio(text, "Выход из режима"):
			mode = "listen"
		else:
			tts.ospeak(text)
	elif mode == "listen":
		if ratio(text, "управление мышкой") or ratio(text, "управление мышью") or ratio(text, "режим управления мышью") or ratio(text, "режимом управления мышью"):
			if rate.count < 0:
				tts.ospeak("Так точно, наводчик хренов")
			elif rate.count < 10:
				tts.ospeak("Принято")
			else:
				tts.ospeak("Готов управлять, (надеюсь потом похвалят)")
			mode = "control mouse"
		elif ratio(text, "Режим печати под диктовку") or ratio(text, "Режим диктовки") or ratio(text, "Режим под диктовку") or ratio(text, "диктую") or ratio(text, "режим управления клавиатурой") or ratio(text, "режима правления короля артура"):
			tts.ospeak("Принято")
			mode = "keyboard"
		elif AnswerOfQ_O(text, rate) != None: pass
		elif "список" in text:
			New_text = ""
			for i in music_list:
			    New_text = New_text + " " + music_list[i]["name"] + ";\n"
			tts.ospeak(New_text)
		elif "стоп" in text or ratio(text, "выключить"):
			for i in music_list:
				if music_list[i]["value"]:
					music_list[i]["music"].stop()
					music_list[i]["value"] = False
		elif "громкость" in text:
			#Громкость и только цифра
			text = convertToNum(text)
			for i in music_list:
				try:music_list[i]["music"].set_volume(text / 100); Music_volume = text
				except:pass
		else:
			try:
				for i in music_list:
					if (ratio(text, music_list[i]["name"]) or music_list[i]["name"] in text) and music_list[i]["value"] == False:
						for StopMusic in music_list:
							if  music_list[StopMusic]["value"]:
								music_list[StopMusic]["music"].stop()
								music_list[StopMusic]["value"] = False
						try:
							music_list[i]["music"].play()
						except:
							music_list[i]["music"] = pygame.mixer.Sound(music_list[i]["path"])
							music_list[i]["music"].play()
						try:music_list[i]["music"].set_volume(Music_volume / 100)
						except:pass
						music_list[i]["value"] = True
						return
			except:pass
			дозапись(text, "Разработчикам.txt")


	elif mode == "control mouse":
		nums = convertToNum(text)
		if ratio(text, "выход из режима управления мышкой") or ratio(text, "выход") or ratio(text, "стоп") or ratio(text,"Выход из режима"):
			tts.ospeak("Есть")
			mode = "listen"
		elif ratio(text, "нажми") or ratio(text, "клик"):
			mouse.click()
		elif "верх" in text or "вверх" in text:
			mouse.move(0, nums * -1, False)
		elif "вниз" in text or "низ" in text:
			mouse.move(0, nums, False)
		elif in_list(text, ["право","вправо", "праву", "правее", "справа"]):
			mouse.move(nums, 0, False)
		elif in_list(text, ["лево", "левее", "леву"]):
			mouse.move(nums * -1, 0, False)
		else:
			дозапись(text, "Разработчикам.txt")
		
	elif mode == "keyboard":
		print("R")
		if ratio(text, "выход") or ratio(text, "стоп") or ratio(text, "Выход из режима"):
			mode = "listen"
			tts.ospeak("Так точно")
		elif ratio(text,"вот"):
			keyboard.press("enter")
		elif ratio(text, "копировать"):
			keyboard.press("ctrl + c")
		elif ratio(text, "вставить"):
			keyboard.press("ctrl + v")
		elif ratio(text, "убери слово",70):
			keyboard.send("ctrl + left")
			keyboard.send("delete")
		else:
			print("Write")
			keyboard.write(text+" ")

def run_loop():
	global mode
	mode = "listen"
	os.chdir(os.getcwd())
	Thread(target=qo_loop, args = ()).start()
if __name__ == "__main__":
	run_loop()