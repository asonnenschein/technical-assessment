"""
This type stub file was generated by pyright.
"""

"""Abstraction for sessions in various clouds."""
class Session:
    """Base for classes that configure access to secured resources.

    Attributes
    ----------
    credentials : dict
        Keys and values for session credentials.

    Notes
    -----
    This class is not intended to be instantiated.

    """
    def get_credential_options(self): # -> Type[NotImplementedError]:
        """Get credentials as GDAL configuration options

        Returns
        -------
        dict

        """
        ...
    
    @staticmethod
    def from_foreign_session(session, cls=...): # -> DummySession:
        """Create a session object matching the foreign `session`.

        Parameters
        ----------
        session : obj
            A foreign session object.
        cls : Session class, optional
            The class to return.

        Returns
        -------
        Session

        """
        ...
    
    @staticmethod
    def from_path(path, *args, **kwargs): # -> DummySession | AWSSession:
        """Create a session object suited to the data at `path`.

        Parameters
        ----------
        path : str
            A dataset path or identifier.
        args : sequence
            Positional arguments for the foreign session constructor.
        kwargs : dict
            Keyword arguments for the foreign session constructor.

        Returns
        -------
        Session

        """
        ...
    


class DummySession(Session):
    """A dummy session.

    Attributes
    ----------
    credentials : dict
        The session credentials.

    """
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def get_credential_options(self): # -> dict[Unknown, Unknown]:
        """Get credentials as GDAL configuration options

        Returns
        -------
        dict

        """
        ...
    


class AWSSession(Session):
    """Configures access to secured resources stored in AWS S3.
    """
    def __init__(self, session=..., aws_unsigned=..., aws_access_key_id=..., aws_secret_access_key=..., aws_session_token=..., region_name=..., profile_name=..., requester_pays=...) -> None:
        """Create a new boto3 session

        Parameters
        ----------
        session : optional
            A boto3 session object.
        aws_unsigned : bool, optional (default: False)
            If True, requests will be unsigned.
        aws_access_key_id : str, optional
            An access key id, as per boto3.
        aws_secret_access_key : str, optional
            A secret access key, as per boto3.
        aws_session_token : str, optional
            A session token, as per boto3.
        region_name : str, optional
            A region name, as per boto3.
        profile_name : str, optional
            A shared credentials profile name, as per boto3.
        requester_pays : bool, optional
            True if the requester agrees to pay transfer costs (default:
            False)
        """
        ...
    
    @property
    def credentials(self): # -> dict[Unknown, Unknown]:
        """The session credentials as a dict"""
        ...
    
    def get_credential_options(self): # -> dict[str, str] | dict[Unknown, Unknown]:
        """Get credentials as GDAL configuration options

        Returns
        -------
        dict

        """
        ...
    


class GSSession(Session):
    """Configures access to secured resources stored in Google Cloud Storage
    """
    def __init__(self, google_application_credentials=...) -> None:
        """Create new Google Cloude Storage session

        Parameters
        ----------
        google_application_credentials: string
            Path to the google application credentials JSON file.
        """
        ...
    
    @classmethod
    def hascreds(cls, config): # -> bool:
        """Determine if the given configuration has proper credentials

        Parameters
        ----------
        cls : class
            A Session class.
        config : dict
            GDAL configuration as a dict.

        Returns
        -------
        bool

        """
        ...
    
    @property
    def credentials(self): # -> dict[Unknown, Unknown]:
        """The session credentials as a dict"""
        ...
    
    def get_credential_options(self): # -> dict[Unknown, Unknown]:
        """Get credentials as GDAL configuration options

        Returns
        -------
        dict

        """
        ...
    

