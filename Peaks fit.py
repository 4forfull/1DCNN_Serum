from pandas import read_csv
import numpy as np
import scipy.signal as ss


def vsraw(file_path):
    df1 = read_csv(file_path, header=None, sep="\t")
    df1.columns = ['w', 'i']

    vector = [rows.i for index, rows in df1.iterrows()]
    indices1 = ss.find_peaks_cwt(vector, np.arange(1, 30))

    value2 = []
    for a in indices1:
        value = df1.w.loc[a]
        value = int(value)
        value2.append(value)

    with open("Raman Peaks.txt", "w") as file:
        for item in value2:
            file.write(str(item) + "\n")


if __name__ == "__main__":
    file_path = 'D:/pythonjinjie/serum_hp_software/demo/negative.txt'
    vsraw(file_path)