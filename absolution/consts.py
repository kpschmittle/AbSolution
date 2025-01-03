import enum


class ClusteringMethods(enum.Enum):
    linclust = "linclust"
    linclust_man = "linclust_man"
    mmseqs = "mmseqs"
    mmseqs_man = "mmseqs_man"
    hamming = "hamming"
    levenshtein = "levenshtein"
    clonotyping = "clonotyping"
    uniques = "uniques"

