-- mod-version:3
local syntax = require "core.syntax"
syntax.add {
name = "Clojure",
files = {
   "%.clojure$",
},
patterns = {
    { pattern = 'comment', type = {';;.d*'} },
    { pattern = 'string', type = {'r#"', '"#', '\\\\'} },
},
symbols = {
    ['def'] = 'keyword',
    ['defn'] = 'keyword',
    ['some'] = 'keyword',
    ['foo'] = 'keyword',
    ['bar'] = 'keyword',
    ['baz'] = 'keyword',
    ['something'] = 'keyword2',
    ['fooo'] = 'keyword2',
    ['baar'] = 'keyword2',
    ['baaz'] = 'keyword2',
    ['asdf'] = 'literal',
    ['asdffas'] = 'literal',
    ['dfasd'] = 'literal',
    ['fas'] = 'literal',
    ['df'] = 'literal',
},
}
