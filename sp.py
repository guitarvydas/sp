def Drawio (_r):                                            #line 1
    _r.push_new_string ()
    _r.begin_breadcrumb ("Drawio")

    _r.trace_accept ()                                      #line 2
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.call (XML)
    _r.append_returned_string ()
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.eof ()                                               #line 3
                                                            #line 4
    _r.end_breadcrumb ("Drawio")
    return _r.return_string_pop ()

def XML (_r):                                               #line 5
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.need_and_append ("<")
    _r.call (Name)
    _r.append_returned_string ()
    _r.call (Attributes)
    _r.append_returned_string ()
                                                            #line 6
    if False:
        pass
    elif _r.maybe_append (">"):
        _r.call (Content)
        _r.append_returned_string ()
                                                            #line 8
        if False:
            pass
        elif _r.peek ("</mxCell>"):
            _r.call (EndMxCell)
            _r.append_returned_string ()
                                                            #line 10
            pass
        elif True:
            _r.need_and_append ("</")
            _r.call (Stuff)
            _r.append_returned_string ()
            _r.need_and_append (">")
                                                            #line 11
            pass

        pass
    elif _r.maybe_append ("/>"):

        pass
                                                            #line 15
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content (_r):                                           #line 16
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")

    while True:                                             #line 17
        _r.call (Spaces)
        _r.append_returned_string ()
                                                            #line 18
        if False:
            pass
        elif _r.peek ("</"):
            break                                           #line 20

            pass
        elif _r.peek ("<mxGeometry "):
            _r.call (mxGeometry)
            _r.append_returned_string ()
                                                            #line 21
            pass
        elif _r.peek ("<"):
            _r.call (XML)
            _r.append_returned_string ()
                                                            #line 22
            pass
        elif True:
            _r.call (Stuff)
            _r.append_returned_string ()
                                                            #line 23
            pass
                                                            #line 25
                                                            #line 26
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def mxGeometry (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("mxGeometry")
    _r.call (XML)
    _r.append_returned_string ()
                                                            #line 29
    _r.end_breadcrumb ("mxGeometry")
    return _r.return_string_pop ()

def Attributes (_r):                                        #line 31
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")

    while True:                                             #line 32

        if False:
            pass
        elif _r.peek ("style="):
            _r.call (Style)
            _r.append_returned_string ()
                                                            #line 34
            pass
        elif _r.peek (">"):
            break                                           #line 35

            pass
        elif _r.peek ("/>"):
            break                                           #line 36

            pass
        elif _r.eof ():
            break                                           #line 37

            pass
        elif True:
            _r.accept_and_append ()                         #line 38

            pass
                                                            #line 40
                                                            #line 41
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Style (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Style")
    _r.need_and_append ("style=")
    _r.call (String)
    _r.append_returned_string ()
                                                            #line 43
    _r.end_breadcrumb ("Style")
    return _r.return_string_pop ()

def Name (_r):                                              #line 45
    _r.push_new_string ()
    _r.begin_breadcrumb ("Name")

    while True:                                             #line 46

        if False:
            pass
        elif _r.peek (" "):
            break                                           #line 48

            pass
        elif _r.peek ("\t"):
            break                                           #line 49

            pass
        elif _r.peek ("\n"):
            break                                           #line 50

            pass
        elif _r.peek (">"):
            break                                           #line 51

            pass
        elif _r.peek ("<"):
            break                                           #line 52

            pass
        elif _r.peek ("/>"):
            break                                           #line 53

            pass
        elif _r.eof ():
            break                                           #line 54

            pass
        elif True:
            _r.accept_and_append ()                         #line 55

            pass
                                                            #line 57
                                                            #line 58
    _r.end_breadcrumb ("Name")
    return _r.return_string_pop ()

def Stuff (_r):                                             #line 59
    _r.push_new_string ()
    _r.begin_breadcrumb ("Stuff")

    while True:                                             #line 60

        if False:
            pass
        elif _r.peek (">"):
            break                                           #line 62

            pass
        elif _r.peek ("<"):
            break                                           #line 63

            pass
        elif _r.peek ("/>"):
            break                                           #line 64

            pass
        elif _r.eof ():
            break                                           #line 65

            pass
        elif True:
            _r.accept_and_append ()                         #line 66

            pass
                                                            #line 68
                                                            #line 69
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces (_r):                                            #line 70
    _r.push_new_string ()
    _r.begin_breadcrumb ("Spaces")

    while True:                                             #line 71

        if False:
            pass
        elif _r.peek (" "):
            _r.accept_and_append ()                         #line 73

            pass
        elif _r.peek ("\t"):
            _r.accept_and_append ()                         #line 74

            pass
        elif _r.peek ("\n"):
            _r.accept_and_append ()                         #line 75

            pass
        elif True:
            break                                           #line 76

            pass
                                                            #line 78
                                                            #line 79
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String (_r):                                            #line 80
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    _r.call (NotDquotes)
    _r.append_returned_string ()
    _r.need_and_append ("\"")
                                                            #line 81
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes (_r):                                        #line 83
    _r.push_new_string ()
    _r.begin_breadcrumb ("NotDquotes")

    while True:                                             #line 84

        if False:
            pass
        elif _r.peek ("\""):
            break                                           #line 86

            pass
        elif True:
            _r.accept_and_append ()                         #line 87

            pass
                                                            #line 89
                                                            #line 90
    _r.end_breadcrumb ("NotDquotes")
    return _r.return_string_pop ()

def EndMxCell (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("EndMxCell")
    _r.need_and_append ("</mxCell>")
    _r.call (Spaces)
    _r.append_returned_string ()
                                                            #line 91
    _r.end_breadcrumb ("EndMxCell")
    return EndMxCell__action__ (_r)

def mxGeometry__action__ (_r):                              #line 94
    _r.trace ("ignore in mxGeometry")                       #line 95

    return _r.return_ignore_pop ()                          #line 96

def EndMxCell__action__ (_r):                               #line 97
    _r.trace ("******** ignore in EndMxCell")               #line 98

    return _r.return_ignore_pop ()                          #line 99

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
