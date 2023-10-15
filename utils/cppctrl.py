import utils.cmdctrl as cmdctrl
import sys, subprocess

class cppcontroller:
	def __init__(self):
		self.cc = cmdctrl.cmdcontroller("g++ .\\utils\\debugfile.cpp", [
			"-DPYRUN_DEBUG_MODE", "-Drunning_offline", "-Ddebug_offline",
			"-Wall -std=c++14 -o main.exe -I utils"
		])
		self.check_result = False

	def isdebugdef(self, s: str):
		return (s.startswith("void debugp(const char *fmt, ...)") or
				s.startswith("void debuge(function<void()> action)"))

	def accept_arg(self, arg):
		if arg == "hack":
			self.cc.removearg("-DPYRUN_DEBUG_MODE")
			self.cc.addarg("-DPYRUN_HACK_MODE")
		elif arg == "hackgen" or arg == "hg":
			self.cc.removearg("-DPYRUN_DEBUG_MODE")
			self.cc.addarg("-DPYRUN_HACKGEN_MODE")
		elif arg == "interactive" or arg == "int":
			self.cc.removearg("-Drunning_offline")
		elif arg == "nodebug" or arg == "nd":
			self.cc.removearg("-Ddebug_offline")
		elif arg == "tofile" or arg == "tf" or arg == "longcheck" or arg == "longchk" or arg == "lc":
			self.check_result = False
			self.cc.addarg("-Dchecking_offline")
		elif arg == "check" or arg == "chk" or arg == "c":
			self.check_result = True
			self.cc.removearg("-Dchecking_offline")
		else:
			return False
		return True
	
	def rewrite(self, file):
		with open(".\\utils\\debugfile.cpp", "w") as debugfile:
			with open(file, "r") as file:
				debugfile.write('#include "debugutils.inc"\n\n')
				for i in file.readlines():
					if not self.isdebugdef(i):
						debugfile.write(i)

	def run(self):
		pitem = subprocess.Popen(self.cc.construct())
		pitem.wait()
		if pitem.returncode != 0:
			print("Compile failed.", file=sys.stderr)
		else:
			print("Compile success.", file=sys.stderr)
			if self.check_result:
				# Get output
				pitem = subprocess.Popen(".\\main.exe", stdout=subprocess.PIPE)
				pitem.wait()
				raw_output = pitem.stdout.read().decode("ascii")
				print(raw_output, end="")
				output = raw_output.split()

				# Get answer
				raw_answer = ""
				with open("answer.txt", "r") as answer_file:
					raw_answer = answer_file.read()
				answer = raw_answer.split()

				# Compare
				correct = True
				for i in range(min(len(output), len(answer))):
					if answer[i] != output[i]:
						print("Token %d differ: \"%s\", expected \"%s\""%(i + 1, output[i], answer[i]))
						correct = False
				if len(output) != len(answer):
					print("Answer length differ: %d, expected %d"%(len(answer), len(output)))
					correct = False
				if correct:
					print("The answer seems to be correct.")
				
			else:
				subprocess.Popen(".\\main.exe").wait()