def Hello (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Hello")
    _r.need_and_append ("Hello")
                                                            #line 1
    _r.end_breadcrumb ("Hello")
    return _r.return_string_pop ()

def Style__action__ (_r):                                   #line 2
    [rc, stdout, stderr] = shellout.shell_out ("./ndsltemp2 styleexpand.grammar styleexpand.rewrite support.js", _r.string_stack [-1])
    _r.string_stack [-1] = stdout

    _r.trace ("Style identity")                             #line 4

    [rc, stdout, stderr] = shellout.shell_out ("./identity", _r.string_stack [-1])
    _r.string_stack [-1] = stdout

    _r.return_string_pop ()


import sys
import receptor
import shellout

# main...
_r = receptor.Receptor (sys.stdin)
Hello (_r)
s = _r.pop_return_value ()
print (s)
