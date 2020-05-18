import numpy as np

# simple Linear Discriminant analysis (only 2 class)


def LDA(x1, x2):
    
    # class mean
    mu1 = np.mean(x1, axis=0)
    mu2 = np.mean(x2, axis=0)

    # covariance
    cov1 = np.cov(x1[:,0], x1[:, 1])
    cov2 = np.cov(x2[:,0], x2[:, 1])

    # within class scatter
    sw = cov1 + cov2
    
    # between class scatter
    mu_12 = (mu1 - mu2).reshape(-1, 1)
    sb = np.matmul(mu_12, np.transpose(mu_12))

    # eigenvalue, eigenvector
    sw_inv = np.linalg.inv(sw)
    u, v = np.linalg.eig(np.matmul(sw_inv, sb))



    print('-'*20)
    print('mu1:')
    print(mu1)
    print('mu2:')
    print(mu2)

    print('-'*20)
    print('cov1:')
    print(cov1)
    print('cov2:')
    print(cov2)
    
    print('-'*20)
    print('sw:')
    print(sw)
    print('sb:')
    print(sb)
    print('sw_inv:')
    print(sw_inv)

    print('-'*20)
    print('eigen_value1: {}\neigen_value2: {}'.format(str(u[0]), str(u[1])))
    print('eigen_vector1:')
    print(v[:, 0])
    print('eigen_vector2:')
    print(v[:, 1])



if __name__ == "__main__":
    # class 1 data
    x1 = np.array([[4, 2], [2, 4], [2, 3], [3, 6], [4, 4]])
    # class 2 data
    x2 = np.array([[9, 10], [6, 8], [9, 5], [8, 7], [10, 8]])

    LDA(x1, x2)