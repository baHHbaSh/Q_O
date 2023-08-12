import time, pyttsx3, sounddevice as sd
import datetime, time
from threading import Thread
import traceback
def дозапись(x: str, path_to_file):
	try:
		with open(path_to_file, "r", encoding="utf-8") as file:
			q = file.read()
		with open(path_to_file, "w", encoding="utf-8") as file:
			file.write(q + f"\n{x}")
	except:
		with open(path_to_file, "w") as file:
			file.write("Start file")
class tts:
	def __init__(self):
		self.async_mode = True
	def ospeak(self, text, print_audio = True):
		if self.async_mode:
			Thread(target=self.ospeak_n_a, args=(text, print_audio)).start()
		else:
			self.ospeak_n_a(text, print_audio)
	def ospeak_n_a(self, text, print_audio = True):
		try:
			if print_audio:
				print(str(datetime.datetime.now().time())[:8] + " Бот: " + text)
			дозапись("Бот: " + text, "history.txt")
			ttss = pyttsx3.init()
			ttss.setProperty('voice', 'ru')
			ttss.say(text)
			ttss.runAndWait()
		except:
			print("[INFO] Поток tts загружен")
	def SaveToFile(self, text):
		ttss = pyttsx3.init()
		ttss.setProperty('voice', 'ru')
		ttss.save_to_file(text, "data.mp3")
		ttss.runAndWait()
		ttss.stop()