from functools import singledispatch
from numbers import Integral
from collections.abc import Sequence
from decimal import Decimal
from html import escape

def html_escape(arg):
    return escape(str(arg))
                      
def html_int(a):
    return '{0}(<i>{1}</i)'.format(a, str(hex(a)))

def html_real(a):
    return '{0:.2f}'.format(round(a, 2))
                                  
def html_str(s):
    return html_escape(s).replace('\n', '<br/>\n')
                                  
def html_list(l):
    items = ['<li>{0}</li>'.format(htmlize(item)) for item in l]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'
                                  
def html_dict(d):
    items = ['<li>{0}={1}</li>'.format(html_escape(k), htmlize(v)) for k, v in d.items()]
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

# We will use singledespatch from functools instead
#def singledispatch(fn):
#    registry = dict()
#    
#    registry[object] = fn
#    
#    def register(type_):
#        def inner(fn):
#            registry[type_] = fn
#            return fn  # we do this so we can stack register decorators!
#        return inner
#   
#    def decorator(arg):
#        fn = registry.get(type(arg), registry[object])
#        return fn(arg)
#    
#    def dispatch(type_):
#        return registry.get(type_, registry[object])
#
#    decorator.register = register
#    decorator.registry = registry.keys()
#    decorator.dispatch = dispatch
#    return decorator

@singledispatch
def htmlize(arg):
    if isinstance(arg, int):
        return html_int(arg)
    elif isinstance(arg, float) or isinstance(arg, Decimal):
        return html_real(arg)
    elif isinstance(arg, str):
        return html_str(arg)
    elif isinstance(arg, list) or isinstance(arg, tuple) or isinstance(arg, set):
        return html_list(arg)
    elif isinstance(arg, dict):
        return html_dict(arg)
    else:
        # default behavior - just html escape string representation
        return html_escape(str(arg))

htmlize.dispatch(int)
htmlize.dispatch(bool)

print(htmlize("""this
is a multi line string with
a < 10"""))
