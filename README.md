# Introducing Lite-syntax

**The easiet way to create syntax highlighters for lite-xl.**

### Suppose you have to make a syntax highlighter for clojure.

- Create a syntax.yaml file and put data inside it like this:

```yaml
name: Clojure
file: ["%.clojure$"]

comment: "//.*"

block-comment: []

patterns:
  - pattern: [";;.*"]
    type: ["comment"]

  - pattern: [";.*"]
    type: ["comment"]

  - pattern: ['#"', '"', '\\']
    type: ["string"]

  - pattern: ["-?0x%x+"]
    type: ["number"]

  - pattern: ["[!%#%$%%&*+./%<=>%?@\\%^|%-~:]"]
    type: ["operator"]

  - pattern: ["[%a_'][%w_']*"]
    type: ["normal"]

keywords:
    - def
    - defn
    - str
    - fn
    - println

keywords2:
    - require
    - "true"
    - "false"

literal:
    - nil
    - int
```

- Now, run the compiler.py file on it and it will generate this:

```lua
-- Generated using https://github.com/RohanVashisht1234/rohansyntax
-- mod-version:3
local syntax = require "core.syntax"
syntax.add {
name = "Clojure",
block_comment = {},
files = {
   "%.clojure$",
},
patterns = {
    { pattern = {';;.*'}, type = {'comment'} },
    { pattern = {';.*'}, type = {'comment'} },
    { pattern = {'#"', '"', '\\\\'}, type = {'string'} },
    { pattern = {'-?0x%x+'}, type = {'number'} },
    { pattern = {'[!%#%$%%&*+./%<=>%?@\\%^|%-~:]'}, type = {'operator'} },
    { pattern = {"[%a_'][%w_']*"}, type = {'normal'} },
},
symbols = {
    ['def'] = 'keyword',
    ['defn'] = 'keyword',
    ['str'] = 'keyword',
    ['fn'] = 'keyword',
    ['println'] = 'keyword',
    ['require'] = 'keyword2',
    ['true'] = 'keyword2',
    ['false'] = 'keyword2',
    ['nil'] = 'literal',
    ['int'] = 'literal',
},
}
```

- Isn't that easy?

## Contribution:
   - Feel free to open a pr or an issues.

## License:
    GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007

