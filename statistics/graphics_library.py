class Graphics:

	def test():
		print("test")

	def tree():

		print('# '*19)
		rnd2 =randint(1,19)
		for x in range(1,15):
			rnd1 =randint(1,rnd2)
			if x==1:
				ch ='$'
			elif rnd1%4==0:
				ch ='o'
			elif rnd1%3==0:
				ch ='i'
			else:
				ch ='*'
			print('#','{:^33}'.format(ch*x),'#')
		print('# '*19)

	def tabulation():
		
		#fix '00' print
		from main import tuple00
		for r in range(1):
			print(' '*len('01  |'))
			for i in range(1,Ki -5):
				print('_ _',end=' ')
			print()
		print()

		print('   ',(' ' +'__')*(Ki -2) +' ')
		for i in range(1,Ki):
			if len(str(i)) ==1:
				print('0{}'.format(i),end='')
			else:
				print('{}'.format(i),end='')
			print(' ',('|' +'__')*(Ki -2) +'|')
		print('Y')

		#
		for j in range(Ki,Ki+1):
			for x in range(1,3):
				print('  ',end='')
			for j in range(1,30):
				if len(str(j)) ==1:
					print('0{}'.format(j),end=' ')
				else:
					print('{}'.format(j),end=' ') 
			print('X')