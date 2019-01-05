def to_rna(dna_strand):
    rna = {'G':'C','C':'G','T':'A','A':'U'}
    compliment = ''
    for strand in dna_strand:
        if strand == 'X':
            break
        compliment += rna[strand]
    return compliment
