import statistics
import math
import numpy as np


def get_mean(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		mean (float): Mean value
	'''
	map(int, data)
	mean = sum(data) / len(data)
	return mean


def get_median(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		median (float): Median value
	'''
	data.sort()
	median = statistics.median(data)
	return median


def get_mode(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		mode (float): Mode value
	'''
	mode = statistics.mode(data)
	return mode


def get_pop_variance(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		pop_variance (float): Population variance value
	'''
	pop_variance = statistics.pvariance(data, get_mean(data))
	return pop_variance


def get_sam_variance(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		sam_variance (float): Sample variance value
	'''
	sam_variance = statistics.variance(data, get_mean(data))
	return sam_variance


def get_pop_sd(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		pop_sd (float): Populations standard deviation value
	'''
	pop_sd = statistics.pstdev(data)
	return pop_sd


def get_sam_sd(data):
	'''
	Args:
		data (list): List of floats

	Returns:
		sam_sd (float): Sample's standard deviation value
	'''
	sam_sd = statistics.stdev(data)
	return sam_sd


def get_zscore(x, mean, sd):
	'''
	Args:
		x (float): Raw score value
		mean (float): Mean value
		sd (float): Standard deviation

	Returns:
		z_score (float): Z-score value
	'''
	z_score = ((x - mean) / sd)
	return z_score


def get_percentile(data, p):
	'''
	Args:
		data (list): List of floats
		p (float): Percentile value

	Returns:
		percentile (float): Percentile value
	'''
	percentile = np.percentile(data, p) 
	return percentile


def get_iqr(data):
	'''
	Args:
		data (list): List of floats
		
	Returns:
		iqr (float): Interquartile range value
	'''
	q3 = get_percentile(data, 75)
	q1 = get_percentile(data, 25)
	iqr = (q3 - q1)
	return iqr


def get_five_num_summary(data):
	'''
	Args:
		data (list): List of floats
		
	Returns:
		summary (float): Five number summary value
	'''
	d_min = min(data)
	q1 = get_percentile(data, 25)
	median = get_median(data)
	q3 = get_percentile(data, 75)
	d_max = max(data)
	summary = str(d_min) + " " + str(q1) + " " + str(median[1]) + " " + str(q3) + " " + str(d_max)
	return summary


def get_combination(n, r):
	'''
	Args:
		n (int): The set or population
		r (int): Subset of n or sample set
	Returns:
		combination (int): Combination value
	'''
	f = math.factorial
	combination = f(n) // f(r) //  f(n-r)
	return combination


def get_permutation(n, r):
	'''
	Args:
		n (int): The set or population
		r (int): Subset of n or sample set
	Returns:
		permutation (int): Permutation value
	'''
	f = math.factorial
	permutation = f(n) // f(n-r)
	return permutation