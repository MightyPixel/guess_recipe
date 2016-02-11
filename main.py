import random

from genetic_algorithm import GeneticAlgorithm
from genetic_function import GeneticFunction


ALL_PRODUCTS = [
    "salt",
    "sweet Italian sausage",
    "lean ground beef",
    "minced onion",
    "garlic",
    "tomatoes",
    "sugar",
    "water",
    "rice",
    "butter",
    "eggs",
    "lemon",
    "salmon",
    "apple",
    "bread",
    "olives",
    "cheese",
    "milk",
    "paper",
    "chocolate",
    "flour",
    "vanilla",
    "blueberries",
    "nuts",
    "crackers",
    "margarine",
    "prunes",
    "soda",
    "corn",
    "celery",
    "orange",
    "bacon",

    # operations
    "bake",
    "fry",
    "chill",
    "wash",
    "mix",
    "boil",
    "steam",
    "melt",
    "spray",
    "chop",
]


class GuessRecipe(GeneticFunction):
        def __init__(self, target,
                     limit=900, size=400,
                     prob_crossover=0.9, prob_mutation=0.2):
            self.target = self.products_to_chromo(target)
            self.counter = 0

            self.limit = limit
            self.size = size
            self.prob_crossover = prob_crossover
            self.prob_mutation = prob_mutation

        # GeneticFunctions interface impls
        def probability_crossover(self):
            return self.prob_crossover

        def probability_mutation(self):
            return self.prob_mutation

        def initial(self):
            return [self.random_chromo() for j in range(self.size)]

        def fitness(self, chromo):
            # larger is better, matched == 0
            return -sum(abs(c - t) for c, t in zip(chromo, self.target))

        def check_stop(self, fits_populations):
            self.counter += 1
            best_match = list(sorted(fits_populations))[-1][1]
            fits = [f for f, ch in fits_populations]
            best = max(fits)
            worst = min(fits)
            ave = sum(fits) / len(fits)
            print(
                "[G %3d] score=(%4d, %4d, %4d): %r" %
                (self.counter, best, ave, worst,
                    self.chromo_to_products(best_match)))

            return best == 0 or  self.counter >= self.limit

        def parents(self, fits_populations):
            while True:
                father = self.tournament(fits_populations)
                mother = self.tournament(fits_populations)
                yield (father, mother)
                pass
            pass

        def crossover(self, parents):
            father, mother = parents
            index1 = random.randint(1, len(self.target) - 2)
            index2 = random.randint(1, len(self.target) - 2)
            if index1 > index2: index1, index2 = index2, index1
            child1 = father[:index1] + mother[index1:index2] + father[index2:]
            child2 = mother[:index1] + father[index1:index2] + mother[index2:]
            return (child1, child2)

        def mutation(self, chromosome):
            index = random.randint(0, len(self.target) - 1)
            vary = random.randint(0, len(ALL_PRODUCTS) - 1)
            mutated = list(chromosome)
            mutated[index] = vary
            return mutated

        # internals
        def tournament(self, fits_populations):
            alicef, alice = self.select_random(fits_populations)
            bobf, bob = self.select_random(fits_populations)
            return alice if alicef > bobf else bob

        def select_random(self, fits_populations):
            return fits_populations[random.randint(0, len(fits_populations)-1)]

        def products_to_chromo(self, products):
            indices = [ALL_PRODUCTS.index(product) for product in products]
            # id = "".join(map(str, indices))
            # return [ord(ch) for ch in id]
            return indices

        def chromo_to_products(self, chromo):
            # return "".join(chr(max(1, min(ch, 255))) for ch in chromo)

            return [ALL_PRODUCTS[index] for index in chromo]

        def random_chromo(self):
            return [random.randint(0, len(ALL_PRODUCTS) - 1) for i in range(len(self.target))]

        pass

if __name__ == "__main__":
    lasagna = ["tomatoes", "steam", "cheese", "melt", "sweet Italian sausage", "mix", "garlic"]
    GeneticAlgorithm(GuessRecipe(lasagna)).run()
