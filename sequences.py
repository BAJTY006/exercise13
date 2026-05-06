import matplotlib.pyplot as plt

class Sequence:
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence.upper()   # vždy uložíme velkými písmeny

    def length(self):
        return len(self.sequence)

    def __str__(self):
        return f"[{self.name}] délka={self.length()} nt, začátek: {self.sequence[:8]}..."


class DNASequence(Sequence):
    # def __init__(self, name, sequence):
    #     super().__init__(name, sequence)
    def gc_content(self):
        gc = self.sequence.count("G") + self.sequence.count("C")
        return gc / len(self.sequence)

    def base_counts(self):
        A = self.sequence.count("A")
        C = self.sequence.count("C")
        G = self.sequence.count("G")
        T = self.sequence.count("T")

        result = {"A": A, "C": C, "G": G, "T": T}
        return result

    def plot_composition(self):
        counts = self.base_counts()
        bases = ["A", "C", "G", "T"]
        values = [counts[b] for b in bases]
        colors = ["tab:green", "tab:blue", "tab:orange", "tab:red"]

        plt.figure(figsize=(5, 3))
        plt.bar(bases, values, color=colors, edgecolor="black")
        plt.title(f"Složení bází: {self.name}")
        plt.ylabel("Počet")
        plt.tight_layout()
        plt.show()

    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "T"}

    def to_rna(self):
        return RNASequence(self.name, self.sequence.replace("T", "U"))


class RNASequence(Sequence):
    def is_valid(self):
        return set(self.sequence) <= {"A", "C", "G", "U"}

    def codons(self):
        return [self.sequence[i:i + 3] for i in range(0, len(self.sequence) - 2, 3)]

    def find_start_codon(self):
        return self.sequence.find("AUG")


# print(RNASequence("správná",   "ACGUACGU").is_valid())   # True
# print(RNASequence("s thyminem","ACGTACGU").is_valid() )  # False — T v RNA být nemá
#
# rna = RNASequence("mini", "AUGGCUUAA")
# print(rna.codons())   # ["AUG", "GCU", "UAA"]
#
# rna2 = RNASequence("zbytek", "AUGGCUUA")
# print(rna2.codons())  # ["AUG", "GCU"]   — poslední dvě písmena netvoří celý kodon

rna = RNASequence("gen", "CCAUGGCUUAA")
print(rna.find_start_codon())   # 2   — AUG začíná na indexu 2


# seq = DNASequence("testovací", "acgtagctagc")
# print(seq.gc_content())
# print(f"délka sekvence: {seq.length()}")
# print(f"str{seq.__str__()}")
# dna1 = DNASequence("platná", "ACGCTAGCTAGC")
# dna2 = DNASequence("neplatná", "ACGCNTAGCTAGC")  # N = neznámá báze
#
# print(dna1.is_valid())  # True
# print(dna2.is_valid())  # False
#
# seq.plot_composition()
#
# dna = DNASequence("mini", "ACCGGGTT")
# print(dna.base_counts())
# dna.plot_composition()
# #
# dna2 = DNASequence("Zkoukška", "actctgtc")
# print(dna2.gc_content())
# print(f"délka sekvence: {dna2.length()}")
# print(f"str{dna2.__str__()}")
# dna2.plot_composition()


if __name__ == "__main__":
    dna1 = DNASequence("platná", "ACGCTAGCTAGC")
    dna2 = DNASequence("neplatná", "ACGCNTAGCTAGC")  # N = neznámá báze

    print(dna1.is_valid())  # True
    print(dna2.is_valid())





# print(seq)            # [testovací] délka=11 nt, začátek: ACGTAGCT...
# print(seq.length())   # 11
# print(seq.sequence)   # ACGTAGCTAGC – automaticky převedeno na velká písmena

dna = DNASequence("gen_01", "CCATGGCTTAA")

rna = dna.to_rna()
print(rna)                          # __str__ zděděné ze Sequence
print(rna.is_valid())               # True
print(rna.find_start_codon())       # pozice prvního AUG
print(rna.codons())                 # seznam kodonů