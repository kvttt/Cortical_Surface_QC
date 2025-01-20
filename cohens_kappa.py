from sklearn.metrics import cohen_kappa_score
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def read_csv_to_y(fn):
    df = pd.read_csv(fn)
    y = df['Score'].fillna(0).values
    return y


if __name__ == '__main__':
    y1 = read_csv_to_y('rater_1.csv')
    y2 = read_csv_to_y('rater_2.csv')
    y3 = read_csv_to_y('rater_3.csv')
    y4 = read_csv_to_y('rater_4.csv')
    mat = np.zeros((4, 4))
    df = [y1, y2, y3, y4]
    for i in range(4):
        for j in range(4):
            mat[i, j] = cohen_kappa_score(df[i], df[j], labels=[1, 2, 3])

    f, axes = plt.subplots(layout='constrained')
    caxes = axes.matshow(mat, cmap='coolwarm', vmin=-1, vmax=1)
    f.colorbar(caxes)
    plt.xticks(range(4), ['Rater 1', 'Rater 2', 'Rater 3', 'Rater 4'])
    plt.yticks(range(4), ['Rater 1', 'Rater 2', 'Rater 3', 'Rater 4'])
    for i in range(4):
        for j in range(4):
            plt.text(j, i, f'{mat[i, j]:.2f}', ha='center', va='center', color='black')
    f.suptitle('Cohen\'s Kappa')
    plt.show()
    f.savefig('kappa.png', dpi=300)
