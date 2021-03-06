#!/usr/bin/env python3

from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

def genbank_generator(original, negative_strand= None):

    """
    Add the new crispr features to the original anotation file
    """
    # Some IO requirements:
    if not negative_strand:
        results = open("../results/data1_positive_unique.txt", "r")
        fo = "../results/gb/positive_crispr.gbk"
        st = 1
    else:
        results = open("../results/data1_negative_unique.txt", "r")
        fo = "../results/gb/NC_000912_ThIns_crispr.gbk"
        st = -1

    # Iterate over the results
    original_records = list(SeqIO.parse(original, "gb"))

    for result in results:
        start = 0
        end = 0

        result = result.split("\t")
        position = int(result[0])

        start = position - 19
        end = position

        if start <= 0:
            start += 816394

        for record in original_records:
            print(start, end)
            record.features.append(SeqFeature(FeatureLocation(start, end), type = "crispr", strand = st))
            SeqIO.write(record, fo, "gb")

if __name__ == "__main__":
    # We will do each strand separately to include the information correctl
    genbank_generator("../ref_data/NC_000912transposoninsertions.gbk", negative_strand = False)
    genbank_generator("../results/gb/positive_crispr.gbk", negative_strand = True)
