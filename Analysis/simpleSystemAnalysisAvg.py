import glob 
import pandas as pd
import numpy as np
import matplotlib 
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import seaborn as sns

def main():
	
	#Read in each file of Experiment 1 
	path= r'/user/johankn1/hpcc/simpleSystem/experiment1/*'
	allFiles= glob.glob(path + '/*.csv')
	
	
	frame= pd.DataFrame()
	list_ = []
	
	#Add all of the data to a frame in columns
	for file_ in allFiles:
		data = pd.read_csv(file_ ,index_col=None, header=0)
		data["rep"]= file_.split("/")[-2]
		data["condition"]= 1
		list_.append(data)
		
	frame= pd.concat(list_)
	
	#Plot data
	sns.tsplot(data=frame, time= "update", unit = "rep", value= " ShannonDiversity", condition= "condition" )
	
	#Show Plot
	plt.show()
	
	
	return 0

if __name__ == '__main__':
	main()

