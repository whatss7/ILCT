from utils.cppctrl import cppcontroller
from utils.pyctrl import pycontroller
from utils.cctrl import ccontroller
import sys

def main():
	if len(sys.argv) == 1:
		print("Usage: python " + sys.argv[0] + " <file-to-compile> [<flags>]")
		return

	args = []
	inst = []
	prefix = "--pyrun-"
	lang = ""
	sc = None
	for i in sys.argv[1:]:
		if i.startswith(prefix):
			args.append(i)
		else:
			inst.append(i)
	file: str = inst[0]
	inst = inst[1:]
	if file.endswith(".cpp") or file.endswith(".cc"):
		lang = "C++"
		sc = cppcontroller()
	elif file.endswith(".py"):
		lang = "Python"
		sc = pycontroller()
	elif file.endswith(".c"):
		lang = "C"
		sc = ccontroller()
	else:
		print("Cannot identify language extension %s" % file[file.find('.'):])
		return
	
	for i in args:
		p = i[len(prefix):]
		if not sc.accept_arg(p):
			info = "Unexpected argument for language %s: --pyrun-%s" % (lang, p)
			print(info, file = sys.stderr)
			return

	sc.rewrite(file)
	sc.run()

if __name__ == "__main__":
	main()