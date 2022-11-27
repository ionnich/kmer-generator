# %%
import random


def generate_kmers(dna_sequence, k):
    """
    A function that generates all the kmers of length k from a dna sequence
    """

    kmers = []
    pivot = 0

    def generate(kmers, dna_sequence, k, pivot):
        while (pivot + k <= len(dna_sequence)):
            candidate = dna_sequence[pivot:pivot+k]
            kmers.append(candidate)
            pivot += 1
        return kmers

    return generate(kmers, dna_sequence, k, pivot)


# %%
def create_dna_sequence(bases, length):
    """
    Generates a random dna sequence of the desired length using the bases provided
    """
    sequence = ""
    for i in range(length):
        # get a random base
        sequence += bases[random.randint(0, len(bases) - 1)]

    return sequence

# %%
