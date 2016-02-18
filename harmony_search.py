import random

nvar = 5
hms = 5
max_iter = 100000
par = 0.4
bw = 0.02
hmcr = 0.9
low = None
high = None
nchv = [None] * nvar
best_fit_history = [None] * (max_iter + 1)
best_harmony = [None] * (nvar + 1)
worst_fit_history = [None] * (max_iter + 1)
hm = [([None] * hms) for x in xrange(0, (nvar + 1))]
generation = 0



def set_bounds(_low, _high):
	global low
	global high

	low = _low
	high = _high

def init():
	global hm
	global nchv

	for i in xrange(0, hms):
		for j in xrange(0, nvar):
			hm[i][j] = random.uniform(low[j], high[j])
			nchv[j] = hm[i][j]
		hm[i][nvar] = fitness(nchv)

def fitness(x):
	l = range(0, len(x))
	fitness = 0
	random.shuffle(l)
	while l:
		fitness += x[l.pop()]
	return fitness

def stop_needed():
	global generation
	global max_iter
	return generation > max_iter

def update_harmony_memory(fitness):
	global worst_fit_history
	global best_fit_history
	global hm

	worst = hm[0][nvar]
	worst_count = 0
	for i in xrange(0, hms):
		if hm[i][nvar] > worst:
			worst = hm[i][nvar]
			worst_count = i

	worst_fit_history[generation] = worst

	if fitness < worst:
		for k in xrange(0, nvar):
			hm[worst_count][k] = nchv[k]
		hm[worst_count][nvar] = fitness

	best = hm[0][nvar]
	best_count = 0
	for i in xrange(0, hms):
		if (hm[i][nvar] < best):
			best = hm[i][nvar]
			best_count = i
	best_fit_history[generation] = best

	if generation > 0 and best != best_fit_history[generation - 1]:
		for k in xrange(0, nvar):
			best_harmony[k] = hm[best_count][k]
		best_harmony[nvar] = best

def memory_consideration(index):
	global nchv
	nchv[index] = hm[random.randrange(0, hms - 1)][index]

def pitch_adjustment(index):
	global nchv
	global bw
	global high
	global low

	random_value = random.random()
	nchv_temp = nchv[index]

	if random_value < 0.5:
		nchv_temp += random_value * bw
		if nchv_temp < high[index]:
			nchv[index] = nchv_temp
	else:
		nchv_temp -= random_value * bw
		if nchv_temp > low[index]:
			nchv[index] = nchv_temp

def set_random_nchv(index):
	global nchv
	nchv[index] = random.uniform(low[index], high[index])

def solve():
	while not stop_needed():
		for i in xrange(0, nvar):
			if (random.random() < hmcr):
				memory_consideration(i)
				if (random.random() < par):
					pitch_adjustment(i)
			else:
				set_random_nchv(i)

		update_harmony_memory(fitness(nchv))
		generation += 1

def main():
	set_bounds([2.0, 3.0, 1.0, 1.0, 1.0], [5.0, 6.0, 2.0, 2.0, 2.0])
	init()
	solve()

if __name__ == '__main__':
	main()
