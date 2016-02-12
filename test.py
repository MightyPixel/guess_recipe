import pylab

from main import *


pylab.figure(1)
pylab.title('Crossover Prob/Avg population')
pylab.xlabel('Crossover Prob')
pylab.ylabel('Avg Generations')

lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]

values = []
for i in range(1, 9):
    results = GeneticAlgorithm(GuessRecipe(lasagna, prob_crossover = 0.1 * i)).run()
    sizes = [len(generation) for generation in results]
    values.append(sum(sizes) / len(sizes))

pylab.plot(values, range(1, 9))
# pylab.savefig('crossoverprob')
pylab.show()
