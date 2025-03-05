#!/bin/bash
# usage: ./build.bash _spec_.sp _outfile_.py
src=$1
gen=$2
gr=sp.grammar
rw=sp.rewrite
# run the code generator - it uses the 0d kernel (call zd.py) and wiring specified by sp2py.json
# sp2py.json is generated elsewhere. [The drawing sp2py.drawio specifies a set of little networks that connect
# software components together to form the code generator. A program `das2json` is used to compile the diagram down to
# the sp2py.json file that is used here]. The code generator writes the generated code tothe file specified as the
# 2nd command-line argument for this shell script (internally named ${gen})
python3 zd.py . . ${src} main sp2py.json >${gen}
python3 mvline.py  ${gen} 60 >/tmp/${gen}
mv /tmp/${gen} ./${gen}
python3 errcheck.py ${gen}


