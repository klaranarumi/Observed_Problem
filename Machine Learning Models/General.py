# Processing
from sklearn.model_selection import train_test_split

y = df['koi_disposition_f']

X = df.iloc[:,2:43]
# 70% treino e 30% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=11)

# Classic Models

## Linear Regression

## Logistic Regression

## Naive Bayes

## SVM - Kernel Linear

## SVM - Kernel Sigmoid

## SVM - Kernel Polinomial

## SVM - Kernel RBF

## K-NN

## Decision Tree

## Random Forest

## Gradient Tree Boosting

