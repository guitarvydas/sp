def Drawio (_r):                                            #line 1
    _r.push_new_string ()
    _r.begin_breadcrumb ("Drawio")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.call (XML)
    _r.append_returned_string ()
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.eof ()                                               #line 2
                                                            #line 3
    _r.end_breadcrumb ("Drawio")
    return _r.return_string_pop ()

def XML (_r):                                               #line 4
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.need_and_append ("<")
    _r.call (Name)
    _r.append_returned_string ()
    _r.call (Attributes)
    _r.append_returned_string ()
                                                            #line 5
    if False:
        pass
    elif _r.maybe_append (">"):
        _r.call (Content)
        _r.append_returned_string ()
                                                            #line 7
        if False:
            pass
        elif _r.peek ("</mxCell>"):
            _r.call (EndMxCell)
            _r.append_returned_string ()
                                                            #line 9
            pass
        elif True:
            _r.need_and_append ("</")
            _r.call (Stuff)
            _r.append_returned_string ()
            _r.need_and_append (">")
                                                            #line 10
            pass

        pass
    elif _r.maybe_append ("/>"):

        pass
                                                            #line 14
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content (_r):                                           #line 15
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")

    while True:                                             #line 16
        _r.call (Spaces)
        _r.append_returned_string ()
                                                            #line 17
        if False:
            pass
        elif _r.peek ("</"):
            break                                           #line 19

            pass
        elif _r.peek ("<mxGeometry "):
            _r.call (mxGeometry)
            _r.append_returned_string ()
                                                            #line 20
            pass
        elif _r.peek ("<"):
            _r.call (XML)
            _r.append_returned_string ()
                                                            #line 21
            pass
        elif True:
            _r.call (Stuff)
            _r.append_returned_string ()
                                                            #line 22
            pass
                                                            #line 24
                                                            #line 25
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def mxGeometry (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("mxGeometry")
    _r.call (XML)
    _r.append_returned_string ()
                                                            #line 28
    _r.end_breadcrumb ("mxGeometry")
    return _r.return_string_pop ()

def Attributes (_r):                                        #line 30
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")

    while True:                                             #line 31

        if False:
            pass
        elif _r.peek ("style="):
            _r.call (Style)
            _r.append_returned_string ()
                                                            #line 33
            pass
        elif _r.peek (">"):
            break                                           #line 34

            pass
        elif _r.peek ("/>"):
            break                                           #line 35

            pass
        elif _r.eof ():
            break                                           #line 36

            pass
        elif True:
            _r.accept_and_append ()                         #line 37

            pass
                                                            #line 39
                                                            #line 40
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Style (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Style")
    _r.need_and_append ("style=")
    _r.call (String)
    _r.append_returned_string ()
                                                            #line 42
    _r.end_breadcrumb ("Style")
    return _r.return_string_pop ()

def Name (_r):                                              #line 44
    _r.push_new_string ()
    _r.begin_breadcrumb ("Name")

    while True:                                             #line 45

        if False:
            pass
        elif _r.peek (" "):
            break                                           #line 47

            pass
        elif _r.peek ("\t"):
            break                                           #line 48

            pass
        elif _r.peek ("\n"):
            break                                           #line 49

            pass
        elif _r.peek (">"):
            break                                           #line 50

            pass
        elif _r.peek ("<"):
            break                                           #line 51

            pass
        elif _r.peek ("/>"):
            break                                           #line 52

            pass
        elif _r.eof ():
            break                                           #line 53

            pass
        elif True:
            _r.accept_and_append ()                         #line 54

            pass
                                                            #line 56
                                                            #line 57
    _r.end_breadcrumb ("Name")
    return _r.return_string_pop ()

def Stuff (_r):                                             #line 58
    _r.push_new_string ()
    _r.begin_breadcrumb ("Stuff")

    while True:                                             #line 59

        if False:
            pass
        elif _r.peek (">"):
            break                                           #line 61

            pass
        elif _r.peek ("<"):
            break                                           #line 62

            pass
        elif _r.peek ("/>"):
            break                                           #line 63

            pass
        elif _r.eof ():
            break                                           #line 64

            pass
        elif True:
            _r.accept_and_append ()                         #line 65

            pass
                                                            #line 67
                                                            #line 68
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces (_r):                                            #line 69
    _r.push_new_string ()
    _r.begin_breadcrumb ("Spaces")

    while True:                                             #line 70

        if False:
            pass
        elif _r.peek (" "):
            _r.accept_and_append ()                         #line 72

            pass
        elif _r.peek ("\t"):
            _r.accept_and_append ()                         #line 73

            pass
        elif _r.peek ("\n"):
            _r.accept_and_append ()                         #line 74

            pass
        elif True:
            break                                           #line 75

            pass
                                                            #line 77
                                                            #line 78
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String (_r):                                            #line 79
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    _r.call (NotDquotes)
    _r.append_returned_string ()
    _r.need_and_append ("\"")
                                                            #line 80
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes (_r):                                        #line 82
    _r.push_new_string ()
    _r.begin_breadcrumb ("NotDquotes")

    while True:                                             #line 83

        if False:
            pass
        elif _r.peek ("\""):
            break                                           #line 85

            pass
        elif True:
            _r.accept_and_append ()                         #line 86

            pass
                                                            #line 88
                                                            #line 89
    _r.end_breadcrumb ("NotDquotes")
    return _r.return_string_pop ()

def EndMxCell (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("EndMxCell")
    _r.need_and_append ("</mxCell>")
    _r.call (Spaces)
    _r.append_returned_string ()
                                                            #line 90
    _r.end_breadcrumb ("EndMxCell")
    return EndMxCell__action__ (_r)

def mxGeometry__action__ (_r):                              #line 93
    _r.trace ("ignore in mxGeometry")                       #line 94

    return _r.return_ignore_pop ()                          #line 95

def EndMxCell__action__ (_r):                               #line 96
    _r.trace ("******** ignore in EndMxCell")               #line 97

    return _r.return_ignore_pop ()                          #line 98

def Style__action__ (_r):
    [rc, stdout, stderr] = shellout.shell_out ("./identity", _r.string_stack [-1])
    _r.string_stack [-1] = ""
    _r.return_stack.append (stdout)



import sys
import receptor
import shellout

# main...
_r = receptor.Receptor (sys.stdin)
Drawio (_r)
s = _r.pop_return_value ()
print (s)
