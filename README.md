<img src="logo.png" alt="proselint logo" width="200">

[![Build Status](https://travis-ci.org/amperser/proselint.svg)](https://travis-ci.org/amperser/proselint)
[![Build status](https://ci.appveyor.com/api/projects/status/hfgv05nkjxkg2gcc/branch/master?svg=true)](https://ci.appveyor.com/project/suchow/proselint-knwyf/branch/master)
[![Code Climate](https://codeclimate.com/repos/5538989ee30ba0793100090f/badges/e10a2fe18a9256d69e2a/gpa.svg)](https://codeclimate.com/repos/5538989ee30ba0793100090f/feed)
[![Coverage Status](https://coveralls.io/repos/github/amperser/proselint/badge.svg?branch=master)](https://coveralls.io/github/amperser/proselint?branch=master)
[![Dependency Status](https://gemnasium.com/amperser/proselint.svg)](https://gemnasium.com/amperser/proselint)
[![License](https://img.shields.io/badge/License-BSD-blue.svg)](https://en.wikipedia.org/wiki/BSD_licenses)

`proselint`, a linter for prose.

### Installation

```
pip install proselint
```

### Plugins for other software

`proselint` is available on:

- [x] A [demo editor](http://proselint.com/write)
- [x] [Sublime Text](https://github.com/amperser/proselint/tree/master/plugins/sublime/SublimeLinter-contrib-proselint)
- [x] [Atom Editor](https://github.com/smockle/linter-proselint) (thanks to [Clay Miller](https://github.com/smockle)).
- [x] [Emacs via Flycheck](https://github.com/amperser/proselint/tree/master/plugins/flycheck) (thanks to [Aaron Jacobs](https://github.com/atheriel))
- [x] [Vim](https://github.com/amperser/proselint/tree/master/plugins/vim) (thanks to [Matthias Bussonnier](https://github.com/Carreau))
- [x] [Phabricator's `arc` CLI](https://github.com/google/arc-proselint) (thanks to [Jeff Verkoeyen](https://github.com/jverkoey))
- [x] [Danger](https://github.com/dbgrandi/danger-prose) (thanks to [David Grandinetti](https://github.com/dbgrandi) and [Orta Therox](https://github.com/orta)) 
- [x] [Visual Studio Code](https://github.com/ppeszko/vscode-proselint) (thanks to [Patryk Peszko](https://github.com/ppeszko))
- [x] [coala](https://github.com/coala-analyzer/bear-docs/blob/master/docs/ProseLintBear.rst) (thanks to the [coala Development Group](https://github.com/coala-analyzer))  

### Usage

Suppose you had a document `text.md` with the following text:

```
John is very unique.
```

You can run `proselint` over the document using the command line:

```bash
❯ proselint text.md
```

This prints a list of suggestions to stdout, one per line. Each suggestion has the form:

```bash
text.md:<line>:<column>: <check_name> <message>
```

For example,

```bash
text.md:0:10: wallace.uncomparables Comparison of an uncomparable: 'unique' cannot be compared.
```

The command-line utility can also print suggestions in JSON using the `--json` flag. In this case, the output is considerably richer:

```javascript
{
    // Type of check that output this suggestion.
    check: "wallace.uncomparables",

    // Message to describe the suggestion.
    message: "Comparison of an uncomparable: 'unique' cannot be compared.",

    // The person or organization giving the suggestion.
    source: "David Foster Wallace"

    // URL pointing to the source material.
    source_url: "http://www.telegraph.co.uk/a/9715551"

    // Line where the error starts.
    line: 0,

    // Column where the error starts.
    column: 10,

    // Index in the text where the error starts.
    start: 10,

    // Index in the text where the error ends.
    end: 21,

    // start - end
    extent: 11,

    // How important is this? Can be "suggestion", "warning", or "error".
    severity: "warning",

    // Possible replacements.
    replacements: [
        {
            value: "unique"
        }
    ]
}
```

### Running Automated Tests

Automated tests are included in the `proselint/tests` directory. To run these tests locally, use the test runner [nose](http://nose.readthedocs.io/en/latest/) and run the following commands:
```bash
cd tests/
nosetests 
```
and watch the output. Nose is compatible with Python versions 2.7, 3.3, 3.4 and 3.5. 

All automated tests in `tests/` are run as part of each submitted pull request, including newly added tests. 

### License

The project is licensed under the BSD license.
