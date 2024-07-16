import json
import requests
from zipfile import ZipFile
from io import BytesIO

def get_ocr_result():
  # Requesting API calls that return byte encoded results
  ocr_response = requests.get('url_ocr_api_call')
  
  # Decoding bytes
  with ZipFile(BytesIO(ocr_response.content), 'r') as my_zip:
    zipped_json = my_zip.filelist[0]
    with my_zip.open(zipped_json, 'r') as json_file:
        pages = json.loads(json_file.read())

    # Saving result in JSON format
    filename = 'filename.json'
    with open(outputPath + "\\" + filename, 'w') as f:
            json.dump(pages, f)

def parse_json(doc_id):
    filename = 'filename.json'
    with open(filename) as f:
        data = json.load(f)
        return data[0]['ExtractedText'].lower()

if __name__ == '__main__':
    TP = sum(1 for (doc1, p_val), (doc2, r_val) in zip(classif_own, classif_regex) if p_val == 1 and r_val == 1)
    TN = sum(1 for (doc1, p_val), (doc2, r_val) in zip(classif_own, classif_regex) if p_val == 0 and r_val == 0)
    FN = sum(1 for (doc1, p_val), (doc2, r_val) in zip(classif_own, classif_regex) if p_val == 1 and r_val == 0)
    FP = sum(1 for (doc1, p_val), (doc2, r_val) in zip(classif_own, classif_regex) if p_val == 0 and r_val == 1)

    accuracy = (TP + TN) / (TP + FP + FN + TN)
    precision = TP / (TP + FP) if (TP + FP) != 0 else 0
    recall = TP / (TP + FN) if (TP + FN) != 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0
  
    print("Confusion Matrix:")
    print(f"{'':<10}{'Predicted 1':<15}{'Predicted 0':<15}") # :< left align with field witdh of 15 spaces
    print(f"{'Actual 1':<10}{TP:<15}{FN:<15}") # :^ center align :> center align
    print(f"{'Actual 0':<10}{FP:<15}{TN:<15}")

    print("\nMetrics:")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1_score:.2f}")
    # Ewample of output
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
