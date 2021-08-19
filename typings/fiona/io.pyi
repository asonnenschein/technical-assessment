"""
This type stub file was generated by pyright.
"""

"""Classes capable of reading and writing collections
"""
log = ...
class MemoryFile(MemoryFileBase):
    """A BytesIO-like object, backed by an in-memory file.

    This allows formatted files to be read and written without I/O.

    A MemoryFile created with initial bytes becomes immutable. A
    MemoryFile created without initial bytes may be written to using
    either file-like or dataset interfaces.

    Examples
    --------

    """
    def __init__(self, file_or_bytes=..., filename=..., ext=...) -> None:
        ...
    
    def open(self, driver=..., schema=..., crs=..., encoding=..., layer=..., vfs=..., enabled_drivers=..., crs_wkt=..., **kwargs): # -> Collection | None:
        """Open the file and return a Fiona collection object.

        If data has already been written, the file is opened in 'r'
        mode. Otherwise, the file is opened in 'w' mode.

        Parameters
        ----------
        Note well that there is no `path` parameter: a `MemoryFile`
        contains a single dataset and there is no need to specify a
        path.

        Other parameters are optional and have the same semantics as the
        parameters of `fiona.open()`.
        """
        ...
    
    def __enter__(self): # -> MemoryFile:
        ...
    
    def __exit__(self, *args, **kwargs): # -> None:
        ...
    


class ZipMemoryFile(MemoryFile):
    """A read-only BytesIO-like object backed by an in-memory zip file.

    This allows a zip file containing formatted files to be read
    without I/O.
    """
    def __init__(self, file_or_bytes=...) -> None:
        ...
    
    def open(self, path=..., driver=..., encoding=..., layer=..., enabled_drivers=..., **kwargs): # -> Collection:
        """Open a dataset within the zipped stream.

        Parameters
        ----------
        path : str
            Path to a dataset in the zip file, relative to the root of the
            archive.

        Returns
        -------
        A Fiona collection object

        """
        ...
    

