import numpy as np
import pandas as pd
import time
import operator
def getFraction(prop_code):
	classcode = {}
	N = len(prop_code)
	for el in prop_code:
		if el in classcode:
			classcode[el] = classcode[el] + 1
		else:
			classcode[el] = 1
	maxcode = max(classcode.values())
	fraction = maxcode/float(N)
	print 'Fraction of assessments are for properties of the most common class: %.12f'%fraction

def makeDict(a,b):
	A = {}
	for i in range(len(a)):
		A[a[i]] = b[i]
	return A 
		
		
def getMedian(a):
	data = {}
	count = {}
	avg = []
	sort = []
	for k,v in a.items():
		if k in data:
			data[k] = v
			count[k] = count[k]+1
		else:
			data[k] = v
			count[k] = 1
			
	for (k,v), (k2,v2) in zip(data.items(),count.items()):
		avg.append(float(v)/float(v2))
	#sort = sorted(data.values())
	#N = len(data)/2
	#median = sort[N]
	dif = max(avg)-min(avg)
	#print 'The Median: %.12f'%median
	print 'Difference: %.12f'%dif
	
	
def main():
	csv_file ='./Historic_Secured_Property_Tax_Rolls.csv'
	df = pd.read_csv(csv_file,low_memory=False)
	#prop_code = df['Property Class Code']
	a = df['Block and Lot Number']
	b = df['Closed Roll Assessed Improvement Value']
	A = makeDict(a,b)	
	#print A
	#print A
	#getFraction(prop_code)
	getMedian(A)

if __name__ == "__main__":
	main()


				

		