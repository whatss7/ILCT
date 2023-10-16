import sys

def debugp(s: str):
	msg = "DBG: " + s
	print(msg, end=("\n" if msg[-1] != '\n' else ""), file=sys.stderr)

def debuge(action):
	action()
