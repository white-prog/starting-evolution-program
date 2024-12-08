import random_mutation

def main():
    print("           EVOLUTION INTERFACE                   ")
    initial_population = int(input("Enter population size : "))
    dna_length = int(input("Enter length of DNA : "))
    generation_turns = int(input("Enter turns of gene : "))
    random_mutation.mutation_by_population(dna_length,initial_population,generation_turns)

if __name__ == '__main__':
    main()