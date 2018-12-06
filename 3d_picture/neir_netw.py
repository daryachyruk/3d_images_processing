import numpy
import mnist as mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

# make seed for cycle results
numpy.random.seed(42)

# load data
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# resize data
X_train = X_train.reshape(60000, 784)

# normalize data
X_train = X_train.astype('float32')
X_train /= 255

# transform tags to categories
y_train = np_utils.to_categorical(y_train, 10)

# 0 -> [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 2 -> [0, 0, 1, 0, 0, 0, 0, 0, 0, 0] # only the right element == 1

# create sequential model
model = Sequential()

# add network levels
model.add(Dense(800, input_dim=784, init="normal", activation="relu"))
model.add(Dense(10, init="normal", activation="softmax"))

# compile model
model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
print(model.summary())

#_________training_______________________
# batch_size - size of data portion
# nb_epoch - amount times of teaching (100 times)
model.fit(X_train, y_train, batch_size=200, nb_epoch=100, verbose=1)

#___________working_____________
# work on input data
predictions = model.predict(X_train)

# transform output data
# from categories to tags of classes (num from 0 to 9)
predictions = np_utils.categorical_probas_to_classes(predictions)

# now we can compare
