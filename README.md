# A01095149_A5.2
Ejercicio de programación 2 y análisis estático

## Run program:
```console 
python compute_sales.py priceCatalogue.json salesRecord.json`

==== Sales Report ====
Total Sales Cost: $4,182.41
Processing Time: 0.0000 seconds

Errors Encountered:
"Product 'other' not found in price catalogue."
"Product 'mouse' not found in price catalogue."
```

## Lint
```console 
pylint compute_sales.py`

compute_sales.py:1:0: C0114: Missing module docstring (missing-module-docstring)
compute_sales.py:15:11: W0718: Catching too general exception Exception (broad-exception-caught)
```

## Flake8
```console
flake8 compute_sales.py --statistics`

compute_sales.py:2:80: E501 line too long (97 > 79 characters)
compute_sales.py:34:80: E501 line too long (85 > 79 characters)
compute_sales.py:37:80: E501 line too long (84 > 79 characters)
compute_sales.py:73:80: E501 line too long (82 > 79 characters)
compute_sales.py:75:80: E501 line too long (83 > 79 characters)
5     E501 line too long (97 > 79 characters)
```