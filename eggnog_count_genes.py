import argparse
import pandas as pd

def count_non_empty_genes(excel_file):
    # load_file
    df = pd.read_excel(excel_file)

    # find
    df['KEGG_Pathway'] = df['KEGG_Pathway'].fillna('')

    # '-' except, count
    non_empty_GO = df[df['GOs'] != '-']['query'].nunique()
    non_empty_EC = df[df['EC'] != '-']['query'].nunique()
    non_empty_KEGG_ko = df[df['KEGG_ko'] != '-']['query'].nunique()
    non_empty_KEGG_Pathway = df[df['KEGG_Pathway'].apply(lambda x: x.strip() != '-')]['query'].nunique()

    # Output display
    print("Non-empty genes in GOs column:", non_empty_GO)
    print("Non-empty genes in EC column:", non_empty_EC)
    print("Non-empty genes in KEGG_ko column:", non_empty_KEGG_ko)
    print("Non-empty genes in KEGG_Pathway column:", non_empty_KEGG_Pathway)

if __name__ == "__main__":
    # parser
    parser = argparse.ArgumentParser(description='Count non-empty genes in various columns of an Excel file')
    parser.add_argument('input_file', type=str, help='Path to the input Excel file')

    # commandline parser
    args = parser.parse_args()

    # function_display
    count_non_empty_genes(args.input_file)
