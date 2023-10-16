import utils.misc as misc
import sys, subprocess

class cppcontroller:
	def __init__(self):
		self.cc = misc.cmdcontroller("g++ .\\utils\\debugfile.cpp", [
			"-DPYRUN_DEBUG_MODE", "-Drunning_offline", "-Ddebug_offline",
			"-Wall -std=c++14 -o .\\utils\\main.exe -I utils"
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
		elif arg == "tofile" or arg == "tf":
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
				debugfile.write('#include "debugutils_cpp.inc"\n\n')
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
				pitem = subprocess.Popen(".\\utils\\main.exe", stdout=subprocess.PIPE)
				pitem.wait()
				output = pitem.stdout.read().decode("ascii")
				print(output, end="")

				# Get answer
				answer = ""
				with open("answer.txt", "r") as answer_file:
					answer = answer_file.read()

				# Compare
				misc.compare(output, answer)
			else:
				subprocess.Popen(".\\main.exe").wait()