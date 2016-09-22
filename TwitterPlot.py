# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# The methods in this modules are for plotting of twitter data.
# Data passed in must be dictionary type.
# if data is {string:int, string:int...}, use functions starting with generic
# if data is {int: int, int: int ...} and want to arrange x-axil in keys' order, use number_bar_plot

def generic_bar_plot(D, num_shown=5, xlabel="", ylabel="", title=""):
	sorted_D = sorted(D.items(), key=lambda t: t[1], reverse=True)
	print(sorted_D)
	x, y = [], []
	for pair in sorted_D[:num_shown]:
		x.append(pair[0])
		y.append(pair[1])
	plt.bar(range(len(y)), y, align='center', width=0.5)
	plt.xticks(range(len(x)), x)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()

def generic_pie_plot(D, num_shown=5, include_others=True,
					startangle=90,shadow=True, autopct='%1.1f%%', 
					xlabel=None, ylabel=None, title=None):
	sorted_D = sorted(D.items(), key=lambda t: t[1], reverse=True)
	print(sorted_D)
	colors = ['r','m','c','b','g']*5
	colors = colors[:num_shown]
	labels = []
	slices = []
	explode = [0]*(num_shown)
	if include_others == True:
		sum_total = 0
		for pair in sorted_D:
			sum_total += pair[1]
		shown_total = 0
		for pair in sorted_D[:num_shown-1]:
			labels.append(pair[0])
			slices.append(pair[1])
			shown_total += pair[1]
		labels.append('Others')
		slices.append(sum_total-shown_total)
	else:
		for pair in sorted_D[:num_shown]:
			labels.append(pair[0])
			slices.append(pair[1])
	plt.pie(slices,labels=labels,colors = colors,startangle = startangle, 
				shadow = True, explode = explode, autopct = autopct)
	if xlabel==None and ylabel==None and title==None:
		plt.show()
	elif xlabel==None and ylabel==None:
		plt.title(title)
		plt.show()
	else:
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)
		plt.show()


def number_bar_plot(D, xlabel="", ylabel="", title=""):
	sorted_D = sorted(D.items(), key=lambda t: t[0])
	print(sorted_D)
	x, y = [], []
	for pair in sorted_D:
		x.append(pair[0])
		y.append(pair[1])
	plt.bar(x, y, align='center', width=0.5)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()


