# GeoJSON.io Test Automation
Playwright test framework for testing geojson.io using Page Object Model.

## Project Structure

```
HERE-geojson/
├── src/
│   └── geojson_tests/
│       ├── __init__.py
│       └── pages/
│           ├── __init__.py
│           ├── base_page.py
│           └── geojson_page.py
├── tests/
│   ├── conftest.py
│   └── test_geojson.py
├── pytest.ini
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
# Run all tests (headless by default)
pytest tests -v

# Run with a visible browser window
pytest tests -v --headed
```

## Test Example

```python
def test_navigate_to_geojson_io(geojson_page):
    geojson_page.open_geojson_io()
    assert "geojson.io" in geojson_page.get_url()
```
