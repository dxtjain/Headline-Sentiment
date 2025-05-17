"""
Headline Sentiment Analyzer - Neural Network Model
This script builds a deep learning model for news headline sentiment analysis
using TF-IDF vectorization and neural networks.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load and prepare the dataset
print("Loading dataset...")
Doc = pd.read_csv("all-data.csv", header=None)
lines = Doc[1]

# TF-IDF Vectorization
print("Performing TF-IDF vectorization...")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(lines)
analyze = vectorizer.build_analyzer()
print(f"Number of features: {len(vectorizer.get_feature_names())}")

# Convert to dense array and create DataFrame
X_array = X.toarray()
final = pd.DataFrame(X_array, columns=vectorizer.get_feature_names())

# Feature selection - remove rare terms
print("Selecting important features...")
final = final.drop(final.columns[final.sum() < 0.5], axis=1)
print(f"Features after selection: {final.shape[1]}")

# Prepare inputs and labels
all_inputs = final[final.columns].values
all_labels = Doc[0].values

# Encode labels
encoder = LabelEncoder()
encoder.fit(all_labels)
encoded_Y = encoder.transform(all_labels)
dummy_y = np_utils.to_categorical(encoded_Y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    all_inputs, dummy_y, test_size=0.2, shuffle=True, random_state=42
)

# Build neural network model
print("Building neural network model...")
model = Sequential()
model.add(Dense(64, input_dim=all_inputs.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))  # Additional layer
model.add(Dense(16, activation='relu'))  # Additional layer
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
print("Training the model...")
history = model.fit(X_train, y_train, epochs=30, validation_split=0.1, verbose=1)

# Evaluate model
print("\nModel Evaluation:")
pred_train = model.predict(X_train)
scores = model.evaluate(X_train, y_train, verbose=0)
print('Accuracy on training data: {:.2f}% \nError on training data: {:.2f}%'.format(scores[1]*100, (1-scores[1])*100))   
 
pred_test = model.predict(X_test)
scores2 = model.evaluate(X_test, y_test, verbose=0)
print('Accuracy on test data: {:.2f}% \nError on test data: {:.2f}%'.format(scores2[1]*100, (1-scores2[1])*100))

# Save the model
model.save('headline_model.h5')
print("Model saved as headline_model.h5")

# Visualize training history
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend()

plt.tight_layout()
plt.savefig('training_history.png')
plt.show()

print("Analysis complete. Results saved.")

