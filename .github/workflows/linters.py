name: Styles

on: push

jobs:
  lint:
    name: Lint code

    runs-on: ubuntu-18.04

    strategy:
      matrix:
        python-version: [3.10]

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2.3.2
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install Poetry
        uses: snok/install-poetry@v1
        with:
          version: "1.1.12"
          virtualenvs-in-project: true

      - name: Set up cache
        uses: actions/cache@v2
        id: cache
        with:
          path: .venv
          key: venv-${{ runner.os }}-py-${{ matrix.python-version }}-poetry-${{ hashFiles('poetry.lock') }}

      - name: Ensure cache is healthy
        if: steps.cache.outputs.cache-hit == 'true'
        run: poetry run pip --version >/dev/null 2>&1 || rm -rf .venv

      - name: Install dependencies
        run: poetry install --no-interaction

      - name: Run linters
        run: poetry run ./scripts/lint
