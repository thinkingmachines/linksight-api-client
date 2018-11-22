# LinkSight API Client

## Install

```sh
pip install git+https://github.com/thinkingmachines/linksight-api-client.git
```

## Usage

```python
import pandas as pd
import linksight

ls = linksight.Client(<API_TOKEN>)
ds = ls.create_dataset(open('some.csv'))
match = ds.match(
    source_bgy_col='Barangay',
    source_municity_col='City',
    source_prov_col='Province',
)
df = pd.read_csv(match['matched_dataset']['file'])
```
