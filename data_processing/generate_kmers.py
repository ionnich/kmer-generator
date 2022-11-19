# %%
# this function is a recursive function that imitates the factorial operation
import random


def generate_kmers(dna_sequence, k):

    kmers = []
    pivot = 0

    def generate(kmers, dna_sequence, k, pivot):
        if (len(dna_sequence) < k):
            return kmers

        candidate = dna_sequence[pivot:pivot+k]
        kmers.append(candidate)

        return generate(kmers, dna_sequence[1:], k, pivot)

    return generate(kmers, dna_sequence, k, pivot)


# %%
# this function generates a random DNA sequence


def create_dna_sequence(bases, length):
    sequence = ""
    for i in range(length):
        # get a random base
        sequence += bases[random.randint(0, len(bases) - 1)]

    return sequence

# %%
