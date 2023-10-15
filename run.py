from utils.cppctrl import cppcontroller
import sys

def main():
	if len(sys.argv) == 1:
		print("Usage: python " + sys.argv[0] + " <file-to-compile> [<flags>]")
		return

	args = []
	inst = []
	prefix = "--pyrun-"
	lang = "C++"
	for i in sys.argv[1:]:
		if i.startswith(prefix):
			args.append(i)
		else:
			inst.append(i)
	file = inst[0]
	inst = inst[1:]
	
	sc = cppcontroller()
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