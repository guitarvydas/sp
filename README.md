# Stream Parser
This project generates a stream parser using a nano-DSL.

The nano-DSL is converted to executable Python code.

The point of this project is to map the nano-DSL `.sp` code to Python `.py` code.

To actually use the stream parser, you need to run the generated python code as described below.

A bunch of extra helper code is injected into the generated parser. This helper code is intended to help with debugging the parser during development. This shows the value of owning the nano-DSL - you can stick extra code into the generated code. Such extra code detracts from the human-readability of the generated code and would complicate issues if you tried to write all of this by hand. The Python compiler doesn't care about human-readability and is happy to deal with all of the extra debug code.

This underlines the utility of inventing notations - SCNS (Solution Centric Notations). You can think about and write code at a higher "abstract" level without worrying about scads of lower level details. You can put the lower-level stuff into the code generator and the code generator will religiously stick all that stuff into the generated code without your needing to worry about niggly, repetitive  details.

The usage of the nano-DSL is documented in `doc/sp.pdf`.

# What is a Stream Parser?

A stream parser is just a parser, like any parser, except that it does _not_ build an AST in-memory. This saves memory and lets you parse really big files as they go through the parser like a conveyor belt.

Because there's no in-memory AST, the parser has to make decisions to execute actions as the parse ensues. AST-based parsers wait until the end of the parse, then trigger actions based on the AST (actually, the AST is culled to produce a CST - concrete sytax tree - by that point, but, I quibble). This detail means that you can't write code that walks up and down the AST after-the-fact (say, by doing a recursive tree-walk). It turns out that this is not a severe restriction. You can still write very complicated parsers this way.

## Why Use a Stream Parser Instead of Regular Parsers?

The ability to use a stream parser mostly causes a change in mind-set. 

With a stream parser, you don't need to inhale a whole program at once before doing something with it.

You can pattern match incoming text and take actions based on what patterns are matched. A pattern matcher is just a parser, when the input is text. You can write a nano-DSL - an "SCN" - in a BNF-like form, then hang actions off of the BNF. This means that you can write pipelines - aka extreme divide and conquer - where each stage in the pipeline has its own custom nano-DSL. This approach is viable when making nano-DSLs takes on the order of 10 minutes each, instead of 10 weeks each (YMMV, but, the goal is to make creating nano-DSLs so quick and inexpensive that it becomes as easy-to-use as using REGEXs in modern programming languages).

For building compilers, you can simply use a technique called `syntax directed translation`, which lets you apply extreme divide-and-conquer to a problem. You can write a new compiler in little pieces, as a pipeline. Each piece can use a custom nano-DSL as its input, as long as the piece before it adheres to the rules of the custom nano-DSL.

If you have infinite memory - e.g. virtual memory - then you can use an AST-based technique.

If you have limited memory, then stream parsing is useful. Taken to the limits, this technique allows you to build complicated pieces of software on simple CPUs that don't need to waste chip space for MMUs and TLBs, and, don't need to waste operating system space for handling cache misses, etc. All that VM stuff costs extra and is fundamentally inefficient. One can write code that doesn't need all of that, hence, one can cost-optimize the result better.

FBP - Flow-Based Programming - works with streams. Mevent-driven techniques, like 0D, work with messages that work like streams with big spaces between messages. In either case, it might be possible to use less memory and to cost-reduce related hardware and software.

### Example - Compiler Pipeline
For example, let's say that you want to write a compiler. 
1. You can write the scanner as a piece at the front of the pipeline. The scanner tokenizes the input file and passes it into the pipeline.
2. The next stage is the parser. It accepts input that no longer looks like the original source file. The input is a stream of `tokens`. The parser checks that the tokens are sequenced in the correct manner, then deletes al syntactic sugar. Humans like syntactic sugar, but machines (compilers) don't care. It is easier to write downstream passes in the compiler, if the the input to those passes does not contain any fluff.
3. The next stage is the semantic gatherer. The input to this stage is a custom nano-DSL. It consists of a machine-readable language that contains only tokens, but no syntactic sugar tokens. It is guaranteed that the tokens parse OK. So, this pass doesn't need to worry about error-checking the input stream. It just does the work it needs to do - one task and one task only. The point of this pass is to look at all incoming declarations and to make some sort of table, or, to insert annotations into the code that give the next pass(es) enough information to do their work. This stage skips over all of the incoming stuff that doesn't relate to declarations. The declaration details are stipped out of the stream, since it is no longer needed.
4. The next stage is the semantic checker. The input to this stage is yet another custom nano-DSL, and, maybe a symbol table. The in At this point, we know that the incoming code consists of tokens, has no syntactic noise, has no parse errors in it, and, has no declarations in it. The incoming code (or associated symbol table) contains enough information to help check the code for correct usage. This stage looks at every use of every variable / function / whatever and checks that the specified operations are semantically legal. If no errors are found, it passes the (modified?) stream on to the next pass. If errors are found, it produces errors messages and kills the pipeline.
5. The next stage converts the incoming stream into code - assembly code or code for some existing language. The input is yet another nano-DSL. At this point, we know that the input contains no fluff, is completely error-free and contains only information needed to convert the code. The only thing that this stage needs to do is to transpile the input to the chosen form of target output. It doesn't need to re-do error checks that were already done in previous stages. The programmer is allowed to think only about this single problem - how to do one task and do it well - how to convert the incoming code to target code. The programmer is given the freedom to do a good job of this task, while not having to worry about niggly details like error checking and edge-cases caused by skipping over unnecessary tokens.

[Depending on how much optimization is required, stage 5 might be split into several sub-stages, some of which might be positioned in the pipeline at various, more convenient places. I want to keep this discussion KISS, so I skipped those kinds of details].

An example of the early use of this technique is the [PT Pascal compiler](https://research.cs.queensu.ca/home/cordy/pub/downloads/ssl/). It was an early attempt at using divide-and-conquer for compiler building and does not have exactly the same pipeline stages as described above.

# usage

To generate the stream parser
1. write a stream parse specification as a `.sp` file
2. `make` - at this time, the input spec is hard-coded to be `drawio.sp` and the output is hard-coded as `sp.py`
   - this, also, runs the resulting parser `sp.py` against the hard-coded test file `sp2py.drawio`

To copy the parser to another project, copy 2 files `sp.py` and `receptor.py`.

# Documentation
See `./doc/sp.md`.

# helper 

As the parser runs, it makes the current rule name accessible, so you can track what's being parsed by whatever rule as you debug. The names of rules are pushed onto the variable `self.breadcrumb_stack`. The topmost name is the currently-running rule.
