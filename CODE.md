## Glossary
- `connection: psycopg2._psycopg.connection`
- `CaseType: covid_data.types.CaseType`
- `Aggregations: covid_data.types.Aggregations`
- `CaseType: covid_data.types.CaseType`
- `OnConflictStrategy: covid_data.types.OnConflictStrategy`
- `OrderBy: covid_data.types.OrderBy`
- `PlaceProperty: covid_data.types.PlaceProperty`
- `PlaceTable: covid_data.types.PlaceTable`
- `PlaceType: covid_data.types.PlaceType`

## `covid_data.db`

```python
def get_db(
    user: str = None,
    passwd: str = None,
    host: str = None,
    port: str = None,
    db: str = None,
) -> connection:
"""
Returns a connection to the database. That connection has to be closed manually. The connection config can be passed as parameters to the functon or with env variables (required if used as CLI). The env variables are:

POSTGRES_USER
POSTGRES_PASS
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
"""
```

```python
def close_db(conn: connection) -> Callable
"""
Receives a connection and returns a lambda that closed the connection once called. This is done this way in order to be able to pass this function as a callback to `ExitStack` and close it automatically once the function is over.
"""
```

## `covid_data.db.queries`

```python
def place_exists(
    place: str, engine: connection, table: PlaceTable = PlaceTable.COUNTRY
) -> Union[str, None]:
"""
Given a place name and a table, returns its ID or none if not exits
"""
```

```python
def get_country_by_alpha2(country: str, engine: connection) -> Optional[dict]:
"""
Given an alpha2 code, return a country
"""
```

```python
def get_country_by_alpha3(country: str, engine: connection) -> Optional[dict]:
"""
Given an alpha3 code, return a country
"""
```

```python
def get_province_by_alpha2(province: str, engine: connection) -> Optional[dict]:
"""
Given an alpha2 code, return a province
"""
```

```python
def get_county_by_alpha2(county: str, engine: connection) -> Optional[dict]:
"""
Given an alpha2 code, return a county
"""
```

```python
def get_country_by_id(country_id: str, engine: connection) -> Optional[dict]:
"""
Given an id, return a country
"""
```

```python
def get_province_by_id(province_id: str, engine: connection) -> Optional[dict]:
"""
Given an id, return a province
"""
```

```python
def get_province_by_name(province: str, engine: connection) -> Optional[dict]:
"""
Given a name, return a country
"""
```

```python
def get_county_by_id(county_id: str, engine: connection) -> Optional[dict]:
"""
Given an id, return a county
"""
```

```python
def row_to_dict(
    rows: Iterable, table_or_cols: Union[str, Iterable[str]], engine: connection
) -> list[dict]:
"""
Given an array of rows and a table or a column lists, transform the rows to an array of dicts, with columns as keys
"""
```

```python
def ensure_array(element) -> List:
"""
Given an object, ensure it's an array
"""
```

```python
def create_country(country: dict, engine: connection) -> str:
"""
Given a dict with all country data, insert it in the database
"""
```

```python
def create_province(province: dict, engine: connection) -> str:
"""
Given a dict with all province data, insert it in the database
"""
```

```python
def create_county(county: dict, engine: connection) -> str:
"""
Given a dict with all county data, insert it in the database
"""
```

```python
def get_cases_by_country(
    country_id: int, engine: connection, case_type: CaseType = None
) -> List[Dict]:
"""
Given a dict with all country data, insert it in the database
"""
```

```python
def get_cases_by_province(
    province_id: int, engine: connection, case_type: CaseType = None
) -> List[Dict]:
"""
Given a province id, return all the cases from that provicen, filtered by type if provided
"""
```

```python
def get_cases_by_filters_query(
    country_id: int = None,
    province_id: int = None,
    date: datetime = None,
    date_lte: datetime = None,
    date_gte: datetime = None,
    case_type: CaseType = None,
    aggregation: list[Aggregations] = [],
    limit: int = None,
    sort: list[str] = [],
) -> Dict[str, Any]:
"""
Returns a query that matches all the filters passed. The returned query is splitted so that the caller can manipulate it before executing. The return dict is in the form:

{
    "select": select,
    "from": from_,
    "query": query,
    "params": tuple(params),
    "columns": tuple(columns),
}
"""
```

```python
def get_cum_cases_by_date(
    engine: connection,
    date: datetime = None,
    date_lte: datetime = None,
    date_gte: datetime = None,
    case_type: CaseType = None,
) -> List[Dict]:
"""
Returns the cummulative sum of cases aggregated by date. Filtered by date and type if provided
"""
```

```python
def get_cum_cases_by_date_country(
    engine: connection,
    country_id: int,
    date: datetime = None,
    date_lte: datetime = None,
    date_gte: datetime = None,
    case_type: CaseType = None,
) -> List[Dict]:
"""
Returns the cummulative sum of cases aggregated by date and contry. Filtered by date and type if provided
"""
```

```python
def get_cum_cases_by_country(
    engine: connection,
    date: datetime = None,
    date_lte: datetime = None,
    date_gte: datetime = None,
    case_type: CaseType = None,
) -> List[Dict]:
"""
Returns the cummulative sum of cases aggregated by country. Filtered by date and type if provided
"""
```

```python
def get_cum_cases_by_province(
    engine: connection,
    date: datetime = None,
    date_lte: datetime = None,
    date_gte: datetime = None,
    case_type: CaseType = None,
    country_id: int = None,
) -> List[Dict]:
"""
Returns the cummulative sum of cases aggregated by province. Filtered by date and type if provided
"""
```

```python
def create_case(
    case: dict,
    engine: connection,
    conflict_strategy: OnConflictStrategy = OnConflictStrategy.REPLACE,
) -> bool:
"""
Given all the data regarding a case, create it. Also takes a replace strategy that can be set to replace or upsert.
"""
```

```python
def get_all_countries(
    engine: connection, name: str = None, near: list[float] = []
) -> list[dict]:
"""
Get all countries filtered by name if provided and ordered by distance to `near`
"""
```

```python
def get_all_provinces(engine: connection) -> list[dict]:
"""
Get all provinces
"""
```

```python
def get_provinces_by_country(engine: connection, country_id: int) -> list[dict]:
"""
Get all provinces that belongs to a specific country
"""
```

```python
def insert_api_key(engine: connection, hashed_key: str) -> bool:
"""
Creates an api key
"""
```

```python
def check_api_key(engine: connection, hashed_key: str) -> bool:
"""
Check if the incoming key exists
"""
```
