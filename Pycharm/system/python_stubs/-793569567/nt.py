# encoding: utf-8
# module nt
# from (built-in)
# by generator 1.136
"""
This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.
"""

# imports
from exceptions import error


# Variables with simple values

F_OK = 0

O_APPEND = 8
O_BINARY = 32768
O_CREAT = 256
O_EXCL = 1024
O_NOINHERIT = 128
O_RANDOM = 16
O_RDONLY = 0
O_RDWR = 2
O_SEQUENTIAL = 32

O_SHORT_LIVED = 4096

O_TEMPORARY = 64
O_TEXT = 16384
O_TRUNC = 512
O_WRONLY = 1

P_DETACH = 4
P_NOWAIT = 1
P_NOWAITO = 3
P_OVERLAY = 2
P_WAIT = 0

R_OK = 4

TMP_MAX = 32767

W_OK = 2

X_OK = 1

# functions

def abort(): # real signature unknown; restored from __doc__
    """
    abort() -> does not return!
    
    Abort the interpreter immediately.  This 'dumps core' or otherwise fails
    in the hardest way possible on the hosting operating system.
    """
    pass

def access(path, mode): # real signature unknown; restored from __doc__
    """
    access(path, mode) -> True if granted, False otherwise
    
    Use the real uid/gid to test for access to a path.  Note that most
    operations will use the effective uid/gid, therefore this routine can
    be used in a suid/sgid environment to test if the invoking user has the
    specified access to the path.  The mode argument can be F_OK to test
    existence, or the inclusive-OR of R_OK, W_OK, and X_OK.
    """
    return False

def chdir(path): # real signature unknown; restored from __doc__
    """
    chdir(path)
    
    Change the current working directory to the specified path.
    """
    pass

def chmod(path, mode): # real signature unknown; restored from __doc__
    """
    chmod(path, mode)
    
    Change the access permissions of a file.
    """
    pass

def close(fd): # real signature unknown; restored from __doc__
    """
    close(fd)
    
    Close a file descriptor (for low level IO).
    """
    pass

def closerange(fd_low, fd_high): # real signature unknown; restored from __doc__
    """
    closerange(fd_low, fd_high)
    
    Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    """
    pass

def dup(fd): # real signature unknown; restored from __doc__
    """
    dup(fd) -> fd2
    
    Return a duplicate of a file descriptor.
    """
    pass

def dup2(old_fd, new_fd): # real signature unknown; restored from __doc__
    """
    dup2(old_fd, new_fd)
    
    Duplicate file descriptor.
    """
    pass

def execv(path, args): # real signature unknown; restored from __doc__
    """
    execv(path, args)
    
    Execute an executable path with arguments, replacing current process.
    
        path: path of executable file
        args: tuple or list of strings
    """
    pass

def execve(path, args, env): # real signature unknown; restored from __doc__
    """
    execve(path, args, env)
    
    Execute a path with arguments and environment, replacing current process.
    
        path: path of executable file
        args: tuple or list of arguments
        env: dictionary of strings mapping to strings
    """
    pass

def fdopen(fd, mode='r', bufsize=None): # real signature unknown; restored from __doc__
    """
    fdopen(fd [, mode='r' [, bufsize]]) -> file_object
    
    Return an open file object connected to a file descriptor.
    """
    pass

def fstat(fd): # real signature unknown; restored from __doc__
    """
    fstat(fd) -> stat result
    
    Like stat(), but for an open file descriptor.
    """
    pass

def fsync(fildes): # real signature unknown; restored from __doc__
    """
    fsync(fildes)
    
    force write of file with filedescriptor to disk.
    """
    pass

def getcwd(): # real signature unknown; restored from __doc__
    """
    getcwd() -> path
    
    Return a string representing the current working directory.
    """
    pass

def getcwdu(): # real signature unknown; restored from __doc__
    """
    getcwdu() -> path
    
    Return a unicode string representing the current working directory.
    """
    pass

def getpid(): # real signature unknown; restored from __doc__
    """
    getpid() -> pid
    
    Return the current process id
    """
    pass

def isatty(fd): # real signature unknown; restored from __doc__
    """
    isatty(fd) -> bool
    
    Return True if the file descriptor 'fd' is an open file descriptor
    connected to the slave end of a terminal.
    """
    return False

def kill(pid, sig): # real signature unknown; restored from __doc__
    """
    kill(pid, sig)
    
    Kill a process with a signal.
    """
    pass

def listdir(path): # real signature unknown; restored from __doc__
    """
    listdir(path) -> list_of_strings
    
    Return a list containing the names of the entries in the directory.
    
        path: path of directory to list
    
    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.
    """
    pass

def lseek(fd, pos, how): # real signature unknown; restored from __doc__
    """
    lseek(fd, pos, how) -> newpos
    
    Set the current position of a file descriptor.
    """
    pass

def lstat(path): # real signature unknown; restored from __doc__
    """
    lstat(path) -> stat result
    
    Like stat(path), but do not follow symbolic links.
    """
    pass

def mkdir(path, mode=0777): # real signature unknown; restored from __doc__
    """
    mkdir(path [, mode=0777])
    
    Create a directory.
    """
    pass

def open(filename, flag, mode=0777): # real signature unknown; restored from __doc__
    """
    open(filename, flag [, mode=0777]) -> fd
    
    Open a file (for low level IO).
    """
    pass

def pipe(): # real signature unknown; restored from __doc__
    """
    pipe() -> (read_end, write_end)
    
    Create a pipe.
    """
    pass

def popen(command, mode='r', bufsize=None): # real signature unknown; restored from __doc__
    """
    popen(command [, mode='r' [, bufsize]]) -> pipe
    
    Open a pipe to/from a command returning a file object.
    """
    pass

def popen2(*args, **kwargs): # real signature unknown
    pass

def popen3(*args, **kwargs): # real signature unknown
    pass

def popen4(*args, **kwargs): # real signature unknown
    pass

def putenv(key, value): # real signature unknown; restored from __doc__
    """
    putenv(key, value)
    
    Change or add an environment variable.
    """
    pass

def read(fd, buffersize): # real signature unknown; restored from __doc__
    """
    read(fd, buffersize) -> string
    
    Read a file descriptor.
    """
    return ""

def remove(path): # real signature unknown; restored from __doc__
    """
    remove(path)
    
    Remove a file (same as unlink(path)).
    """
    pass

def rename(old, new): # real signature unknown; restored from __doc__
    """
    rename(old, new)
    
    Rename a file or directory.
    """
    pass

def rmdir(path): # real signature unknown; restored from __doc__
    """
    rmdir(path)
    
    Remove a directory.
    """
    pass

def spawnv(mode, path, args): # real signature unknown; restored from __doc__
    """
    spawnv(mode, path, args)
    
    Execute the program 'path' in a new process.
    
        mode: mode of process creation
        path: path of executable file
        args: tuple or list of strings
    """
    pass

def spawnve(mode, path, args, env): # real signature unknown; restored from __doc__
    """
    spawnve(mode, path, args, env)
    
    Execute the program 'path' in a new process.
    
        mode: mode of process creation
        path: path of executable file
        args: tuple or list of arguments
        env: dictionary of strings mapping to strings
    """
    pass

def startfile(filepath, operation=None): # real signature unknown; restored from __doc__
    """
    startfile(filepath [, operation]) - Start a file with its associated
    application.
    
    When "operation" is not specified or "open", this acts like
    double-clicking the file in Explorer, or giving the file name as an
    argument to the DOS "start" command: the file is opened with whatever
    application (if any) its extension is associated.
    When another "operation" is given, it specifies what should be done with
    the file.  A typical operation is "print".
    
    startfile returns as soon as the associated application is launched.
    There is no option to wait for the application to close, and no way
    to retrieve the application's exit status.
    
    The filepath is relative to the current directory.  If you want to use
    an absolute path, make sure the first character is not a slash ("/");
    the underlying Win32 ShellExecute function doesn't work if it is.
    """
    pass

def stat(path): # real signature unknown; restored from __doc__
    """
    stat(path) -> stat result
    
    Perform a stat system call on the given path.
    """
    pass

def stat_float_times(newval=None): # real signature unknown; restored from __doc__
    """
    stat_float_times([newval]) -> oldval
    
    Determine whether os.[lf]stat represents time stamps as float objects.
    If newval is True, future calls to stat() return floats, if it is False,
    future calls return ints. 
    If newval is omitted, return the current setting.
    """
    pass

def strerror(code): # real signature unknown; restored from __doc__
    """
    strerror(code) -> string
    
    Translate an error code to a message string.
    """
    return ""

def system(command): # real signature unknown; restored from __doc__
    """
    system(command) -> exit_status
    
    Execute the command (a string) in a subshell.
    """
    pass

def tempnam(dir=None, prefix=None): # real signature unknown; restored from __doc__
    """
    tempnam([dir[, prefix]]) -> string
    
    Return a unique name for a temporary file.
    The directory and a prefix may be specified as strings; they may be omitted
    or None if not needed.
    """
    return ""

def times(): # real signature unknown; restored from __doc__
    """
    times() -> (utime, stime, cutime, cstime, elapsed_time)
    
    Return a tuple of floating point numbers indicating process times.
    """
    pass

def tmpfile(): # real signature unknown; restored from __doc__
    """
    tmpfile() -> file object
    
    Create a temporary file with no directory entries.
    """
    return file('/dev/null')

def tmpnam(): # real signature unknown; restored from __doc__
    """
    tmpnam() -> string
    
    Return a unique name for a temporary file.
    """
    return ""

def umask(new_mask): # real signature unknown; restored from __doc__
    """
    umask(new_mask) -> old_mask
    
    Set the current numeric umask and return the previous umask.
    """
    pass

def unlink(path): # real signature unknown; restored from __doc__
    """
    unlink(path)
    
    Remove a file (same as remove(path)).
    """
    pass

def urandom(n): # real signature unknown; restored from __doc__
    """
    urandom(n) -> str
    
    Return n random bytes suitable for cryptographic use.
    """
    return ""

def utime(path, (atime, mtime)): # real signature unknown; restored from __doc__
    """
    utime(path, (atime, mtime))
    utime(path, None)
    
    Set the access and modified time of the file to the given values.  If the
    second form is used, set the access and modified times to the current time.
    """
    pass

def waitpid(pid, options): # real signature unknown; restored from __doc__
    """
    waitpid(pid, options) -> (pid, status << 8)
    
    Wait for completion of a given process.  options is ignored on Windows.
    """
    pass

def write(fd, string): # real signature unknown; restored from __doc__
    """
    write(fd, string) -> byteswritten
    
    Write a string to a file descriptor.
    """
    pass

def _exit(status): # real signature unknown; restored from __doc__
    """
    _exit(status)
    
    Exit to the system with specified status, without normal exit processing.
    """
    pass

def _getfullpathname(*args, **kwargs): # real signature unknown
    pass

def _isdir(*args, **kwargs): # real signature unknown
    """ Return true if the pathname refers to an existing directory. """
    pass

# classes

class statvfs_result(object):
    """
    statvfs_result: Result from statvfs or fstatvfs.
    
    This object may be accessed either as a tuple of
      (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
    or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
    
    See os.statvfs for more information.
    """
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    f_bavail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_bfree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_bsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_favail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_ffree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_flag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_frsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_namemax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    n_fields = 10
    n_sequence_fields = 10
    n_unnamed_fields = 0


class stat_result(object):
    """
    stat_result: Result from stat or lstat.
    
    This object may be accessed either as a tuple of
      (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
    
    Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
    or st_flags, they are available as attributes only.
    
    See os.stat for more information.
    """
    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mul__(self, n): # real signature unknown; restored from __doc__
        """ x.__mul__(n) <==> x*n """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rmul__(self, n): # real signature unknown; restored from __doc__
        """ x.__rmul__(n) <==> n*x """
        pass

    st_atime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last access"""

    st_ctime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last change"""

    st_dev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """device"""

    st_gid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """group ID of owner"""

    st_ino = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inode"""

    st_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """protection bits"""

    st_mtime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last modification"""

    st_nlink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number of hard links"""

    st_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total size, in bytes"""

    st_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user ID of owner"""


    n_fields = 13
    n_sequence_fields = 10
    n_unnamed_fields = 3


# variables with complex values

environ = {
    'ALLUSERSPROFILE': 'C:\\ProgramData',
    'APPDATA': 'C:\\Users\\Richard\\AppData\\Roaming',
    'CCHZPATH': 'D:\\Program Files (x86)\\CTEX\\CTeX\\cct\\fonts',
    'CCPKPATH': 'D:\\Program Files (x86)\\CTEX\\CTeX\\fonts\\pk\\modeless\\cct\\dpi$d',
    'CLASSPATH': '.;D:\\Program files\\Java\\jdk1.7.0\\lib;D:\\Program files\\Java\\jdk1.7.0\\lib\\tools.jar',
    'COMPUTERNAME': 'RICHARD-PC',
    'ComSpec': 'C:\\Windows\\system32\\cmd.exe',
    'CommonProgramFiles': 'C:\\Program Files\\Common Files',
    'CommonProgramFiles(x86)': 'C:\\Program Files (x86)\\Common Files',
    'CommonProgramW6432': 'C:\\Program Files\\Common Files',
    'FP_NO_HOST_CHECK': 'NO',
    'HOMEDRIVE': 'C:',
    'HOMEPATH': '\\Users\\Richard',
    'JAVA_HOME': 'D:\\Program files\\Java\\jdk1.7.0',
    'LOCALAPPDATA': 'C:\\Users\\Richard\\AppData\\Local',
    'LOGONSERVER': '\\\\RICHARD-PC',
    'MEMO_HOME': 'E:\\10.171.5.2_NTUInternship\\SLProblemTools\\MEMo_v1.1\\MEMo',
    'NUMBER_OF_PROCESSORS': '4',
    'OS': 'Windows_NT',
    'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC',
    'PROCESSOR_ARCHITECTURE': 'AMD64',
    'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 42 Stepping 7, GenuineIntel',
    'PROCESSOR_LEVEL': '6',
    'PROCESSOR_REVISION': '2a07',
    'PSModulePath': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\',
    'PUBLIC': 'C:\\Users\\Public',
    'Path': 'C:\\ProgramData\\Oracle\\Java\\javapath;D:\\MinGW\\bin;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\windows\\system32\\ping.exe;D:\\Program files\\Java\\jdk1.7.0\\bin;D:\\Program Files (x86)\\CTEX\\UserData\\miktex\\bin;D:\\Program Files (x86)\\CTEX\\MiKTeX\\miktex\\bin;D:\\Program Files (x86)\\CTEX\\CTeX\\ctex\\bin;D:\\Program Files (x86)\\CTEX\\CTeX\\cct\\bin;D:\\Program Files (x86)\\CTEX\\CTeX\\ty\\bin;D:\\Program Files (x86)\\CTEX\\Ghostscript\\gs9.05\\bin;D:\\Program Files (x86)\\CTEX\\GSview\\gsview;D:\\Program Files (x86)\\CTEX\\WinEdt;D:\\Program files\\MinGW\\MinGWStudio\\MinGW\\bin;E:\\10.171.5.2_NTUInternship\\SLProblemTools\\MEMo_v1.1\\MEMo\\bin;D:\\Program files\\Python27;D:\\Program Files\\nodejs\\;D:\\Program files\\Java\\jdk1.7.0\\bin;C:\\Program Files (x86)\\Windows Kits\\8.1\\Windows Performance Toolkit\\;C:\\Program Files\\Microsoft SQL Server\\110\\Tools\\Binn\\;C:\\Program Files (x86)\\Microsoft SDKs\\TypeScript\\1.0\\;C:\\Program Files\\Microsoft SQL Server\\120\\Tools\\Binn\\;C:\\Users\\Richard\\AppData\\Roaming\\npm',
    'ProgramData': 'C:\\ProgramData',
    'ProgramFiles': 'C:\\Program Files',
    'ProgramFiles(x86)': 'C:\\Program Files (x86)',
    'ProgramW6432': 'C:\\Program Files',
    'SESSIONNAME': 'Console',
    'SystemDrive': 'C:',
    'SystemRoot': 'C:\\Windows',
    'TEMP': 'C:\\Users\\Richard\\AppData\\Local\\Temp',
    'TMP': 'C:\\Users\\Richard\\AppData\\Local\\Temp',
    'USERDOMAIN': 'Richard-PC',
    'USERNAME': 'Richard',
    'USERPROFILE': 'C:\\Users\\Richard',
    'VS100COMNTOOLS': 'D:\\Program Files (x86)\\Microsoft Visual Studio 10.0\\Common7\\Tools\\',
    'VS110COMNTOOLS': 'C:\\Program Files (x86)\\Microsoft Visual Studio 11.0\\Common7\\Tools\\',
    'VS120COMNTOOLS': 'D:\\Program Files (x86)\\Microsoft Visual Studio 12.0\\Common7\\Tools\\',
    'windir': 'C:\\Windows',
    'windows_tracing_flags': '3',
    'windows_tracing_logfile': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log',
}

