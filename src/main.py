import random_mutation as MUTATION

def main():
    print("----------- EVOLUTION INTERFACE -----------------")
    # Checks random mutation in population genetics
    initial_population = int(input("Enter population size : "))
    dna_length = int(input("Enter length of DNA : "))
    generation_turns = int(input("Enter turns of gene : "))
    
    MUTATION.mutation_by_population(dna_length,initial_population,generation_turns)

if __name__ == '__main__':
    main()