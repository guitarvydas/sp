#!/bin/bash
# usage: ./build.bash _spec_.sp _outfile_.py
src=$1
gen=$2
gr=sp.grammar
rw=sp.rewrite
d2j=das2json-bootstrap/mac/das2json
python3 zd.py . . ${src} main sp2py.json >${gen}
python3 mvline.py  ${gen} 60 >/tmp/${gen}
mv /tmp/${gen} ./${gen}
python3 errcheck.py ${gen}


