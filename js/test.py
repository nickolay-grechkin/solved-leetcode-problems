import pandas as pd

tab = pd.read_excel(
    "https://github.com/nadiinchi/voronovo_seminar_materials/blob/master/base_track/seminars/scoring.xls?raw=true"
)

tab.head()

print(tab.dtypes)