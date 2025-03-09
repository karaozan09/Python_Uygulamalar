import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

# 1) Telefon Fiyat Tahmini için Model Oluşturma

# Veri Yükleme
data = pd.read_csv("data.csv")
X = data.drop("price_range", axis=1)
y = data["price_range"]

# Eğitim ve Test Setine Ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Oluşturma
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Başarım Değerlendirme
print("Classification Report:")
print(classification_report(y_test, y_pred))

# 2) Çapraz Doğrulama
cv_scores = cross_val_score(model, X, y, cv=10)
print("Cross Validation Scores:", cv_scores)
print("Average CV Score:", np.mean(cv_scores))

# 3) Özellik Çıkartma
X_new = X.drop(["blue", "fc", "int_memory", "ram", "wifi"], axis=1)
X_train_new, X_test_new, y_train, y_test = train_test_split(X_new, y, test_size=0.2, random_state=42)
model.fit(X_train_new, y_train)
y_pred_new = model.predict(X_test_new)

print("Classification Report (Özellik Çıkartıldı):")
print(classification_report(y_test, y_pred_new))

# 4) Diyabet Verisi ile YSA Modeli
# Diyabet veri seti yükleme
from sklearn.datasets import load_diabetes

X_diabetes, y_diabetes = load_diabetes(return_X_y=True)
X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_diabetes, y_diabetes, test_size=0.2, random_state=42)

# YSA Modeli
model_nn = Sequential()
model_nn.add(Dense(64, input_dim=X_train_d.shape[1], activation='relu'))
model_nn.add(Dense(32, activation='relu'))
model_nn.add(Dense(1, activation='sigmoid'))

model_nn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model_nn.fit(X_train_d, y_train_d, validation_data=(X_test_d, y_test_d), epochs=50, batch_size=10)

# Eğitim ve Doğrulama Kaybı Grafiği
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title("Model Kayıp Grafiği")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()

# 5) ROC Eğrisi
y_pred_proba = model_nn.predict(X_test_d)
fpr, tpr, _ = roc_curve(y_test_d, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color='blue', label='ROC Curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc='lower right')
plt.show()