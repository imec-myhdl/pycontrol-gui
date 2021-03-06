# block definition
# name = 'Compare' 
# libname = 'math'

from libraries.library_math.Bitwise import *
from libraries.library_math.Bitwise import getSymbol as _getSymbol

tooltip = '''Compare function with optional delay
     e.g. a_0 > a_1
the output can be inverted by putting Z parameter to '-' 
(uses Bitwise block as primitive)'''

parameters = {'Z':'+'} # pcell if not empty
properties = {'delay':0.0, 'op':['==', '== != < >'.split()]} # netlist properties

def getSymbol(param, properties,parent=None,scene=None):
    pp = dict(_name=name, _libname=libname)
    pp.update(properties)
    return _getSymbol(param, pp,parent,scene)
