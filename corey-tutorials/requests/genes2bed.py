import os
import sys
import argparse
import pandas as pd
import mysql.connector
from collections import defaultdict

def main(args):
    """ Args function to run mysql query """
    filename = os.path.abspath(args.list)
    table = args.table
    genome = args.genome
    # output name
    output_p = os.path.dirname(filename)
    output_name = os.path.basename(filename).split(".")[0]
    output = os.path.join(output_p, output_name + ".bed")
    # Create list with genes
    with open(filename) as file:
        genes_list = file.read().rstrip("\n").split(",")
    db = mysql.connector.connect(
        host="genome-mysql.soe.ucsc.edu",
        user="genome",
        database=genome
    )
    mycursor = db.cursor()
    # Query genes intervals from gene_list in UCSC database
    mycursor.execute("SELECT chrom,txStart,txEnd,name2,name,strand,score FROM %s WHERE name2 in ('%s');" % (table, "','".join(genes_list)))
    bed_dict = defaultdict(list)
    for row in mycursor:
        # Create dictionary values
        bed_dict["chr"].append(row[0])
        bed_dict["start"].append(row[1])
        bed_dict["end"].append(row[2])
        bed_dict["gene"].append(row[3])
        bed_dict["transcript"].append(row[4])
        bed_dict["strand"].append(row[5])
        bed_dict["score"].append(row[6])
    db.close()
    # Create dataframe BED
    bed = pd.DataFrame.from_dict(bed_dict)
    bed["source"] = bed["gene"] + "_" + bed["transcript"]
    bed_out = bed[["chr", "start", "end", "source", "score", "strand"]]
    bed_out.to_csv(output, index=False, header=False, sep="\t")
    # Check gene names not found
    diff = list(set(genes_list) - set(bed["gene"].to_list()))
    if len(diff) > 0:
        # Create TXT with genes not found
        with open(output.replace(".bed", "_genes_not_found.txt"), "w") as file:
            file.write(",".join(diff))

if __name__ == "__main__":
    """ Arguments for the main function """
    parser = argparse.ArgumentParser(
        description="Script to create BED file from list of genes", usage='''Usage:
        python genes2bed.py -l /path/to/genes_list.txt''')
    parser.add_argument("-l", "--list", help="TXT file with gene list separated by comma", type=str)
    parser.add_argument("-t", "--table", help="UCSC table to search genes, default=ncbiRefSeqSelect", type=str, nargs='?', default="ncbiRefSeqSelect")
    parser.add_argument("-g", "--genome", help="Version of genome, default=hg38", type=str, nargs='?', default="hg38")
    parser.set_defaults(func=main)
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    args.func(args)