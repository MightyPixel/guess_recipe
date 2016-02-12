import pylab

from main import *

PROBS = range(5, 9)
REPEAT_COUNT = 3

pylab.figure(1)
pylab.title('Crossover Prob/Avg population')
pylab.xlabel('Crossover Prob')
pylab.ylabel('Avg Generations')
pylab.grid(True)

lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]

values = []
for i in PROBS:
    results = []
    for i in range(REPEAT_COUNT):
        result = GeneticAlgorithm(GuessRecipe(lasagna, prob_crossover = 0.1 * i)).run()
        results.append(result)

    values.append(sum(results) / len(results))

print values
pylab.plot(values, PROBS)
pylab.savefig('crossoverprob')
pylab.show()
