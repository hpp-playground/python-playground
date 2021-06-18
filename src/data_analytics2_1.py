import numpy as np

def main():
    A = np.matrixlib.mat([
        [75, -20, -60, 0, 0],
        [0, 25, 0, 0, -20],
        [0, -20, 75, -60, 0],
        [0, -20, 0, 75, 0],
        [-20, 0, 0, 0, 25],
    ])
    Y = np.matrixlib.mat([
        [3],
        [1],
        [3],
        [3],
        [1],
    ])

    print(np.linalg.solve(A,Y))



if __name__ == "__main__":
    main()