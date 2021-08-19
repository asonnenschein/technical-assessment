"""
This type stub file was generated by pyright.
"""

"""
Monkey patching of distutils.
"""

def get_unpatched(item): ...
def get_unpatched_class(cls):  # -> type:
    """Protect against re-patching the distutils if reloaded

    Also ensures that no other distutils extension monkeypatched the distutils
    first.
    """
    ...

def patch_all(): ...
def patch_func(replacement, target_mod, func_name):  # -> None:
    """
    Patch func_name in target_mod with replacement

    Important - original must be resolved by name to avoid
    patching an already patched function.
    """
    ...

def get_unpatched_function(candidate): ...
def patch_for_msvc_specialized_compiler():  # -> None:
    """
    Patch functions in distutils to use standalone Microsoft Visual C++
    compilers.
    """
    ...
