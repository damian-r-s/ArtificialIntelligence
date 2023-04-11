import numpy as np
from keras.datasets import mnist

nTraining = 60000
nTest = 10000

(xtrn, ytrn), (xtst, ytst) = mnist.load_data()

idx = np.argsort(np.random.random(ytrn.shape[0]))
xtrn = xtrn[idx]
ytrn = ytrn[idx]

idx = np.argsort(np.random.random(ytst.shape[0]))
xtst = xtst[idx]
ytst = ytst[idx]

np.save("mnist_train_images.npy", xtrn)
np.save("mnist_train_labels.npy", ytrn)
np.save("mnist_test_images.npy", xtst)
np.save("mnist_test_labels.npy", ytst)

xtrnv = xtrn.reshape((nTraining, 28*28))
xtstv = xtst.reshape((nTest, 28*28))
np.save("mnist_train_vectors.npy", xtrnv)
np.save("mnist_test_vectors.npy", xtstv)

idx = np.argsort(np.random.random(28*28))
for i in range(nTraining):
    xtrnv[i, :] = xtrnv[i, idx]
    
for i in range(nTest):
    xtstv[i, :] = xtstv[i, idx]
np.save("mnist_train_scrambled_vectors.npy", xtrnv)
np.save("mnist_test_scrambled_vectors.npy", xtstv)

t = np.zeros((nTraining, 28, 28))
for i in range(nTraining):
    t[i, :, :] = xtrnv[i,:].reshape((28, 28))
    
np.save("mnist_train_scrambled_images.npy", t)
t = np.zeros((nTest, 28, 28))
for i in range(nTest):
    t[i, :, :] = xtstv[i,:].reshape((28, 28))
np.save("mnist_test_scrambled_images.npy", t)