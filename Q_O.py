from stt_and_logic import run_loop
import traceback
try:
	while 1:
		run_loop()
		input()
except:
	input(traceback.format_exc())