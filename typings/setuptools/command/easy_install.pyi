"""
This type stub file was generated by pyright.
"""

import sys
import os
from distutils.command.install import INSTALL_SCHEMES
from setuptools import Command, SetuptoolsDeprecationWarning
from setuptools.package_index import PackageIndex
from pkg_resources import Environment

"""
Easy Install
------------

A tool for doing automatic download/extract/build of distutils-based Python
packages.  For detailed documentation, see the accompanying EasyInstall.txt
file, or visit the `EasyInstall home page`__.

__ https://setuptools.readthedocs.io/en/latest/easy_install.html

"""

def is_64bit(): ...
def samefile(p1, p2):  # -> bool:
    """
    Determine if two paths reference the same file.

    Augments os.path.samefile to work on Windows and
    suppresses errors if the path doesn't exist.
    """
    ...

def isascii(s): ...

class easy_install(Command):
    """Manage a download/build/install process"""

    description = ...
    command_consumes_arguments = ...
    user_options = ...
    boolean_options = ...
    negative_opt = ...
    create_index = PackageIndex
    def initialize_options(self): ...
    def delete_blockers(self, blockers): ...
    def finalize_options(self): ...
    def expand_basedirs(self):  # -> None:
        """Calls `os.path.expanduser` on install_base, install_platbase and
        root."""
        ...
    def expand_dirs(self):  # -> None:
        """Calls `os.path.expanduser` on install dirs."""
        ...
    def run(self, show_deprecation=...): ...
    def pseudo_tempname(self):
        """Return a pseudo-tempname base in the install directory.
        This code is intentionally naive; if a malicious party can write to
        the target directory you're already in deep doodoo.
        """
        ...
    def warn_deprecated_options(self): ...
    def check_site_dir(self):  # -> None:
        """Verify that self.install_dir is .pth-capable dir, if needed"""
        ...
    __cant_write_msg = ...
    __not_exists_id = ...
    __access_msg = ...
    def cant_write_to_target(self): ...
    def check_pth_processing(self):  # -> bool:
        """Empirically verify whether .pth files are supported in inst. dir"""
        ...
    def install_egg_scripts(self, dist):  # -> None:
        """Write all the scripts for `dist`, unless scripts are excluded"""
        ...
    def add_output(self, path): ...
    def not_editable(self, spec): ...
    def check_editable(self, spec): ...
    def easy_install(self, spec, deps=...): ...
    def install_item(self, spec, download, tmpdir, deps, install_needed=...): ...
    def select_scheme(self, name):  # -> None:
        """Sets the install directories by applying the install schemes."""
        ...
    def process_distribution(self, requirement, dist, deps=..., *info): ...
    def should_unzip(self, dist): ...
    def maybe_move(self, spec, dist_filename, setup_base): ...
    def install_wrapper_scripts(self, dist): ...
    def install_script(self, dist, script_name, script_text, dev_path=...):  # -> None:
        """Generate a legacy script wrapper and install it"""
        ...
    def write_script(self, script_name, contents, mode=..., blockers=...):  # -> None:
        """Write an executable file to the scripts directory"""
        ...
    def install_eggs(self, spec, dist_filename, tmpdir): ...
    def egg_distribution(self, egg_path): ...
    def install_egg(self, egg_path, tmpdir): ...
    def install_exe(self, dist_filename, tmpdir): ...
    def exe_to_egg(self, dist_filename, egg_tmp):  # -> None:
        """Extract a bdist_wininst to the directories an egg would use"""
        ...
    def install_wheel(self, wheel_path, tmpdir): ...
    __mv_warning = ...
    __id_warning = ...
    def installation_report(self, req, dist, what=...):  # -> str:
        """Helpful installation message for display to package users"""
        ...
    __editable_msg = ...
    def report_editable(self, spec, setup_script): ...
    def run_setup(self, setup_script, setup_base, args): ...
    def build_and_install(self, setup_script, setup_base): ...
    def update_pth(self, dist): ...
    def unpack_progress(self, src, dst): ...
    def unpack_and_compile(self, egg_path, destination): ...
    def byte_compile(self, to_compile): ...
    __no_default_msg = ...
    def create_home_path(self):  # -> None:
        """Create directories under ~."""
        ...
    INSTALL_SCHEMES = ...
    DEFAULT_SCHEME = ...

def get_site_dirs():  # -> list[str]:
    """
    Return a list of 'site' dirs
    """
    ...

def expand_paths(inputs):  # -> Generator[tuple[str, List[str]], None, None]:
    """Yield sys.path directories that might contain "old-style" packages"""
    ...

def extract_wininst_cfg(dist_filename):  # -> RawConfigParser | None:
    """Extract configuration data from a bdist_wininst .exe

    Returns a configparser.RawConfigParser, or None
    """
    ...

def get_exe_prefixes(
    exe_filename,
):  # -> list[tuple[str, Literal['', 'EGG-INFO/scripts/']]]:
    """Get exe->egg path translations for a given .exe file"""
    ...

class PthDistributions(Environment):
    """A .pth file with Distribution paths in it"""

    dirty = ...
    def __init__(self, filename, sitedirs=...) -> None: ...
    def save(self):  # -> None:
        """Write changed .pth file back to disk"""
        ...
    def add(self, dist):  # -> None:
        """Add `dist` to the distribution map"""
        ...
    def remove(self, dist):  # -> None:
        """Remove `dist` from the distribution map"""
        ...
    def make_relative(self, path): ...

class RewritePthDistributions(PthDistributions):
    prelude = ...
    postlude = ...

if os.environ.get("SETUPTOOLS_SYS_PATH_TECHNIQUE", "raw") == "rewrite":
    PthDistributions = ...

def auto_chmod(func, arg, exc): ...
def update_dist_caches(dist_path, fix_zipimporter_caches):  # -> None:
    """
    Fix any globally cached `dist_path` related data

    `dist_path` should be a path of a newly installed egg distribution (zipped
    or unzipped).

    sys.path_importer_cache contains finder objects that have been cached when
    importing data from the original distribution. Any such finders need to be
    cleared since the replacement distribution might be packaged differently,
    e.g. a zipped egg distribution might get replaced with an unzipped egg
    folder or vice versa. Having the old finders cached may then cause Python
    to attempt loading modules from the replacement distribution using an
    incorrect loader.

    zipimport.zipimporter objects are Python loaders charged with importing
    data packaged inside zip archives. If stale loaders referencing the
    original distribution, are left behind, they can fail to load modules from
    the replacement distribution. E.g. if an old zipimport.zipimporter instance
    is used to load data from a new zipped egg archive, it may cause the
    operation to attempt to locate the requested data in the wrong location -
    one indicated by the original distribution's zip archive directory
    information. Such an operation may then fail outright, e.g. report having
    read a 'bad local file header', or even worse, it may fail silently &
    return invalid data.

    zipimport._zip_directory_cache contains cached zip archive directory
    information for all existing zipimport.zipimporter instances and all such
    instances connected to the same archive share the same cached directory
    information.

    If asked, and the underlying Python implementation allows it, we can fix
    all existing zipimport.zipimporter instances instead of having to track
    them down and remove them one by one, by updating their shared cached zip
    archive directory information. This, of course, assumes that the
    replacement distribution is packaged as a zipped egg.

    If not asked to fix existing zipimport.zipimporter instances, we still do
    our best to clear any remaining zipimport.zipimporter related cached data
    that might somehow later get used when attempting to load data from the new
    distribution and thus cause such load operations to fail. Note that when
    tracking down such remaining stale data, we can not catch every conceivable
    usage from here, and we clear only those that we know of and have found to
    cause problems if left alive. Any remaining caches should be updated by
    whomever is in charge of maintaining them, i.e. they should be ready to
    handle us replacing their zip archives with new distributions at runtime.

    """
    ...

if "__pypy__" in sys.builtin_module_names:
    _replace_zip_directory_cache_data = ...
else: ...

def is_python(text, filename=...):  # -> bool:
    "Is this string a valid Python script?"
    ...

def is_sh(executable):  # -> bool:
    """Determine if the specified executable is a .sh (contains a #! line)"""
    ...

def nt_quote_arg(arg):  # -> str:
    """Quote a command line argument according to Windows parsing rules"""
    ...

def is_python_script(script_text, filename):  # -> bool:
    """Is this text, as a whole, a Python script? (as opposed to shell/bat/etc."""
    ...

def chmod(path, mode): ...

class CommandSpec(list):
    """
    A command spec for a #! header, specified as a list of arguments akin to
    those passed to Popen.
    """

    options = ...
    split_args = ...
    @classmethod
    def best(cls):  # -> Type[CommandSpec]:
        """
        Choose the best CommandSpec class based on environmental conditions.
        """
        ...
    @classmethod
    def from_param(cls, param):  # -> CommandSpec:
        """
        Construct a CommandSpec from a parameter to build_scripts, which may
        be None.
        """
        ...
    @classmethod
    def from_environment(cls): ...
    @classmethod
    def from_string(cls, string):  # -> CommandSpec:
        """
        Construct a command spec from a simple string representing a command
        line parseable by shlex.split.
        """
        ...
    def install_options(self, script_text): ...
    def as_header(self): ...

sys_executable = ...

class WindowsCommandSpec(CommandSpec):
    split_args = ...

class ScriptWriter:
    """
    Encapsulates behavior around writing entry point scripts for console and
    gui apps.
    """

    template = ...
    command_spec_class = CommandSpec
    @classmethod
    def get_script_args(cls, dist, executable=..., wininst=...): ...
    @classmethod
    def get_script_header(cls, script_text, executable=..., wininst=...): ...
    @classmethod
    def get_args(
        cls, dist, header=...
    ):  # -> Generator[tuple[Unknown, str | Unknown], None, None]:
        """
        Yield write_script() argument tuples for a distribution's
        console_scripts and gui_scripts entry points.
        """
        ...
    @classmethod
    def get_writer(cls, force_windows): ...
    @classmethod
    def best(cls):  # -> Type[ScriptWriter]:
        """
        Select the best ScriptWriter for this environment.
        """
        ...
    @classmethod
    def get_header(cls, script_text=..., executable=...):  # -> str:
        """Create a #! line, getting options (if any) from script_text"""
        ...

class WindowsScriptWriter(ScriptWriter):
    command_spec_class = WindowsCommandSpec
    @classmethod
    def get_writer(cls): ...
    @classmethod
    def best(cls):
        """
        Select the best ScriptWriter suitable for Windows
        """
        ...

class WindowsExecutableLauncherWriter(WindowsScriptWriter): ...

get_script_args = ...
get_script_header = ...

def get_win_launcher(type):  # -> bytes:
    """
    Load the Windows launcher (executable) suitable for launching a script.

    `type` should be either 'cli' or 'gui'

    Returns the executable as a byte string.
    """
    ...

def load_launcher_manifest(name): ...
def rmtree(path, ignore_errors=..., onerror=...): ...
def current_umask(): ...

class EasyInstallDeprecationWarning(SetuptoolsDeprecationWarning):
    """
    Warning for EasyInstall deprecations, bypassing suppression.
    """

    ...
