import os
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix


def evaluate(model, test_generator, class_indices=None):
    # reset generator and predict
    test_generator.reset()
    preds = model.predict(test_generator, verbose=1)
    y_pred = np.argmax(preds, axis=1)
    y_true = test_generator.classes

    if class_indices:
        inv_map = {v: k for k, v in class_indices.items()}
        labels = [inv_map[i] for i in range(len(inv_map))]
    else:
        labels = None

    print("Classification Report:")
    print(classification_report(y_true, y_pred, target_names=labels))
    print("Confusion Matrix:")
    cm = confusion_matrix(y_true, y_pred)
    print(cm)
    return cm

if __name__ == '__main__':
    print("Evaluation script placeholder")

if __name__ == '__main__':
    print("Evaluation script placeholder")
