import random
def generate_initial_gene(length_of_genes) -> str:
    return ''.join([random.choice('ACGT') for _ in range(length_of_genes)])

def mutation(gene_structure) -> str:
    list_of_gene = list(gene_structure)
    position = random.randint(1,len(gene_structure)-1)
    random_gene = random.choice('ACGT')
    list_of_gene[position] = random_gene
    return "".join(list_of_gene)

def mutation_by_population(length_of_genes,size_of_population,generation_turns) -> bool:
    initial_generation = [generate_initial_gene(length_of_genes) for _ in range(size_of_population)]
    temp_generation = initial_generation
    for count in range(generation_turns+1):
        print(f"generation {count} : {temp_generation}")
        temp_generation = [mutation(genes) for genes in temp_generation]
    return True









