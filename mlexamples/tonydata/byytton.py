from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import seaborn as sb


print("!")

data = datasets.load_breast_cancer()

print(data)

label_names = data["target_names"]
print(label_names)

labels = data["target"]
print(labels)

feature_names = data["feature_names"]
print(feature_names)

features = data["data"]
print(features)

train, test, train_labels, test_labels = train_test_split(features, labels, test_size = 0.33)

randomForest = RandomForestClassifier();

model = randomForest.fit(train, train_labels)

ennusteet = randomForest.predict(test)

print("Ennusteet: 0=hyvälaatuinen, 1=huonolaatuinen")
print(ennusteet)

accuracyScore = metrics.accuracy_score(test_labels, ennusteet)
print("Score: ", accuracyScore)

precisionScore = metrics.precision_score(test_labels, ennusteet)

recallScore = metrics.recall_score(test_labels, ennusteet)

print("Precision: ", precisionScore)
print("Recall: ", recallScore)

confusionMatrix = metrics.confusion_matrix(test_labels, ennusteet)
print(confusionMatrix)

sb.heatmap(confusionMatrix)