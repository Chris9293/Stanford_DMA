import numpy as mp
import tflearn
from tflearn.datasets import titanic
titanic.download_dataset('titanic_dataset.csv')

from tflearn.data_utils import load_csv
data , labels = load_csv('titanic_dataset.csv' , target_column=0, categorical_labels=True, n_classes=2, columns_to_ignore=[2,7])

for p in data:
    if p[1] == 'female':
        p[1] = 1
    else:
        p[1] = 0

#neural network // HERE
net = tflearn.input_data(shape=[None,6])
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 32)
net = tflearn.fully_connected(net, 2, activation='softmax')
net = tflearn.regression(net)
# TO HERE//

model = tflearn.DNN(net)
model.fit(data, labels, n_epoch=100, batch_size=16, show_metric=True)

jack = [3, 'Jack Dawson', 'male', 19, 0,0, 'N/A', 5.000]
print (model.predict([[3, 0, 19, 0, 0, 5.0]]))

total = 0
count = 0
for fare in data:
    total += float(fare[5])
    count += 1
average = total/count
print(average)