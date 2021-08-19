"""
This type stub file was generated by pyright.
"""

import attr

"""Dataset paths, identifiers, and filenames"""
SCHEMES = ...
CURLSCHEMES = ...
REMOTESCHEMES = ...
class Path:
    """Base class for dataset paths"""
    ...


@attr.s(slots=True)
class ParsedPath(Path):
    """Result of parsing a dataset URI/Path

    Attributes
    ----------
    path : str
        Parsed path. Includes the hostname and query string in the case
        of a URI.
    archive : str
        Parsed archive path.
    scheme : str
        URI scheme such as "https" or "zip+s3".
    """
    path = ...
    archive = ...
    scheme = ...
    @classmethod
    def from_uri(cls, uri): # -> ParsedPath:
        ...
    
    @property
    def name(self): # -> Any | str:
        """The parsed path's original URI"""
        ...
    
    @property
    def is_remote(self): # -> Any | bool:
        """Test if the path is a remote, network URI"""
        ...
    
    @property
    def is_local(self): # -> Any | bool:
        """Test if the path is a local URI"""
        ...
    


@attr.s(slots=True)
class UnparsedPath(Path):
    """Encapsulates legacy GDAL filenames

    Attributes
    ----------
    path : str
        The legacy GDAL filename.
    """
    path = ...
    @property
    def name(self): # -> Any:
        """The unparsed path's original path"""
        ...
    


def parse_path(path): # -> Path | UnparsedPath | ParsedPath:
    """Parse a dataset's identifier or path into its parts

    Parameters
    ----------
    path : str or path-like object
        The path to be parsed.

    Returns
    -------
    ParsedPath or UnparsedPath

    Notes
    -----
    When legacy GDAL filenames are encountered, they will be returned
    in a UnparsedPath.
    """
    ...

def vsi_path(path): # -> Any | str:
    """Convert a parsed path to a GDAL VSI path

    Parameters
    ----------
    path : Path
        A ParsedPath or UnparsedPath object.

    Returns
    -------
    str
    """
    ...
