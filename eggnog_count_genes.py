import argparse
import pandas as pd

def count_non_empty_genes(excel_file):
    # 엑셀 파일 읽기
    df = pd.read_excel(excel_file)

    # 각 열에서 '-'이 아닌 유전자 개수 세기
    non_empty_GO = df[df['GOs'] != '-']['query'].nunique()
    non_empty_EC = df[df['EC'] != '-']['query'].nunique()
    non_empty_KEGG_ko = df[df['KEGG_ko'] != '-']['query'].nunique()
    non_empty_KEGG_Pathway = df[df['KEGG_Pathway'] != '-']['query'].nunique()

    # 결과 출력
    print("Non-empty genes in GOs column:", non_empty_GO)
    print("Non-empty genes in EC column:", non_empty_EC)
    print("Non-empty genes in KEGG_ko column:", non_empty_KEGG_ko)
    print("Non-empty genes in KEGG_Pathway column:", non_empty_KEGG_Pathway)

if __name__ == "__main__":
    # 커맨드 라인 인자 파서 생성
    parser = argparse.ArgumentParser(description='Count non-empty genes in various columns of an Excel file')
    parser.add_argument('input_file', type=str, help='Path to the input Excel file')

    # 커맨드 라인 인자 파싱
    args = parser.parse_args()

    # 인자로 입력한 파일명으로 함수 호출
    count_non_empty_genes(args.input_file)
