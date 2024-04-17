import pandas as pd

list_of_dicts = [{'feature1': 1, 'feature2': 2, 'target': 'A'},
                 {'feature1': 2, 'feature2': 3, 'target': 'A'},
                 {'feature1': 3, 'feature2': 4, 'target': 'B'},
                 {'feature1': 4, 'feature2': 5, 'target': 'B'},
                 {'feature1': 5, 'feature2': 6, 'target': 'B'}]

df = pd.DataFrame(list_of_dicts)
