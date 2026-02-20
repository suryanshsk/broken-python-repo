```python
# src/importer.py
import math

def square_root(x):
    return math.sqrt(x)
```

```python
# tests/test_importer.py
from src.importer import square_root

def test_square_root():
    assert square_root(4) == 2

```