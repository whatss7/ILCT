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

def compare(raw_output, raw_answer):
	output = raw_output.split()
	answer = raw_answer.split()
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
