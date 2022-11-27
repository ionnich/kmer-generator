from data_structures import hash_table as hashing


def get_unique_kmers(kmer_distribution):
    """
    Creates a kmer distribution composed of only unique kmers
    """
    unique_kmers = []
    for kmer in kmer_distribution:
        # if the kmer only appears once, add it to the list
        if kmer[1] == 1:
            unique_kmers.append(kmer)

    return unique_kmers


def get_most_common_kmers(kmer_distribution, n):
    """
    Creates a list of the n most common kmers
    """
    most_common_kmers = []

    for _ in range(n):
        highest_count = 0
        most_common_kmer = None
        for kmer in kmer_distribution:
            if kmer[1] > highest_count and kmer not in most_common_kmers:
                highest_count = kmer[1]
                most_common_kmer = kmer

        if most_common_kmer:
            most_common_kmers.append(most_common_kmer)

    return most_common_kmers


def parse_table(table: hashing.hash_table, kmer_list):
    """
    Parses the hash table and returns a list of tuples containing the kmer and the count
    """

    kmer_distribution = []

    unique_kmers = set(kmer_list)

    for kmer in unique_kmers:
        if table.search(kmer) is not None:
            kmer_distribution.append((kmer, table.search(kmer)))

    return kmer_distribution


def get_kmers_with_count(kmer_distribution, count):
    """
    Creates a list of kmers whose occurrences are equal to the count
    """
    kmers_with_count = []
    for kmer in kmer_distribution:
        if kmer[1] == count:
            kmers_with_count.append(kmer)

    return kmers_with_count


def parse_math_expression(expression):
    """
    Parses a math expression and returns the result
    """

    num = 0

    # if expression contains ^, then it is a power
    if "^" in expression:
        # split the expression into the base and the exponent
        base = int(expression.split("^")[0])
        power = int(expression.split("^")[1])
        return base ** power

    # if expression contains *, then it is a multiplication
    if "*" in expression:
        # split the expression into the two factors
        factor1 = int(expression.split("*")[0])
        factor2 = int(expression.split("*")[1])
        return factor1 * factor2

    num = int(expression)
    return num


def get_inputs():
    """
    Gets user input for kmer distribution generation
    """

    alphabet = input("Enter the dna alphabet: ")
    dna_length = (input("Enter the length of the dna: "))
    k_mer = input("Enter the length of the kmer: ")

    dna_length = parse_math_expression(dna_length)
    k_mer = parse_math_expression(k_mer)

    # return an object containing the alphabet, dna length, and kmer length

    return {
        "alphabet": alphabet,
        "dna_length": dna_length,
        "kmer_length": k_mer
    }
