import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score

cancer_data = load_breast_cancer()
cancer_data.feature_names

cancer_data.target

df = pd.DataFrame(data=cancer_data.data, columns=cancer_data.feature_names)
df['target'] = cancer_data.target
df.head()

df.target.value_counts()

lr = LogisticRegression(class_weight='balanced')
trainX,testX,trainY,testY = train_test_split(cancer_data.data, cancer_data.target)
lr.fit(trainX,trainY)

pred = lr.predict(testX)

accuracy_score(y_pred=pred,y_true=testY)

confusion_matrix(y_pred=pred,y_true=testY)

df.corr()

from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier(n_neighbors=6)


neigh.fit(trainX, trainY)

pred_knn = neigh.predict(testX)

accuracy_score(y_pred=pred_knn,y_true=testY)

from sklearn.svm import SVC

 model_svm = SVC()

 model_svm.fit(trainX, trainY)

pred_svm = model_svm.predict(testX)

accuracy_score(y_pred=pred_svm,y_true=testY)
