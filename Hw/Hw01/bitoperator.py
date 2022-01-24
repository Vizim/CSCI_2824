#DO NOT CHANGE THE NAMES OF THE FILE, CLASS or METHOD


class BitOperator(object):
	self = 0

	def bitOperator(self,bit1,bit2):
		s1 = ""
		s2 = ""
		for i in range(len(bit1)):
			if(bit1[i]== "1" and bit2[i] == "1"):
				s1 = s1 + "1"
			else:
				s1 = s1 + "0"

			if(bit1[i]== "1" or bit2[i] == "1"):
				s2 = s2 + "1"
			else:
				s2 = s2 + "0"

		return (s2, s1)



'''
x = BitOperator() 
print(x.bitOperator(11011,10001))
'''
