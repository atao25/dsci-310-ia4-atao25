# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd
from IPython.display import Markdown, display
from tabulate import tabulate
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
```{python}
#| label: tbl-horses-sd
#| tbl-cap: "Standard deviation of historical (1906-1972) horse populations for each Canadian province."

horses_sd_table = pd.read_csv("../results/horses_sd.csv")
largest_sd = horses_sd_table["Province"].values[0]
horses_sd_table
# horses_sd_table = pd.read_csv("../results/horses_sd.csv")
# largest_sd = horses_sd_table['Province'].values[0]
# Markdown(horses_sd_table.to_markdown(index = False))


#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
