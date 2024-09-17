# Compute Confusion matrix
# The documents have to be in the same order in both lists
TP = sum(1 for (_doc, ground_truth_value), (_doc, predicted_value) in zip(classif_own, classif_regex) if ground_truth_value == 1 and predicted_value == 1)
TN = sum(1 for (_doc, ground_truth_value), (_doc, predicted_value) in zip(classif_own, classif_regex) if ground_truth_value == 0 and predicted_value == 0)
FN = sum(1 for (_doc, ground_truth_value), (_doc, predicted_value) in zip(classif_own, classif_regex) if ground_truth_value == 1 and predicted_value == 0)
FP = sum(1 for (_doc, ground_truth_value), (_doc, predicted_value) in zip(classif_own, classif_regex) if ground_truth_value == 0 and predicted_value == 1)

# Compute Confusion matrix metrics
accuracy = (TP + TN) / (TP + FP + FN + TN)
precision = TP / (TP + FP) if (TP + FP) != 0 else 0
recall = TP / (TP + FN) if (TP + FN) != 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0


print("Confusion Matrix:")
print(f"{'':<10}{'Predicted 1':<15}{'Predicted 0':<15}") # :< left align with field witdh of 15 spaces
print(f"{'Actual 1':<10}{TP:<15}{FN:<15}") # :^ center align 
print(f"{'Actual 0':<10}{FP:<15}{TN:<15}") # :> right align

print("\nMetrics:")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1_score:.2f}")

# Example of output
'''
Confusion Matrix:
          Predicted 1    Predicted 0
Actual 1  120            7
Actual 0  4              19

Metrics:
Accuracy: 0.93
Precision: 0.97
Recall: 0.94
F1 Score: 0.96
'''
