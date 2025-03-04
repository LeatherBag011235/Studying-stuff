import time
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.datasets import fetch_openml, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start:.5f} sec")
        return result
    return wrapper

# Load Datasets
@timer
def load_mnist():
    mnist = fetch_openml('mnist_784', version=1)
    X, y = mnist.data / 255.0, mnist.target.astype(int)
    return train_test_split(X, y, test_size=0.2, random_state=42)

@timer
def load_california_housing():
    housing = fetch_california_housing()
    X, y = housing.data, housing.target
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest Classifier
@timer
def rf_classifier(X_train, X_test, y_train, y_test):
    clf = RandomForestClassifier(n_estimators=100, n_jobs=-1)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("RF Classifier Accuracy:", accuracy_score(y_test, y_pred))

# Random Forest Regressor
@timer
def rf_regressor(X_train, X_test, y_train, y_test):
    reg = RandomForestRegressor(n_estimators=100, n_jobs=-1)
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    print("RF Regressor MSE:", mean_squared_error(y_test, y_pred))

# CatBoost Classifier
@timer
def catboost_classifier(X_train, X_test, y_train, y_test):
    clf = CatBoostClassifier(iterations=100, depth=6, verbose=0)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("CatBoost Classifier Accuracy:", accuracy_score(y_test, y_pred))

# CatBoost Regressor
@timer
def catboost_regressor(X_train, X_test, y_train, y_test):
    reg = CatBoostRegressor(iterations=100, depth=6, verbose=0)
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    print("CatBoost Regressor MSE:", mean_squared_error(y_test, y_pred))

# MLP Model for MNIST
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.softmax(self.fc3(x))
        return x

@timer
def train_mlp():
    transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(lambda x: x.view(-1))])
    train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=1000, shuffle=False)
    
    model = MLP()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.NLLLoss()
    
    for epoch in range(3):  # 3 epochs
        for images, labels in train_loader:
            optimizer.zero_grad()
            output = model(images)
            loss = criterion(output, labels)
            loss.backward()
            optimizer.step()
    
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            output = model(images)
            pred = output.argmax(dim=1)
            correct += (pred == labels).sum().item()
            total += labels.size(0)
    
    print(f"MLP Test Accuracy: {correct / total:.4f}")

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_mnist()
    rf_classifier(X_train, X_test, y_train, y_test)
    catboost_classifier(X_train, X_test, y_train, y_test)
    
    X_train, X_test, y_train, y_test = load_california_housing()
    rf_regressor(X_train, X_test, y_train, y_test)
    catboost_regressor(X_train, X_test, y_train, y_test)
    
    train_mlp()

# PC win 11 no Turbo boost
# load_mnist: 3.70313 sec
# RF Classifier Accuracy: 0.9678571428571429
# rf_classifier: 2.34605 sec
# CatBoost Classifier Accuracy: 0.9504285714285714
# catboost_classifier: 34.92314 sec
# load_california_housing: 0.02419 sec
# RF Regressor MSE: 0.25325295521323066
# rf_regressor: 1.00768 sec
# CatBoost Regressor MSE: 0.22586471748100057
# catboost_regressor: 0.40252 sec
# MLP Test Accuracy: 0.9769
# train_mlp: 18.98875 sec

# Old laptop win 10:
# load_mnist: 5.51620 sec
# RF Classifier Accuracy: 0.967
# rf_classifier: 17.20083 sec
# CatBoost Classifier Accuracy: 0.9503571428571429
# catboost_classifier: 302.23807 sec
# load_california_housing: 0.04166 sec
# RF Regressor MSE: 0.25202950675839814
# rf_regressor: 6.48558 sec
# CatBoost Regressor MSE: 0.22586471748100057
# catboost_regressor: 0.80315 sec
# MLP Test Accuracy: 0.9722
# train_mlp: 37.97328 sec

# Pc win 11 Turbo Boost:
# load_mnist: 2.14450 sec
# RF Classifier Accuracy: 0.9667857142857142
# rf_classifier: 1.49566 sec
# CatBoost Classifier Accuracy: 0.9504285714285714
# catboost_classifier: 23.12175 sec
# load_california_housing: 0.00000 sec
# RF Regressor MSE: 0.2571675255243977
# rf_regressor: 0.55462 sec
# CatBoost Regressor MSE: 0.22586471748100057
# catboost_regressor: 0.25019 sec
# MLP Test Accuracy: 0.9746
# train_mlp: 12.62488 sec

# Summary statistics (percentage change from Old Laptop Win 10)
# ------------------------------------------------------------------------------
# Task                     | PC Win 11 No Turbo Boost (sec) | Old Laptop Win 10 (sec) | PC Win 11 Turbo Boost (sec) | % Change (PC Win 11 No Turbo Boost) | % Change (PC Win 11 Turbo Boost)
# -------------------------------------------------------------------------------------------------------------------
# load_mnist               | 3.70313                        | 5.51620                 | 2.14450                      | -32.87%                             | -61.12%
# rf_classifier            | 2.34605                        | 17.20083                | 1.49566                      | -86.36%                             | -91.30%
# catboost_classifier      | 34.92314                       | 302.23807               | 23.12175                     | -88.45%                             | -92.35%
# load_california_housing  | 0.02419                        | 0.04166                 | 0.00000                      | -41.93%                             | -100.00%
# rf_regressor             | 1.00768                        | 6.48558                 | 0.55462                      | -84.46%                             | -91.45%
# catboost_regressor       | 0.40252                        | 0.80315                 | 0.25019                      | -49.88%                             | -68.85%
# train_mlp                | 18.98875                       | 37.97328                | 12.62488                     | -49.99%                             | -66.75%