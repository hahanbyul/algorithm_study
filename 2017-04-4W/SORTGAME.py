import pprint as pp


class Sortgame:
	def __init__(self, string):
		self.seq = string.split()
		self.discovered = dict()
		self.q = list()
		
	def reverse_sublist(self,lst,start,end):
		ret = [i for i in lst]
		ret[start:end] = ret[start:end][::-1]
		return ret
		
	def generator(self, lst):
		for i in range(len(lst)-1):
			for j in range(i+2, len(lst)+1):
				yield self.reverse_sublist(lst,i,j)
				
	def print_all_rev(self, lst):
		for rev in self.generator(lst):
			print(rev)
			
	def bfs(self):
		self.discovered[' '.join(self.seq)] = 0
		self.q.append(self.seq)
		
		while len(self.q) != 0:
			here = self.q.pop(0)
			print('here: %s' % here)
			#pp.pprint(self.q)
			if here == sorted(here):
				print("found: %s" % self.discovered[' '.join(here)])
				break
			for there in self.generator(here):
				if not self.discovered.get(' '.join(there), False):
					self.q.append(there)
					self.discovered[' '.join(there)] = self.discovered[' '.join(here)] + 1
