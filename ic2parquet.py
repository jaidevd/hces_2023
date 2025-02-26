import yaml
import pandas as pd

with open('item_codes.yaml', 'r') as f:
    item_codes = yaml.safe_load(f)

payload = []
for section in item_codes:
    for item_name, item_code in section['items'].items():
        payload.append({
            "item_name": item_name,
            "item_code": item_code,
            "section": section['section'],
            "questionnaire": section['questionnaire']
        })

df = pd.DataFrame.from_records(payload)
df.set_index('item_code', verify_integrity=True, inplace=True)
df.to_parquet('05_readable/item_codes.parquet')
