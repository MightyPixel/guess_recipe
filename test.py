import pylab

from main import *

PROBS_CROSSOVER = range(1, 9)
PROBS_MUTATION = range(5, 40, 5)
PROBS_SELECTION = range(1, 9)
REPEAT_COUNT = 5

values = []

def plot_crossover():
    pylab.figure(1)
    pylab.title('Crossover Prob/Avg population')
    pylab.xlabel('Crossover Prob')
    pylab.ylabel('Avg Generations')
    pylab.grid(True)

    lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]

    values = []
    for i in PROBS_CROSSOVER:
        results = []
        for i in range(REPEAT_COUNT):
            result = GeneticAlgorithm(GuessRecipe(lasagna, prob_crossover = 0.1 * i)).run()
            results.append(result)

        values.append(sum(results) / len(results))

    print values
    pylab.plot(sorted(values), PROBS_CROSSOVER, 'r--')
    pylab.savefig('crossoverprob')
    pylab.show()

def plot_mutation():
    pylab.figure(1)
    pylab.title('Mutation Prob/Avg population')
    pylab.xlabel('Mutation Prob')
    pylab.ylabel('Avg Generations')
    pylab.grid(True)

    lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]

    values = []
    for i in PROBS_MUTATION:
        results = []
        for i in range(REPEAT_COUNT):
            result = GeneticAlgorithm(GuessRecipe(lasagna, prob_mutation = 0.01 * i)).run()
            results.append(result)

        values.append(sum(results) / len(results))

    print values
    pylab.plot(sorted(values), PROBS_MUTATION, 'r--')
    pylab.savefig('mutationprob')
    pylab.show()


def plot_selection():
    pylab.figure(1)
    pylab.title('Selection Prob/Avg population')
    pylab.xlabel('Selection Prob')
    pylab.ylabel('Avg Generations')
    pylab.grid(True)

    lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]

    values = []
    for i in PROBS_SELECTION:
        results = []
        for i in range(REPEAT_COUNT):
            result = GeneticAlgorithm(GuessRecipe(lasagna, prob_selection = 0.1 * i)).run()
            results.append(result)

        values.append(sum(results) / len(results))

    print values
    pylab.plot(sorted(values), PROBS_SELECTION, 'r--')
    pylab.savefig('mutationprob')
    pylab.show()




plot_mutation()
