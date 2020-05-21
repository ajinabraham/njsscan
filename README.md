# njsscan
**njsscan** is a static application testing (SAST) tool that can find insecure code patterns in your node.js applications using simple pattern matcher from [libsast](https://github.com/ajinabraham/libsast) and powerful syntax-aware semantic code pattern search tool [semgrep](https://github.com/returntocorp/semgrep).

[![PyPI version](https://badge.fury.io/py/njsscan.svg)](https://badge.fury.io/py/njsscan)
[![platform](https://img.shields.io/badge/platform-osx%2Flinux-green.svg)](https://github.com/ajinabraham/njsscan)
[![License](https://img.shields.io/:license-lgpl2.1-blue.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.en.html)
[![python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/)

[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ajinabraham/njsscan.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ajinabraham/njsscan/context:python)
[![Requirements Status](https://requires.io/github/ajinabraham/njsscan/requirements.svg?branch=master)](https://requires.io/github/ajinabraham/njsscan/requirements/?branch=master)
[![Build](https://github.com/ajinabraham/njsscan/workflows/Build/badge.svg)](https://github.com/ajinabraham/njsscan/actions?query=workflow%3ABuild)

### e-Learning Courses & Certifications
[![OpSecX Video Course](https://user-images.githubusercontent.com/4301109/82597198-99fa8600-9b76-11ea-8243-c604bc7b06b1.png)](https://opsecx.com/index.php/product/node-js-security-pentesting-and-exploitation/?uid=github) [OpSecX Node.js Security: Pentesting and Exploitation - NJS](https://opsecx.com/index.php/product/node-js-security-pentesting-and-exploitation/?uid=github)

## Installation

`pip install njsscan`

Requires Python 3.6+ and supports only Mac and Linux

## Command Line Options

```bash
$ njsscan
usage: njsscan [-h] [--json] [-o OUTPUT] [--missing-controls] [-v]
               [path [path ...]]

positional arguments:
  path                  Path can be file(s) or directories with source code

optional arguments:
  -h, --help            show this help message and exit
  --json                set output format as JSON
  -o OUTPUT, --output OUTPUT
                        output filename to save the result
  --missing-controls    enable missing security controls check
  -v, --version         show njsscan version
```


## Sample Usage

```bash
$ njsscan xss_node.js
- Pattern Match ████████████████████████████████████████████████████████████ 1
- Semantic Grep ████████████████████████████████████████████████████████████ 53

======================================================================================================
RULE ID: express_xss
OWASP: A1: Injection
CWE: CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
DESCRIPTION: Untrusted User Input in Response will result in Reflected Cross Site Scripting Vulnerability.
SEVERITY: ERROR
======================================================================================================

__________________FILES___________________________


File: xss_node.js
Match Position: 5 - 37
Line Number(s): 5: 6
Match String:     var html = "Hello" + req.query.name + ". How are you?"

    res.write('Response</br>' + html);
```


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


## Configure njsscan

A `.njsscan` file in the root of the source code directory allows you to configure njsscan.

```
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

```

## Suppress Findings

You can suppress findings from javascript source files by adding the comment `//ignore: rule_id1, rule_id2` to the line that trigger the findings.

Example:

```javascript
app.get('/some/redirect', function (req, res) {
    var target = req.param("target");
    res.redirect(target); //ignore: express_open_redirect
});
```
