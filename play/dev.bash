#!/bin/bash
# usage: ./run.bash 'grammar' 'rewrite' 'support' 'src'
# (supply a library directory, a grammar file, a rewrite file, and a support (JS) file, inhale a source file (written in new nDSL syntax), exhale output of running the nanoDSL code
set -e
LIB=../t2t/lib
GRAMMAR=$1
REWRITE=$2
SUPPORT=$3
SRC=$4
node ${LIB}/t2t.mjs ${REWRITE} >temp.rewrite.mjs
cat ${LIB}/front.part.js ${GRAMMAR} ${LIB}/middle.part.js ${LIB}/args.part.js ${SUPPORT} temp.rewrite.mjs ${LIB}/tail.part.js >temp.nanodsl.mjs
node temp.nanodsl.mjs ${SRC}
