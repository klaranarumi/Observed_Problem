# Pre-Processing

from sklearn.model_selection import train_test_split

y = df['y']
X = df.iloc[:,2:10]

## 70% treino e 30% teste
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

# Model-Performace

from sklearn.metrics import roc_curve
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print('Precisão do Naive Bayes: ',precision)
print('Revocação do Naive Bayes: ',recall)

y_pred_proba = gnb.predict_proba(X_test)[::,1]
fpr, tpr, _ = roc_curve(y_test,  y_pred_proba)

plt.plot(fpr,tpr,color='#F08080')
plt.title('Curva ROC do Model')
plt.ylabel('Taxa de Verdadeiro Positivo')
plt.xlabel('Taxa de Falso Positivo')
plt.show()
