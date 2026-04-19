# GOCODE RECRUITMENT TASK

This project contains a basic test framework along with fully implemented login tests for the Fashionhub Demo App:  
https://hub.docker.com/r/pocketaces2/fashionhub-demo-app

---

## 1. Installation

Install Playwright and pytest:

```bash
pip install pytest-playwright
```

Install Playwright browsers:

```bash
playwright install
```

---

## 2. Clone Repository

Clone the repository via **HTTPS**:

```bash
git clone https://github.com/mbiesiada1988/gocode-technical-challenge.git
```

Clone via **SSH**:

```bash
git clone git@github.com:mbiesiada1988/gocode-technical-challenge.git
```

---

## 3. Running Tests

To run tests, use:

```bash
python -m pytest
```

### Available options:

| Option            | Description |
|------------------|------------|
| `--config`       | Path to the configuration file (default: `config.json`) |
| `--env`          | Target environment. Possible values:<br/>`local` – local Docker instance: http://localhost:4000/fashionhub/<br/>`staging` – staging environment: https://staging-env/fashionhub/<br/>`prod` – production: https://pocketaces2.github.io/fashionhub/<br/>If a different value is provided, it will be treated as a direct URL |
| `--browser_name` | Browser to run tests on:<br/>`chromium` – Chrome/Edge/Opera engine<br/>`webkit` – Safari engine<br/>`firefox` – Firefox engine<br/>Invalid values will cause test execution to fail |
| `--headed`       | Runs tests in headed (GUI) mode (default: `false`) |
| `--slowmo`       | Slows down execution by a given number of milliseconds per action |
| `{file_path}`    | Path to a specific test file (by default all tests are executed) |

**NOTE:** CLI options (`--env`, `--browser_name`) override values defined in the configuration file.

---

### Examples

**Example 1:**
```bash
python -m pytest
```

Runs all tests in headless mode. Browser and environment are loaded from the default config file (`config.json`).

---

**Example 2:**
```bash
python -m pytest --config=config.json --env=local --browser_name=chromium --headed --slowmo=1000 tests/test_smoke_menu.py
```

Runs tests from `test_smoke_menu.py` in headed mode using Chromium on a local environment.  
Each action is slowed down by 1 second.  
Values from the config file are overridden by CLI parameters.

---

**Example 3:**
```bash
python -m pytest --env=https://google.com/ --browser_name=firefox
```

Runs all tests in headless mode using Firefox against the provided URL.

---

## 4. Configuration

Default test execution settings can be defined in a configuration file:

```json
{
  "env": "local",
  "browser": "chromium",
  "environments": {
    "local": "http://localhost:4000/fashionhub/",
    "staging": "https://staging-env/fashionhub/",
    "prod": "https://pocketaces2.github.io/fashionhub/"
  }
}
```

| Key            | Description |
|----------------|-------------|
| `env`          | Environment key defined in `environments` |
| `browser`      | One of:<br/>`chromium`, `webkit`, `firefox` |
| `environments` | Dictionary of environment names and their corresponding URLs |

**NOTE:** CLI options override configuration file values.

---

## 5. Test Description

- `tests/test_e2e_login.py` – full login functionality tests  
  ⚠️**NOTE:** The first test in this file is expected to fail due to insecure HTTP usage and exposed credentials on the page  

- `tests/test_e2e_purchase.py` – placeholder test (framework structure demonstration)  

- `tests/test_func_about.py` – placeholder test  

- `tests/test_func_cart.py` – placeholder test  

- `tests/test_func_home.py` – contains a single homepage link test  

- `tests/test_func_products.py` – placeholder test  

- `tests/test_smoke_menu.py` – smoke tests for all pages  
   ⚠️**NOTE:** The last test in this file is expected to fail due to a console error on the "About" page  


---

## 6. Architecture & Design Decisions

### Test Framework Structure
The project follows a modular and scalable structure typical for Playwright + pytest setups:
- Separation of test types (e2e, functional, smoke)
- Clear naming conventions for test files
- Easy extensibility for adding new test suites

### Configuration Handling
A dual-source configuration approach is implemented:
- **Configuration file (`config.json`)** provides default values
- **CLI arguments** allow dynamic overrides at runtime

Priority logic:
1. CLI parameters (highest priority)
2. Configuration file
3. Default values (fallback)

This ensures flexibility for both local development and CI/CD pipelines.

### Environment Management
Environments are abstracted via a dictionary in the config file:
- Enables easy switching between `local`, `staging`, and `prod`
- Allows passing a custom URL directly via CLI
- Keeps test code environment-agnostic

### Browser Abstraction
Browser selection is handled dynamically:
- Uses Playwright’s built-in browser engines (`chromium`, `firefox`, `webkit`)
- Prevents hardcoding browser-specific logic in tests
- Supports cross-browser testing with minimal effort

### Test Execution Control
Runtime behavior can be adjusted via CLI:
- `--headed` for debugging (visual mode)
- `--slowmo` for step-by-step observation
- File-level execution for targeted test runs

This improves developer experience and debugging efficiency.

### Known Limitations (Intentional)
Some tests are designed to fail:
- To demonstrate error handling
- To highlight issues in the tested application (e.g. insecure HTTP, console errors)

This reflects real-world testing scenarios rather than artificially “green” test suites.

### Design Philosophy
The project prioritizes:
- Simplicity over over-engineering
- Readability and clarity
- Real-world usability (CLI + config support)
- Easy onboarding for new contributors
