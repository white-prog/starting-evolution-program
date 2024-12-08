import random
def generate_initial_gene(length_of_genes) -> str:
    return ''.join([random.choice('ACGT') for _ in range(length_of_genes)])

def mutation(gene_structure) -> str:
    list_of_gene = list(gene_structure)
    position = random.randint(1,len(gene_structure)-1)
    random_gene = random.choice('ACGT')
    list_of_gene[position] = random_gene
    return "".join(list_of_gene)

def mutation_by_population(length_of_genes,size_of_population,generation_turns) -> dict:
    #try for taking manual input of initial generation from API or user
    initial_generation = [generate_initial_gene(length_of_genes) for _ in range(size_of_population)]
    temp_generation = initial_generation
    generation_dictionary = {}
    for count in range(generation_turns + 1):
        generation_dictionary[count] = temp_generation
        print(f"generation {count} : {temp_generation}")
        temp_generation = [mutation(genes) for genes in temp_generation]
    return generation_dictionary


if __name__ == "__main__":
    # Example usage of the module
    print("=== Genetic Mutation Simulation ===")
    length_of_genes = 10  # Length of each gene
    size_of_population = 5  # Number of individuals in the population
    generation_turns = 3  # Number of generations to simulate

    print("\nStarting mutation simulation...\n")
    mutation_by_population(length_of_genes, size_of_population, generation_turns)
    print("\n=== Simulation Complete ===")








