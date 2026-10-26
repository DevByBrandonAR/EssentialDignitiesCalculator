import matplotlib.pyplot as plt 
import numpy as np 

def plot(scores): 
	values = [] 
	categories =  [ "♄", "♃" ,"♂" , "☉" , "♀" , "☿" , "☽" ]
	names = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"]
	for name in names:
		values.append(scores[name]) 
	for i in range(len(values)):
		if values[i] < 0: 
			values[i] = 0 
	angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
	values += values[:1]
	angles += angles[:1] 
	fig, ax = plt.subplots(figsize=(6,6), subplot_kw={'projection':'polar'})
	ax.plot(angles, values,linewidth=2, linestyle='solid')
	ax.fill(angles, values, alpha=0.25)
	ax.set_xticks(angles[:-1])
	ax.set_xticklabels(categories)
	ax.set_ylim(0,max(values) + 1)
	ax.set_yticks([i for i in range(max(values) + 1)])
	ax.set_yticklabels([str(i) for i in range(max(values) + 1)], color='gray', size=8)
	plt.show()
