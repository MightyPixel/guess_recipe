import pylab

from main import *

PROBS_CROSSOVER = range(1, 10)
PROBS_MUTATION = range(0, 40, 5)
PROBS_SELECTION = range(1, 9)
REPEAT_COUNT = 10

ALL_PROBS = sorted(PROBS_CROSSOVER + PROBS_MUTATION + PROBS_SELECTION)
print ALL_PROBS

values = []

pylab.figure(1)
pylab.title('Crossove (red), Mutation (green), Selection (blue) Probs/Avg population')
pylab.xlabel('%')
pylab.ylabel('Avg Generations')
pylab.grid(True)
lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]

def plot_crossover():
    pylab.title('Crossove (red) Probs/Avg population')
    for prob in PROBS_CROSSOVER:
        results = []
        for i in range(REPEAT_COUNT):
            result = GeneticAlgorithm(GuessRecipe(lasagna, prob_crossover = 0.1 * prob)).run()
            results.append(result)

        values.append(sum(results) / len(results))

    print values
    pylab.plot(PROBS_CROSSOVER, values, 'r--')


def plot_mutation():
    pylab.title('Mutation (green) Probs/Avg population')
    for prob in PROBS_MUTATION:
        results = []
        for i in range(REPEAT_COUNT):
            result = GeneticAlgorithm(GuessRecipe(lasagna, prob_mutation = 0.01 * prob)).run()
            results.append(result)

        values.append(sum(results) / len(results))

    print values
    pylab.plot(PROBS_MUTATION, values, 'g--')


def plot_selection():
    pylab.title('Selection (blue) Probs/Avg population')
    for prob in PROBS_SELECTION:
        results = []
        for i in range(REPEAT_COUNT):
            result = GeneticAlgorithm(GuessRecipe(lasagna, prob_selection = 0.1 * prob)).run()
            results.append(result)

        values.append(sum(results) / len(results))

    print values
    pylab.plot(PROBS_SELECTION, values, 'b--')


# plot_crossover()
# plot_mutation()
plot_selection()

pylab.savefig('allprob')
pylab.show()
