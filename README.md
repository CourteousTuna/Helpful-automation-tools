# Helpful-automation-tools

Random codes that I've made to make life easier.

### [Automation of URLs opening](./web_automate-url-opening.py)

Open multiple URLs simultaneously using Selenium with a list of document IDs. 
This is particularly useful when the URLs follow a generic format, such as url/document_id.pdf. 
You can add multiple drivers and iterate through them, allowing for the concurrent opening of multiple browser windows.

### [Byte decoding](./byte-decoding-to-json.py)

Decode the byte response from an API call into an associated JSON object. The JSON object is then saved and parsed to extract relevant fields.

### [Transpose Excel file using Pandas](./excel_transpose-horizontal-lines-of-different-sizes.py)

If your excel looks like this:
```
    column 1    column 2    column 3    column 1    column 2    column 3    column 1    column 2    column 3
id_1    x          x           x           y          y           y
id_2    z          z           z
id_3    w          w           w           t          t           t           s          s           s
```
The output will look like:
```
    column 1    column 2    column 3
id_1    x          x           x 
id_1    y          y           y 
id_2    z          z           z 
id_3    w          w           w 
id_3    t          t           t 
id_3    s          s           s 
```

### [Stats using Pandas on Excel file](./excel_stats-using-pandas.py)

Uses the Pandas to process and analyze data from a CSV file. Performs several operations:

1. Data Extraction
2. Data Transformation
3. Filtering
4. Grouping and Counting
5. Boolean Masking
6. Average Calculation


### [Nice format for confusion matrix](./confusion-matrix.py)

Example of output:

```
Confusion Matrix:
          Predicted 1    Predicted 0
Actual 1  120            7
Actual 0  4              19

Metrics:
Accuracy: 0.93
Precision: 0.97
Recall: 0.94
F1 Score: 0.96
```
