#!/bin/bash
src=drawio.sp
gen=sp.py
gr=sp.grammar
rw=sp.rewrite
d2j=das2json-bootstrap/mac/das2json
python3 zd.py . . ${src} main sp2py.json >${gen}
python3 mvline.py  ${gen} 60 >/tmp/${gen}
mv /tmp/${gen} ./${gen}
python3 errcheck.py ${gen}


