"""
This type stub file was generated by pyright.
"""

from ctypes import c_char_p

'''Prototyping of the GEOS C API

See header file: geos-x.y.z/capi/geos_c.h
'''
EXCEPTION_HANDLER_FUNCTYPE = ...
c_size_t_p = ...
class allocated_c_char_p(c_char_p):
    '''char pointer return type'''
    ...


def prototype(lgeos, geos_version): # -> None:
    """Protype functions in geos_c.h for different version of GEOS

    Use the GEOS version, not the C API version.
    """
    ...

