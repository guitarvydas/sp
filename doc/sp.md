This is a nano-DSL - an "SCN" - for creating stream parsing receptors as Python code.

The syntax for this SCN deals only with defining rules that pattern-match incoming text and fire actions when certain patterns are detected. The details of reading strings of characters from stdin are elided and abstracted away, making it possible to think _only_ about the job of pattern matching. The code generator generates Python code that fills in all of the other details that to run the parser.

The `.sp` specification consists of a set of rules. Rules can call other rules. Most rules just parse incoming text and return a the collected, single string. The other kind of rules parse incoming text, but perform an action on the collected string before returning it.

This tool is a parser generator, rather than a formal language specification.

Two kinds of rules can be defined using the following syntax:
```
^ name = ...
# name = ...
```

The first form `^ ... = ...` defines a parsing rule which simply collects up what it finds, then returns the collected as a string to whatever rule called it.

The second form `# ... = ...` defines a parsing rule which calls an action just before returning the collected string.

Actions are defined at the end of the file using the syntax:
```
#: name = _ignore_value
```

The built-in operator `_ignore_value` clears the return string. This is the only action defined at this time. It seems likely that another action will be added, that calls an "external" function with the collected string as a parameter, then returns whatever string is returned by the "external" function. As bizarre as it may sound, only 2 actions are required for culling .drawio diagrams:
1. keeping the parsed text
2. discarding the parsed text.
Note that these 2 actions are performed on a per-rule basis. This gives enough fine-grained control to parse and throw away bits of the incoming stream.

[Note to self, re. future action: call out to OhmJS to parse the collected string and transpile it to some other string. Should we simply shell-out to Javascript, or rewrite this stream parser in Javascript? OhmJS is implemented in JS and requires that its semantic actions be written in JS. I use the `.rewrite` nano-DSL to specify rewrites and to generate the required semantic JS code.]

[Note to self. To use OhmJS on the complete input, only 1 `.sp` rule needs to be written - a top-level `@=` that collects all incoming characters then calls OhmJS to parse the collection.]

# Operations
Every call to a rule instantiates a new, empty, collector. A stack of collectors is maintained. All work done by a rule affect the topmost collector. A collector is just a string of characters. At the end of a rule, the collector contents are returned, as a single string, to the caller, or, the edge-case of returning from the top-most rule, the collector is printed on `stdout`. When a rule returns, the top-most collector is popped from the collector stack.

Potential matches are kept `on deck`.

There are 8 basic operations in sp:

- `.` accept whatever is on-deck - the on-deck string is appended to the end of the current collector string
- `"..."` match and accept a string of characters, with backtracking - the matcher matches characters from left to right, if it gets to the end, the characters are appended to the collector, if the match fails at any point before the end of the string, all characters matched up to that point are put back at the front of the stream. If the match fails in a non-lookahead context, an syntax error is declared and parsing quits.
- `<<<...>>>` - cycle (loop) the operations within the bracketed section are repeated until `_break` is encountered. This is typically used to parse a pattern repeatedly and usually incorporate a `choice` which determines when to exit the cycle. 
- `_break` - exits the containing cycle
- `[ | "...": ... ]` accepting choice - if the `"..."` string is matched, it is accepted and the operations following the `:` are executed, else the next choice is tried. Note that control flows in an ordered, top to bottom manner. The first choice that matches is accepted and no other choices are tried. A default branch can be specified as `| *: ...`. The default branch always matches.
- lookahead choice `[* | "...": ... ]` same as an `accepting choice` except that the `"..."` string is not accepted if it is matched (the match can be immediately accepted, though, by specifying a `.` operation immediately to the right of the `:`)
- `name` call rule - control transfers to the named rule, which immediately causes a fresh collector to be pushed onto the collector stack. Rules have no explicit parameters - rules only implicitly match against the input stream
- `ignore_value` - clears the topmost collector, the topmost collector string is replaced by an empty string

## Example Cycle
For example, imagine parsing the body of a curly-braced block of statements. The match might be written as:
```
CompoundBody ^=
  "{"
	<<<
	  Statement
	  [*
		| "if":
		| "while":
		| *: _break
	  ]
	>>>
  "}"
```

N.B. this example is incomplete, since it shows only a few possible statement types. I intend to allow for choice-calling, hence, expect to rewrite this example in a more concise manner. Probably something like:
```
CompoundBody ^=
  "{"
	<<<
	  [ Statement
		| _ok:
		| *: _break
	  ]
	>>>
  "}"
```

- _end
- languages @t2t, @swipl
  #: RuleName @ swipl
...
- include, copy/paste 
  #: Rulename < "filename.sp" ???
