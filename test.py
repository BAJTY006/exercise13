import sequences as sekvence

dna1 = sekvence.DNASequence("platná", "ACGCTAGCTAGC")
dna2 = sekvence.DNASequence("neplatná", "ACGCNTAGCTAGC")  # N = neznámá báze

print(dna1.is_valid())  # True
print(dna2.is_valid())

seq = sekvence.DNASequence("testovací", "acgtagctagc")
print(seq.gc_content())
print(f"délka sekvence: {seq.length()}")
print(f"str{seq.__str__()}")
# dna1 = DNASequence("platná", "ACGCTAGCTAGC")
# dna2 = DNASequence("neplatná", "ACGCNTAGCTAGC")  # N = neznámá báze
#
# print(dna1.is_valid())  # True
# print(dna2.is_valid())  # False

seq.plot_composition()

# dna = DNASequence("mini", "ACCGGGTT")
# print(dna.base_counts())
# dna.plot_composition()
# #
# dna2 = DNASequence("Zkoukška", "actctgtc")
# print(dna2.gc_content())
# print(f"délka sekvence: {dna2.length()}")
# print(f"str{dna2.__str__()}")
# dna2.plot_composition()