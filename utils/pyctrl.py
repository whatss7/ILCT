import utils.misc as misc
import sys, subprocess

class pycontroller:
	def __init__(self):
		self.cc = misc.cmdcontroller("python .\\utils\\debugfile.py", [])
		self.check_result = False
		self.mode = "default"
		self.redirect_input = True
		self.redirect_output = False
		self.will_rewrite = True

	def isdebugdef(self, s: str):
		return (s.startswith("debugp = lambda _: None") or
				s.startswith("debuge = lambda _: None"))

	def accept_arg(self, arg):
		# if arg == "hack":
		# 	self.mode = "hack"
		# 	return True
		# elif arg == "hackgen" or arg == "hg":
		# 	self.mode = "hackgen"
		# 	return True
		if arg == "interactive" or arg == "int":
			self.redirect_input = False
		elif arg == "nodebug" or arg == "nd":
			self.will_rewrite = False
		elif arg == "tofile" or arg == "tf":
			self.check_result = False
			self.redirect_output = True
		elif arg == "check" or arg == "chk" or arg == "c":
			self.check_result = True
			self.redirect_output = False
		else:
			return False
		return True
	
	def rewrite(self, file):
		if not self.will_rewrite:
			return
		with open(".\\utils\\debugfile.py", "w") as debugfile:
			with open(file, "r") as file:
				debugfile.write('from debugutils_py import debugp, debuge\n\n')
				for i in file.readlines():
					if not self.isdebugdef(i):
						debugfile.write(i)

	def run(self):
		if self.redirect_input:
			with open("in.txt", "r") as in_file:
				self.run_I(in_file)
		else:
			self.run_I(sys.stdin)
		
	def run_I(self, in_file):
		if self.redirect_output:
			with open("out.txt", "w") as out_file:
				self.run_IO(in_file, out_file)
		elif self.check_result:
			self.run_IO(in_file, subprocess.PIPE)
		else:
			self.run_IO(in_file, sys.stdout)
	
	def run_IO(self, in_file, out_file):
		pitem = subprocess.Popen(self.cc.construct(), cwd=".", stdin=in_file, stdout=out_file)
		pitem.wait()
		if self.check_result:
			# Get output
			output = pitem.stdout.read().decode("ascii")
			print(output, end="")

			# Get answer
			answer = ""
			with open("answer.txt", "r") as answer_file:
				answer = answer_file.read()

			# Compare
			misc.compare(output, answer)