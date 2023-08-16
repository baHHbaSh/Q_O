from stt_and_logic import*
import traceback
try:
	while Q_O_Work:
		run_loop()
		input()
except:
	input(traceback.format_exc())