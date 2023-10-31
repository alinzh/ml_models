from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

# divided dataset into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=0)

# define an instance of a class
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# prediction classes on test data
y_pred = clf.predict(X_test)

tree.plot_tree(clf)

accuracy = accuracy_score(y_test, y_pred)
print(accuracy)

