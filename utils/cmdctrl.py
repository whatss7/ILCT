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
