from processing_data import processing_df
from annotate_data import annotate_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse
import re


def main(exam_df, stem, word, freq, output):
    df = pd.read_csv(exam_df)
    print("Loading the dataframe.")
    df = processing_df(df, stem, word, freq)
    print("Processing the dataframe.")
    df = annotate_data(df)
    df.sort_values(by=['word', 'gdex'], ascending=[True, False], inplace=True)
    print("Saving the dataframe.")
    df.to_csv(output, index=False)
    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compiling dataset for evaluating good dictionary examples")
    parser.add_argument("--exam_df", type=str, help="Path to the dataframe with examples")
    parser.add_argument("--word", type=str, help="Full word")
    parser.add_argument("--stem", type=str, help="Full word's stem")
    parser.add_argument("--freq", type=str, help="Occurrence of the word")
    parser.add_argument("--output", type=str, help="Path to save the dataframe")

    args = parser.parse_args()

    main(args.exam_df, args.word, args.stem, args.freq, args.output)
