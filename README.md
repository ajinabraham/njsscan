# njsscan
**njsscan** is a static application testing (SAST) tool that can find insecure code patterns in your node.js applications using simple pattern matcher from [libsast](https://github.com/ajinabraham/libsast) and syntax-aware semantic code pattern search tool [semgrep](https://github.com/returntocorp/semgrep).

Made with ![Love](https://cloud.githubusercontent.com/assets/4301109/16754758/82e3a63c-4813-11e6-9430-6015d98aeaab.png) in India  [![Tweet](https://img.shields.io/twitter/url?url=https://github.com/ajinabraham/njsscan)](https://twitter.com/intent/tweet/?text=njsscan%20is%20a%20semantic%20aware%20SAST%20tool%20that%20can%20find%20insecure%20code%20patterns%20in%20your%20Node.js%20applications%20by%20%40ajinabraham%20%40OpenSecurity_IN&url=https://github.com/ajinabraham/njsscan)

[![PyPI version](https://badge.fury.io/py/njsscan.svg)](https://badge.fury.io/py/njsscan)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux-green.svg)](https://github.com/ajinabraham/njsscan)
[![License](https://img.shields.io/:license-lgpl3+-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Build](https://github.com/ajinabraham/njsscan/workflows/Build/badge.svg)](https://github.com/ajinabraham/njsscan/actions?query=workflow%3ABuild)

### Support njsscan

* **Donate via Paypal:** [![Donate via Paypal](https://user-images.githubusercontent.com/4301109/76471686-c43b0500-63c9-11ea-8225-2a305efb3d87.gif)](https://paypal.me/ajinabraham)
* **Sponsor the Project:** [![Github Sponsors](https://user-images.githubusercontent.com/4301109/95517226-9e410780-098e-11eb-9ef5-7b8c7561d725.png)](https://github.com/sponsors/ajinabraham)

### e-Learning Courses & Certifications
[![OpSecX Video Course](https://user-images.githubusercontent.com/4301109/82597198-99fa8600-9b76-11ea-8243-c604bc7b06b1.png)](https://opsecx.com/index.php/product/node-js-security-pentesting-and-exploitation/?uid=github) [OpSecX Node.js Security: Pentesting and Exploitation - NJS](https://opsecx.com/index.php/product/node-js-security-pentesting-and-exploitation/?uid=github)

## Installation

`pip install njsscan`

Requires Python 3.7+ and supports only Mac and Linux

## Command Line Options

```bash
$ njsscan
usage: njsscan [-h] [--json] [--sarif] [--sonarqube] [--html] [-o OUTPUT] [-c CONFIG] [--missing-controls] [-w] [-v] [path ...]

positional arguments:
  path                  Path can be file(s) or directories with source code

optional arguments:
  -h, --help            show this help message and exit
  --json                set output format as JSON
  --sarif               set output format as SARIF 2.1.0
  --sonarqube           set output format compatible with SonarQube
  --html                set output format as HTML
  -o OUTPUT, --output OUTPUT
                        output filename to save the result
  -c CONFIG, --config CONFIG
                        Location to .njsscan config file
  --missing-controls    enable missing security controls check
  -w, --exit-warning    non zero exit code on warning
  -v, --version         show njsscan version
```


## Example Usage

```bash
$ njsscan test.js
- Pattern Match ████████████████████████████████████████████████████████████ 1
- Semantic Grep ███████████████████████████ 160

njsscan: v0.1.9 | Ajin Abraham | opensecurity.in
╒═════════════╤═══════════════════════════════════════════════════════════════════════════════════════════════╕
│ RULE ID     │ express_xss                                                                                   │
├─────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
│ OWASP       │ A1: Injection                                                                                 │
├─────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
│ CWE         │ CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')  │
├─────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
│ DESCRIPTION │ Untrusted User Input in Response will result in Reflected Cross Site Scripting Vulnerability. │
├─────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
│ SEVERITY    │ ERROR                                                                                         │
├─────────────┼───────────────────────────────────────────────────────────────────────────────────────────────┤
│ FILES       │ ╒════════════════╤═══════════════════════════════════════════════╕                            │
│             │ │ File           │ test.js                                       │                            │
│             │ ├────────────────┼───────────────────────────────────────────────┤                            │
│             │ │ Match Position │ 5 - 46                                        │                            │
│             │ ├────────────────┼───────────────────────────────────────────────┤                            │
│             │ │ Line Number(s) │ 7: 8                                          │                            │
│             │ ├────────────────┼───────────────────────────────────────────────┤                            │
│             │ │ Match String   │ const { name } = req.query;                   │                            │
│             │ │                │     res.send('<h1> Hello :' + name + "</h1>") │                            │
│             │ ╘════════════════╧═══════════════════════════════════════════════╛                            │
╘═════════════╧═══════════════════════════════════════════════════════════════════════════════════════════════╛
```

## nodejsscan SAST

**nodejsscan**, built on top of **njsscan** provides a full fledged vulnerability management user interface along with other nifty integrations.

![nodejsscan web ui](https://user-images.githubusercontent.com/4301109/83994121-74fe6500-a923-11ea-9ad7-012113f1bb12.png)

See [nodejsscan](https://github.com/ajinabraham/nodejsscan)

## Python API

```python
>>> from njsscan.njsscan import NJSScan
>>> node_source = '/node_source/true_positives/sqli_node.js'
>>> scanner = NJSScan([node_source], json=True, check_controls=False)
>>> scanner.scan()
{
    'templates': {},
    'nodejs': {
        'node_sqli_injection': {
            'files': [{
                'file_path': '/node_source/true_positives/sqli_node.js',
                'match_position': (1, 24),
                'match_lines': (4, 11),
                'match_string': 'var employeeId = req.foo;\n\nvar sql = "SELECT * FROM trn_employee WHERE employee_id = " + employeeId;\n\n\n\nconnection.query(sql, function (error, results, fields) {\n\n    if (error) {\n\n        throw error;\n\n    }\n\n    console.log(results);'
            }],
            'metadata': {
                'owasp': 'A1: Injection',
                'cwe': "CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')",
                'description': 'Untrusted input concatinated with raw SQL query can result in SQL Injection.',
                'severity': 'ERROR'
            }
        }
    },
    'errors': []
}
```

## Configure njsscan

A `.njsscan` file in the root of the source code directory allows you to configure njsscan. You can also use a custom `.njsscan` file using `--config` argument.

```yaml
---
- nodejs-extensions:
  - .js

  template-extensions:
  - .new
  - .hbs
  - ''

  ignore-filenames:
  - skip.js

  ignore-paths:
  - __MACOSX
  - skip_dir
  - node_modules

  ignore-extensions:
  - .jsx

  ignore-rules:
  - regex_injection_dos
  - pug_jade_template

  severity-filter:
  - WARNING
  - ERROR
```

## Suppress Findings

You can suppress findings from javascript source files by adding the comment `// njsscan-ignore: rule_id1, rule_id2` to the line that trigger the findings.

Example:

```javascript
app.get('/some/redirect', function (req, res) {
    var target = req.param("target");
    res.redirect(target); // njsscan-ignore: express_open_redirect
});
```

## CI/CD Integrations

You can enable njsscan in your CI/CD or DevSecOps pipelines.

#### Github Action

Add the following to the file `.github/workflows/njsscan.yml`.

```yaml
name: njsscan
on:
  push:
    branches: [ master, main ]
  pull_request:
    branches: [ master, main ]
jobs:
  njsscan:
    runs-on: ubuntu-latest
    name: njsscan check
    steps:
    - name: Checkout the code
      uses: actions/checkout@v4.2.2
    - uses: actions/setup-python@v5.3.0
      with:
        python-version: '3.12'
    - name: nodejsscan scan
      id: njsscan
      uses: ajinabraham/njsscan-action@master
      with:
        args: '.'
```
Example: [dvna with njsscan github action](https://github.com/ajinabraham/dvna/actions?query=workflow%3Anjsscan)

#### Github Code Scanning Integration

Add the following to the file `.github/workflows/njsscan_sarif.yml`.

```yaml
name: njsscan sarif
on:
  push:
    branches: [ master, main ]
  pull_request:
    branches: [ master, main ]
jobs:
  njsscan:
    runs-on: ubuntu-latest
    name: njsscan code scanning
    steps:
    - name: Checkout the code
      uses: actions/checkout@v4.2.2
    - uses: actions/setup-python@v5.3.0
      with:
        python-version: '3.12'
    - name: nodejsscan scan
      id: njsscan
      uses: ajinabraham/njsscan-action@master
      with:
        args: '. --sarif --output results.sarif || true'
    - name: Upload njsscan report
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: results.sarif
```
![nodejsscan web ui](https://user-images.githubusercontent.com/4301109/99230041-cfe29500-27bc-11eb-8baa-d5b30e21348d.png)


#### Gitlab CI/CD

Add the following to the file `.gitlab-ci.yml`.

```yaml
stages:
    - test
njsscan:
    image: python
    before_script:
        - pip3 install --upgrade njsscan
    script:
        - njsscan .
```
Example: [dvna with njsscan gitlab](https://gitlab.com/ajinabraham/dvna/-/jobs/602110439)


#### Travis CI

Add the following to the file `.travis.yml`.

```yaml
language: python
install:
    - pip3 install --upgrade njsscan
script:
    - njsscan .
```

#### Circle CI

Add the following to the file `.circleci/config.yaml`

```yaml
version: 2.1
jobs:
  njsscan:
    docker:
      - image: cimg/python:3.9.6
    steps:
      - checkout
      - run:
          name: Install njsscan
          command: pip install --upgrade njsscan
      - run:
           name: njsscan check
           command: njsscan .
```

## Docker

### Prebuilt image from [DockerHub](https://hub.docker.com/r/opensecurity/njsscan)

```bash
docker pull opensecurity/njsscan
docker run -v /path-to-source-dir:/src opensecurity/njsscan /src
```

### Build Locally

```
docker build -t njsscan .
docker run -v /path-to-source-dir:/src njsscan /src
```



