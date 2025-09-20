# GeoJSON.io Test Automation
Playwright test framework for testing geojson.io using Page Object Model.

## Project Structure

```
HERE-geojson/
├── src/geojson_tests/
│   ├── pages/                     # Page objects
│   │   ├── base_page.py
│   │   └── geojson_page.py
│   └── config/
│       └── test_config.py
├── tests/integration/             # Test files
│   ├── conftest.py
│   └── test_geojson.py
└── requirements.txt
```

## Setup

```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install browser
playwright install chromium
```

## Running Tests

```bash
# Run all tests
pytest tests -v

# Run with visible browser
pytest tests -v -s
```

## Test Example

```python
def test_navigate_to_geojson_io(geojson_page):
    geojson_page.open_geojson_io()
    page_info = geojson_page.get_page_info()
    assert "geojson.io" in page_info["url"]
```