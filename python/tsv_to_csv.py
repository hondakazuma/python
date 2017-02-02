# -*- coding: utf-8 -*-

import pandas as pd
import csv
import glob

# 読み込み元のディレクトリ/ファイル名
READ_DIR = "/Users/hondakazuma/python/samplefile/"
READ_FILE = "*.tsv"
# 出力先のディレクトリ/ファイル名
OUTPUT_DIR = "/Users/hondakazuma/python/samplefile/tsv_to_csv/"
OUTPUT_FILE = "mergesample.csv"

def tsv_to_csv():

    readdir = READ_DIR
    readfile = READ_FILE

    outdir = OUTPUT_DIR
    outfile = OUTPUT_FILE

    # READ_DIR 配下のファイルをリストとして保持
    want_to_read_files = glob.glob(readdir + readfile)

    # dataframeの初期化
    df_want = pd.DataFrame()

    # ファイルの読み込みと連結
    for i in range(0, len(want_to_read_files)):
        read_file = want_to_read_files[i]
        df_read_file = pd.read_csv(read_file, header=None)
        df_want = pd.concat([df_want, df_read_file])
    # dataframeにindexを振り直す。
    # drop=True とすることでもとのインデックスを削除しつつ、新しくindexを付与する
    df_want = df_want.reset_index(drop = True)
    print(df_want)

    #   ファイル出力
    df_want.to_csv(outdir + outfile)


tsv_to_csv()
