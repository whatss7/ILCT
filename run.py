import sys, subprocess


class cmdcontroller:

	def __init__(self, base: str, extra: list[str]):
		self.base = base
		self.extra = set()
		for i in extra:
			self.extra.add(i)

	def addarg(self, arg: str):
		self.extra.add(arg)

	def removearg(self, arg: str):
		if arg in self.extra:
			self.extra.remove(arg)

	def construct(self) -> str:
		return self.base + " " + " ".join(self.extra)


def isdebugdef(s: str):
	return (s.startswith("void debugp(const char *fmt, ...)") or
	        s.startswith("void debuge(function<void()> action)"))


def main():
	if len(sys.argv) == 1:
		print("Usage: python " + sys.argv[0] + " <file-to-compile> [<flags>]")
		return

	args = []
	inst = []
	prefix = "--pyrun-"
	for i in sys.argv[1:]:
		if i.startswith(prefix):
			args.append(i)
		else:
			inst.append(i)

	with open(".\\utils\\debugfile.cpp", "w") as debugfile:
		with open(inst[0], "r") as file:
			debugfile.write('#include "debugutils.inc"\n')
			for i in file.readlines():
				if not isdebugdef(i):
					debugfile.write(i)

	cc = cmdcontroller("g++ .\\utils\\debugfile.cpp " + " ".join(inst[1:]), [
	    "-DPYRUN_DEBUG_MODE", "-Drunning_offline", "-Ddebug_offline",
	    "-Wall -std=c++14 -o main.exe -I utils"
	])
	check_result = False
	for i in args:
		p = i[len(prefix):]
		if p == "random" or p == "rand":
			subprocess.Popen(".\\utils\\randgen.exe").wait()
		elif p == "hack":
			cc.removearg("-DPYRUN_DEBUG_MODE")
			cc.addarg("-DPYRUN_HACK_MODE")
		elif p == "hackgen" or p == "hg":
			cc.removearg("-DPYRUN_DEBUG_MODE")
			cc.addarg("-DPYRUN_HACKGEN_MODE")
		elif p == "interactive" or p == "int":
			cc.removearg("-Drunning_offline")
		elif p == "nodebug" or p == "nd":
			cc.removearg("-Ddebug_offline")
		elif p == "tofile" or p == "tf" or p == "longcheck" or p == "longchk" or p == "lc":
			check_result = False
			cc.addarg("-Dchecking_offline")
		elif p == "check" or p == "chk" or p == "c":
			check_result = True
			cc.removearg("-Dchecking_offline")
		else:
			print("Unexpected argument: --pyrun-" + p, file = sys.stderr)
			return

	pitem = subprocess.Popen(cc.construct())
	pitem.wait()
	if pitem.returncode != 0:
		print("Compile failed.", file=sys.stderr)
	else:
		print("Compile success.", file=sys.stderr)
		if check_result:

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


if __name__ == "__main__":
	main()