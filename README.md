# text2sqlite

Convert CSV files to SQLite

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-Apr%2C%2019%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Requirements

```bash
pip install tqdm
```

or

```bash
pip install -r requirements.txt
```

```python
import sqlite3
import csv
from tqdm import tqdm
```

## How to run

```python
csv_file = "data1.csv"
db_name = "data1.db"
table_name = "datatable1"

import_csv_to_sqlite(csv_file, db_name, table_name)
```
