# encoding: utf-8
# module numpy.core.multiarray
# from D:\Program files\Python27\lib\site-packages\numpy\core\multiarray.pyd
# by generator 1.136
# no doc

# imports
from exceptions import error


# Variables with simple values

ALLOW_THREADS = 1

BUFSIZE = 8192

CLIP = 0

ITEM_HASOBJECT = 1

ITEM_IS_POINTER = 4

LIST_PICKLE = 2

MAXDIMS = 32

NEEDS_INIT = 8
NEEDS_PYAPI = 16

RAISE = 2

USE_GETITEM = 32
USE_SETITEM = 64

WRAP = 1

__version__ = '3.1'

# functions

def arange(start=None, stop=None, step=None, dtype=None): # known case of numpy.core.multiarray.arange
    """
    arange([start,] stop[, step,], dtype=None)
    
        Return evenly spaced values within a given interval.
    
        Values are generated within the half-open interval ``[start, stop)``
        (in other words, the interval including `start` but excluding `stop`).
        For integer arguments the function is equivalent to the Python built-in
        `range <http://docs.python.org/lib/built-in-funcs.html>`_ function,
        but returns an ndarray rather than a list.
    
        When using a non-integer step, such as 0.1, the results will often not
        be consistent.  It is better to use ``linspace`` for these cases.
    
        Parameters
        ----------
        start : number, optional
            Start of interval.  The interval includes this value.  The default
            start value is 0.
        stop : number
            End of interval.  The interval does not include this value, except
            in some cases where `step` is not an integer and floating point
            round-off affects the length of `out`.
        step : number, optional
            Spacing between values.  For any output `out`, this is the distance
            between two adjacent values, ``out[i+1] - out[i]``.  The default
            step size is 1.  If `step` is specified, `start` must also be given.
        dtype : dtype
            The type of the output array.  If `dtype` is not given, infer the data
            type from the other input arguments.
    
        Returns
        -------
        arange : ndarray
            Array of evenly spaced values.
    
            For floating point arguments, the length of the result is
            ``ceil((stop - start)/step)``.  Because of floating point overflow,
            this rule may result in the last element of `out` being greater
            than `stop`.
    
        See Also
        --------
        linspace : Evenly spaced numbers with careful handling of endpoints.
        ogrid: Arrays of evenly spaced numbers in N-dimensions.
        mgrid: Grid-shaped arrays of evenly spaced numbers in N-dimensions.
    
        Examples
        --------
        >>> np.arange(3)
        array([0, 1, 2])
        >>> np.arange(3.0)
        array([ 0.,  1.,  2.])
        >>> np.arange(3,7)
        array([3, 4, 5, 6])
        >>> np.arange(3,7,2)
        array([3, 5])
    """
    pass

def array(p_object, dtype=None, copy=True, order=None, subok=False, ndmin=0): # real signature unknown; restored from __doc__
    """
    array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
    
        Create an array.
    
        Parameters
        ----------
        object : array_like
            An array, any object exposing the array interface, an
            object whose __array__ method returns an array, or any
            (nested) sequence.
        dtype : data-type, optional
            The desired data-type for the array.  If not given, then
            the type will be determined as the minimum type required
            to hold the objects in the sequence.  This argument can only
            be used to 'upcast' the array.  For downcasting, use the
            .astype(t) method.
        copy : bool, optional
            If true (default), then the object is copied.  Otherwise, a copy
            will only be made if __array__ returns a copy, if obj is a
            nested sequence, or if a copy is needed to satisfy any of the other
            requirements (`dtype`, `order`, etc.).
        order : {'C', 'F', 'A'}, optional
            Specify the order of the array.  If order is 'C' (default), then the
            array will be in C-contiguous order (last-index varies the
            fastest).  If order is 'F', then the returned array
            will be in Fortran-contiguous order (first-index varies the
            fastest).  If order is 'A', then the returned array may
            be in any order (either C-, Fortran-contiguous, or even
            discontiguous).
        subok : bool, optional
            If True, then sub-classes will be passed-through, otherwise
            the returned array will be forced to be a base-class array (default).
        ndmin : int, optional
            Specifies the minimum number of dimensions that the resulting
            array should have.  Ones will be pre-pended to the shape as
            needed to meet this requirement.
    
        Returns
        -------
        out : ndarray
            An array object satisfying the specified requirements.
    
        See Also
        --------
        empty, empty_like, zeros, zeros_like, ones, ones_like, fill
    
        Examples
        --------
        >>> np.array([1, 2, 3])
        array([1, 2, 3])
    
        Upcasting:
    
        >>> np.array([1, 2, 3.0])
        array([ 1.,  2.,  3.])
    
        More than one dimension:
    
        >>> np.array([[1, 2], [3, 4]])
        array([[1, 2],
               [3, 4]])
    
        Minimum dimensions 2:
    
        >>> np.array([1, 2, 3], ndmin=2)
        array([[1, 2, 3]])
    
        Type provided:
    
        >>> np.array([1, 2, 3], dtype=complex)
        array([ 1.+0.j,  2.+0.j,  3.+0.j])
    
        Data-type consisting of more than one element:
    
        >>> x = np.array([(1,2),(3,4)],dtype=[('a','<i4'),('b','<i4')])
        >>> x['a']
        array([1, 3])
    
        Creating an array from sub-classes:
    
        >>> np.array(np.mat('1 2; 3 4'))
        array([[1, 2],
               [3, 4]])
    
        >>> np.array(np.mat('1 2; 3 4'), subok=True)
        matrix([[1, 2],
                [3, 4]])
    """
    pass

def busday_count(begindates, enddates, weekmask='1111100', holidays=[], busdaycal=None, out=None): # real signature unknown; restored from __doc__
    """
    busday_count(begindates, enddates, weekmask='1111100', holidays=[], busdaycal=None, out=None)
    
        Counts the number of valid days between `begindates` and
        `enddates`, not including the day of `enddates`.
    
        If ``enddates`` specifies a date value that is earlier than the
        corresponding ``begindates`` date value, the count will be negative.
    
        .. versionadded:: 1.7.0
    
        Parameters
        ----------
        begindates : array_like of datetime64[D]
            The array of the first dates for counting.
        enddates : array_like of datetime64[D]
            The array of the end dates for counting, which are excluded
            from the count themselves.
        weekmask : str or array_like of bool, optional
            A seven-element array indicating which of Monday through Sunday are
            valid days. May be specified as a length-seven list or array, like
            [1,1,1,1,1,0,0]; a length-seven string, like '1111100'; or a string
            like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for
            weekdays, optionally separated by white space. Valid abbreviations
            are: Mon Tue Wed Thu Fri Sat Sun
        holidays : array_like of datetime64[D], optional
            An array of dates to consider as invalid dates.  They may be
            specified in any order, and NaT (not-a-time) dates are ignored.
            This list is saved in a normalized form that is suited for
            fast calculations of valid days.
        busdaycal : busdaycalendar, optional
            A `busdaycalendar` object which specifies the valid days. If this
            parameter is provided, neither weekmask nor holidays may be
            provided.
        out : array of int, optional
            If provided, this array is filled with the result.
    
        Returns
        -------
        out : array of int
            An array with a shape from broadcasting ``begindates`` and ``enddates``
            together, containing the number of valid days between
            the begin and end dates.
    
        See Also
        --------
        busdaycalendar: An object that specifies a custom set of valid days.
        is_busday : Returns a boolean array indicating valid days.
        busday_offset : Applies an offset counted in valid days.
    
        Examples
        --------
        >>> # Number of weekdays in January 2011
        ... np.busday_count('2011-01', '2011-02')
        21
        >>> # Number of weekdays in 2011
        ...  np.busday_count('2011', '2012')
        260
        >>> # Number of Saturdays in 2011
        ... np.busday_count('2011', '2012', weekmask='Sat')
        53
    """
    pass

def busday_offset(dates, offsets, roll='raise', weekmask='1111100', holidays=None, busdaycal=None, out=None): # real signature unknown; restored from __doc__
    """
    busday_offset(dates, offsets, roll='raise', weekmask='1111100', holidays=None, busdaycal=None, out=None)
    
        First adjusts the date to fall on a valid day according to
        the ``roll`` rule, then applies offsets to the given dates
        counted in valid days.
    
        .. versionadded:: 1.7.0
    
        Parameters
        ----------
        dates : array_like of datetime64[D]
            The array of dates to process.
        offsets : array_like of int
            The array of offsets, which is broadcast with ``dates``.
        roll : {'raise', 'nat', 'forward', 'following', 'backward', 'preceding', 'modifiedfollowing', 'modifiedpreceding'}, optional
            How to treat dates that do not fall on a valid day. The default
            is 'raise'.
    
              * 'raise' means to raise an exception for an invalid day.
              * 'nat' means to return a NaT (not-a-time) for an invalid day.
              * 'forward' and 'following' mean to take the first valid day
                later in time.
              * 'backward' and 'preceding' mean to take the first valid day
                earlier in time.
              * 'modifiedfollowing' means to take the first valid day
                later in time unless it is across a Month boundary, in which
                case to take the first valid day earlier in time.
              * 'modifiedpreceding' means to take the first valid day
                earlier in time unless it is across a Month boundary, in which
                case to take the first valid day later in time.
        weekmask : str or array_like of bool, optional
            A seven-element array indicating which of Monday through Sunday are
            valid days. May be specified as a length-seven list or array, like
            [1,1,1,1,1,0,0]; a length-seven string, like '1111100'; or a string
            like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for
            weekdays, optionally separated by white space. Valid abbreviations
            are: Mon Tue Wed Thu Fri Sat Sun
        holidays : array_like of datetime64[D], optional
            An array of dates to consider as invalid dates.  They may be
            specified in any order, and NaT (not-a-time) dates are ignored.
            This list is saved in a normalized form that is suited for
            fast calculations of valid days.
        busdaycal : busdaycalendar, optional
            A `busdaycalendar` object which specifies the valid days. If this
            parameter is provided, neither weekmask nor holidays may be
            provided.
        out : array of datetime64[D], optional
            If provided, this array is filled with the result.
    
        Returns
        -------
        out : array of datetime64[D]
            An array with a shape from broadcasting ``dates`` and ``offsets``
            together, containing the dates with offsets applied.
    
        See Also
        --------
        busdaycalendar: An object that specifies a custom set of valid days.
        is_busday : Returns a boolean array indicating valid days.
        busday_count : Counts how many valid days are in a half-open date range.
    
        Examples
        --------
        >>> # First business day in October 2011 (not accounting for holidays)
        ... np.busday_offset('2011-10', 0, roll='forward')
        numpy.datetime64('2011-10-03','D')
        >>> # Last business day in February 2012 (not accounting for holidays)
        ... np.busday_offset('2012-03', -1, roll='forward')
        numpy.datetime64('2012-02-29','D')
        >>> # Third Wednesday in January 2011
        ... np.busday_offset('2011-01', 2, roll='forward', weekmask='Wed')
        numpy.datetime64('2011-01-19','D')
        >>> # 2012 Mother's Day in Canada and the U.S.
        ... np.busday_offset('2012-05', 1, roll='forward', weekmask='Sun')
        numpy.datetime64('2012-05-13','D')
    
        >>> # First business day on or after a date
        ... np.busday_offset('2011-03-20', 0, roll='forward')
        numpy.datetime64('2011-03-21','D')
        >>> np.busday_offset('2011-03-22', 0, roll='forward')
        numpy.datetime64('2011-03-22','D')
        >>> # First business day after a date
        ... np.busday_offset('2011-03-20', 1, roll='backward')
        numpy.datetime64('2011-03-21','D')
        >>> np.busday_offset('2011-03-22', 1, roll='backward')
        numpy.datetime64('2011-03-23','D')
    """
    pass

def can_cast(from, totype, casting='safe'): # real signature unknown; restored from __doc__
    """
    can_cast(from, totype, casting = 'safe')
    
        Returns True if cast between data types can occur according to the
        casting rule.  If from is a scalar or array scalar, also returns
        True if the scalar value can be cast without overflow or truncation
        to an integer.
    
        Parameters
        ----------
        from : dtype, dtype specifier, scalar, or array
            Data type, scalar, or array to cast from.
        totype : dtype or dtype specifier
            Data type to cast to.
        casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
            Controls what kind of data casting may occur.
    
              * 'no' means the data types should not be cast at all.
              * 'equiv' means only byte-order changes are allowed.
              * 'safe' means only casts which can preserve values are allowed.
              * 'same_kind' means only safe casts or casts within a kind,
                like float64 to float32, are allowed.
              * 'unsafe' means any data conversions may be done.
    
        Returns
        -------
        out : bool
            True if cast can occur according to the casting rule.
    
        See also
        --------
        dtype, result_type
    
        Examples
        --------
    
        Basic examples
    
        >>> np.can_cast(np.int32, np.int64)
        True
        >>> np.can_cast(np.float64, np.complex)
        True
        >>> np.can_cast(np.complex, np.float)
        False
    
        >>> np.can_cast('i8', 'f8')
        True
        >>> np.can_cast('i8', 'f4')
        False
        >>> np.can_cast('i4', 'S4')
        True
    
        Casting scalars
    
        >>> np.can_cast(100, 'i1')
        True
        >>> np.can_cast(150, 'i1')
        False
        >>> np.can_cast(150, 'u1')
        True
    
        >>> np.can_cast(3.5e100, np.float32)
        False
        >>> np.can_cast(1000.0, np.float32)
        True
    
        Array scalar checks the value, array does not
    
        >>> np.can_cast(np.array(1000.0), np.float32)
        True
        >>> np.can_cast(np.array([1000.0]), np.float32)
        False
    
        Using the casting rules
    
        >>> np.can_cast('i8', 'i8', 'no')
        True
        >>> np.can_cast('<i8', '>i8', 'no')
        False
    
        >>> np.can_cast('<i8', '>i8', 'equiv')
        True
        >>> np.can_cast('<i4', '>i8', 'equiv')
        False
    
        >>> np.can_cast('<i4', '>i8', 'safe')
        True
        >>> np.can_cast('<i8', '>i4', 'safe')
        False
    
        >>> np.can_cast('<i8', '>i4', 'same_kind')
        True
        >>> np.can_cast('<i8', '>u4', 'same_kind')
        False
    
        >>> np.can_cast('<i8', '>u4', 'unsafe')
        True
    """
    pass

def compare_chararrays(*args, **kwargs): # real signature unknown
    pass

def concatenate(a_tuple, axis=0): # real signature unknown; restored from __doc__
    """
    concatenate((a1, a2, ...), axis=0)
    
        Join a sequence of arrays together.
    
        Parameters
        ----------
        a1, a2, ... : sequence of array_like
            The arrays must have the same shape, except in the dimension
            corresponding to `axis` (the first, by default).
        axis : int, optional
            The axis along which the arrays will be joined.  Default is 0.
    
        Returns
        -------
        res : ndarray
            The concatenated array.
    
        See Also
        --------
        ma.concatenate : Concatenate function that preserves input masks.
        array_split : Split an array into multiple sub-arrays of equal or
                      near-equal size.
        split : Split array into a list of multiple sub-arrays of equal size.
        hsplit : Split array into multiple sub-arrays horizontally (column wise)
        vsplit : Split array into multiple sub-arrays vertically (row wise)
        dsplit : Split array into multiple sub-arrays along the 3rd axis (depth).
        hstack : Stack arrays in sequence horizontally (column wise)
        vstack : Stack arrays in sequence vertically (row wise)
        dstack : Stack arrays in sequence depth wise (along third dimension)
    
        Notes
        -----
        When one or more of the arrays to be concatenated is a MaskedArray,
        this function will return a MaskedArray object instead of an ndarray,
        but the input masks are *not* preserved. In cases where a MaskedArray
        is expected as input, use the ma.concatenate function from the masked
        array module instead.
    
        Examples
        --------
        >>> a = np.array([[1, 2], [3, 4]])
        >>> b = np.array([[5, 6]])
        >>> np.concatenate((a, b), axis=0)
        array([[1, 2],
               [3, 4],
               [5, 6]])
        >>> np.concatenate((a, b.T), axis=1)
        array([[1, 2, 5],
               [3, 4, 6]])
    
        This function will not preserve masking of MaskedArray inputs.
    
        >>> a = np.ma.arange(3)
        >>> a[1] = np.ma.masked
        >>> b = np.arange(2, 5)
        >>> a
        masked_array(data = [0 -- 2],
                     mask = [False  True False],
               fill_value = 999999)
        >>> b
        array([2, 3, 4])
        >>> np.concatenate([a, b])
        masked_array(data = [0 1 2 2 3 4],
                     mask = False,
               fill_value = 999999)
        >>> np.ma.concatenate([a, b])
        masked_array(data = [0 -- 2 2 3 4],
                     mask = [False  True False False False False],
               fill_value = 999999)
    """
    pass

def copyto(dst, src, casting='same_kind', where=None, preservena=False): # real signature unknown; restored from __doc__
    """
    copyto(dst, src, casting='same_kind', where=None, preservena=False)
    
        Copies values from one array to another, broadcasting as necessary.
    
        Raises a TypeError if the `casting` rule is violated, and if
        `where` is provided, it selects which elements to copy.
    
        .. versionadded:: 1.7.0
    
        Parameters
        ----------
        dst : ndarray
            The array into which values are copied.
        src : array_like
            The array from which values are copied.
        casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
            Controls what kind of data casting may occur when copying.
    
              * 'no' means the data types should not be cast at all.
              * 'equiv' means only byte-order changes are allowed.
              * 'safe' means only casts which can preserve values are allowed.
              * 'same_kind' means only safe casts or casts within a kind,
                like float64 to float32, are allowed.
              * 'unsafe' means any data conversions may be done.
        where : array_like of bool, optional
            A boolean array which is broadcasted to match the dimensions
            of `dst`, and selects elements to copy from `src` to `dst`
            wherever it contains the value True.
        preservena : bool, optional
            If set to True, leaves any NA values in `dst` untouched. This
            is similar to the "hard mask" feature in numpy.ma.
    """
    pass

def correlate(a, v, mode=0): # real signature unknown; restored from __doc__
    """ cross_correlate(a,v, mode=0) """
    pass

def correlate2(*args, **kwargs): # real signature unknown
    pass

def count_nonzero(a): # real signature unknown; restored from __doc__
    """
    count_nonzero(a)
    
        Counts the number of non-zero values in the array ``a``.
    
        Parameters
        ----------
        a : array_like
            The array for which to count non-zeros.
    
        Returns
        -------
        count : int or array of int
            Number of non-zero values in the array.
    
        See Also
        --------
        nonzero : Return the coordinates of all the non-zero values.
    
        Examples
        --------
        >>> np.count_nonzero(np.eye(4))
        4
        >>> np.count_nonzero([[0,1,7,0,0],[3,0,0,2,19]])
        5
    """
    pass

def datetime_as_string(*args, **kwargs): # real signature unknown
    pass

def datetime_data(*args, **kwargs): # real signature unknown
    pass

def dot(*args, **kwargs): # real signature unknown
    pass

def einsum(subscripts, *operands, out=None, dtype=None, order='K', casting='safe'): # real signature unknown; restored from __doc__
    """
    einsum(subscripts, *operands, out=None, dtype=None, order='K', casting='safe')
    
        Evaluates the Einstein summation convention on the operands.
    
        Using the Einstein summation convention, many common multi-dimensional
        array operations can be represented in a simple fashion.  This function
        provides a way compute such summations. The best way to understand this
        function is to try the examples below, which show how many common NumPy
        functions can be implemented as calls to `einsum`.
    
        Parameters
        ----------
        subscripts : str
            Specifies the subscripts for summation.
        operands : list of array_like
            These are the arrays for the operation.
        out : ndarray, optional
            If provided, the calculation is done into this array.
        dtype : data-type, optional
            If provided, forces the calculation to use the data type specified.
            Note that you may have to also give a more liberal `casting`
            parameter to allow the conversions.
        order : {'C', 'F', 'A', or 'K'}, optional
            Controls the memory layout of the output. 'C' means it should
            be C contiguous. 'F' means it should be Fortran contiguous,
            'A' means it should be 'F' if the inputs are all 'F', 'C' otherwise.
            'K' means it should be as close to the layout as the inputs as
            is possible, including arbitrarily permuted axes.
            Default is 'K'.
        casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
            Controls what kind of data casting may occur.  Setting this to
            'unsafe' is not recommended, as it can adversely affect accumulations.
    
              * 'no' means the data types should not be cast at all.
              * 'equiv' means only byte-order changes are allowed.
              * 'safe' means only casts which can preserve values are allowed.
              * 'same_kind' means only safe casts or casts within a kind,
                like float64 to float32, are allowed.
              * 'unsafe' means any data conversions may be done.
    
        Returns
        -------
        output : ndarray
            The calculation based on the Einstein summation convention.
    
        See Also
        --------
        dot, inner, outer, tensordot
    
        Notes
        -----
        .. versionadded:: 1.6.0
    
        The subscripts string is a comma-separated list of subscript labels,
        where each label refers to a dimension of the corresponding operand.
        Repeated subscripts labels in one operand take the diagonal.  For example,
        ``np.einsum('ii', a)`` is equivalent to ``np.trace(a)``.
    
        Whenever a label is repeated, it is summed, so ``np.einsum('i,i', a, b)``
        is equivalent to ``np.inner(a,b)``.  If a label appears only once,
        it is not summed, so ``np.einsum('i', a)`` produces a view of ``a``
        with no changes.
    
        The order of labels in the output is by default alphabetical.  This
        means that ``np.einsum('ij', a)`` doesn't affect a 2D array, while
        ``np.einsum('ji', a)`` takes its transpose.
    
        The output can be controlled by specifying output subscript labels
        as well.  This specifies the label order, and allows summing to
        be disallowed or forced when desired.  The call ``np.einsum('i->', a)``
        is like ``np.sum(a, axis=-1)``, and ``np.einsum('ii->i', a)``
        is like ``np.diag(a)``.  The difference is that `einsum` does not
        allow broadcasting by default.
    
        To enable and control broadcasting, use an ellipsis.  Default
        NumPy-style broadcasting is done by adding an ellipsis
        to the left of each term, like ``np.einsum('...ii->...i', a)``.
        To take the trace along the first and last axes,
        you can do ``np.einsum('i...i', a)``, or to do a matrix-matrix
        product with the left-most indices instead of rightmost, you can do
        ``np.einsum('ij...,jk...->ik...', a, b)``.
    
        When there is only one operand, no axes are summed, and no output
        parameter is provided, a view into the operand is returned instead
        of a new array.  Thus, taking the diagonal as ``np.einsum('ii->i', a)``
        produces a view.
    
        An alternative way to provide the subscripts and operands is as
        ``einsum(op0, sublist0, op1, sublist1, ..., [sublistout])``. The examples
        below have corresponding `einsum` calls with the two parameter methods.
    
        Examples
        --------
        >>> a = np.arange(25).reshape(5,5)
        >>> b = np.arange(5)
        >>> c = np.arange(6).reshape(2,3)
    
        >>> np.einsum('ii', a)
        60
        >>> np.einsum(a, [0,0])
        60
        >>> np.trace(a)
        60
    
        >>> np.einsum('ii->i', a)
        array([ 0,  6, 12, 18, 24])
        >>> np.einsum(a, [0,0], [0])
        array([ 0,  6, 12, 18, 24])
        >>> np.diag(a)
        array([ 0,  6, 12, 18, 24])
    
        >>> np.einsum('ij,j', a, b)
        array([ 30,  80, 130, 180, 230])
        >>> np.einsum(a, [0,1], b, [1])
        array([ 30,  80, 130, 180, 230])
        >>> np.dot(a, b)
        array([ 30,  80, 130, 180, 230])
    
        >>> np.einsum('ji', c)
        array([[0, 3],
               [1, 4],
               [2, 5]])
        >>> np.einsum(c, [1,0])
        array([[0, 3],
               [1, 4],
               [2, 5]])
        >>> c.T
        array([[0, 3],
               [1, 4],
               [2, 5]])
    
        >>> np.einsum('..., ...', 3, c)
        array([[ 0,  3,  6],
               [ 9, 12, 15]])
        >>> np.einsum(3, [Ellipsis], c, [Ellipsis])
        array([[ 0,  3,  6],
               [ 9, 12, 15]])
        >>> np.multiply(3, c)
        array([[ 0,  3,  6],
               [ 9, 12, 15]])
    
        >>> np.einsum('i,i', b, b)
        30
        >>> np.einsum(b, [0], b, [0])
        30
        >>> np.inner(b,b)
        30
    
        >>> np.einsum('i,j', np.arange(2)+1, b)
        array([[0, 1, 2, 3, 4],
               [0, 2, 4, 6, 8]])
        >>> np.einsum(np.arange(2)+1, [0], b, [1])
        array([[0, 1, 2, 3, 4],
               [0, 2, 4, 6, 8]])
        >>> np.outer(np.arange(2)+1, b)
        array([[0, 1, 2, 3, 4],
               [0, 2, 4, 6, 8]])
    
        >>> np.einsum('i...->...', a)
        array([50, 55, 60, 65, 70])
        >>> np.einsum(a, [0,Ellipsis], [Ellipsis])
        array([50, 55, 60, 65, 70])
        >>> np.sum(a, axis=0)
        array([50, 55, 60, 65, 70])
    
        >>> a = np.arange(60.).reshape(3,4,5)
        >>> b = np.arange(24.).reshape(4,3,2)
        >>> np.einsum('ijk,jil->kl', a, b)
        array([[ 4400.,  4730.],
               [ 4532.,  4874.],
               [ 4664.,  5018.],
               [ 4796.,  5162.],
               [ 4928.,  5306.]])
        >>> np.einsum(a, [0,1,2], b, [1,0,3], [2,3])
        array([[ 4400.,  4730.],
               [ 4532.,  4874.],
               [ 4664.,  5018.],
               [ 4796.,  5162.],
               [ 4928.,  5306.]])
        >>> np.tensordot(a,b, axes=([1,0],[0,1]))
        array([[ 4400.,  4730.],
               [ 4532.,  4874.],
               [ 4664.,  5018.],
               [ 4796.,  5162.],
               [ 4928.,  5306.]])
    """
    pass

def empty(shape, dtype=None, order='C'): # real signature unknown; restored from __doc__
    """
    empty(shape, dtype=float, order='C')
    
        Return a new array of given shape and type, without initializing entries.
    
        Parameters
        ----------
        shape : int or tuple of int
            Shape of the empty array
        dtype : data-type, optional
            Desired output data-type.
        order : {'C', 'F'}, optional
            Whether to store multi-dimensional data in C (row-major) or
            Fortran (column-major) order in memory.
    
        See Also
        --------
        empty_like, zeros, ones
    
        Notes
        -----
        `empty`, unlike `zeros`, does not set the array values to zero,
        and may therefore be marginally faster.  On the other hand, it requires
        the user to manually set all the values in the array, and should be
        used with caution.
    
        Examples
        --------
        >>> np.empty([2, 2])
        array([[ -9.74499359e+001,   6.69583040e-309],
               [  2.13182611e-314,   3.06959433e-309]])         #random
    
        >>> np.empty([2, 2], dtype=int)
        array([[-1073741821, -1067949133],
               [  496041986,    19249760]])                     #random
    """
    pass

def empty_like(a, dtype=None, order='K', subok=True): # real signature unknown; restored from __doc__
    """
    empty_like(a, dtype=None, order='K', subok=True)
    
        Return a new array with the same shape and type as a given array.
    
        Parameters
        ----------
        a : array_like
            The shape and data-type of `a` define these same attributes of the
            returned array.
        dtype : data-type, optional
            Overrides the data type of the result.
        order : {'C', 'F', 'A', or 'K'}, optional
            Overrides the memory layout of the result. 'C' means C-order,
            'F' means F-order, 'A' means 'F' if ``a`` is Fortran contiguous,
            'C' otherwise. 'K' means match the layout of ``a`` as closely
            as possible.
        subok : bool, optional.
            If True, then the newly created array will use the sub-class
            type of 'a', otherwise it will be a base-class array. Defaults
            to True.
    
        Returns
        -------
        out : ndarray
            Array of uninitialized (arbitrary) data with the same
            shape and type as `a`.
    
        See Also
        --------
        ones_like : Return an array of ones with shape and type of input.
        zeros_like : Return an array of zeros with shape and type of input.
        empty : Return a new uninitialized array.
        ones : Return a new array setting values to one.
        zeros : Return a new array setting values to zero.
    
        Notes
        -----
        This function does *not* initialize the returned array; to do that use
        `zeros_like` or `ones_like` instead.  It may be marginally faster than
        the functions that do set the array values.
    
        Examples
        --------
        >>> a = ([1,2,3], [4,5,6])                         # a is array-like
        >>> np.empty_like(a)
        array([[-1073741821, -1073741821,           3],    #random
               [          0,           0, -1073741821]])
        >>> a = np.array([[1., 2., 3.],[4.,5.,6.]])
        >>> np.empty_like(a)
        array([[ -2.00000715e+000,   1.48219694e-323,  -2.00000572e+000],#random
               [  4.38791518e-305,  -2.00000715e+000,   4.17269252e-309]])
    """
    pass

def format_longfloat(*args, **kwargs): # real signature unknown
    pass

def frombuffer(buffer, dtype=None, count=-1, offset=0): # real signature unknown; restored from __doc__
    """
    frombuffer(buffer, dtype=float, count=-1, offset=0)
    
        Interpret a buffer as a 1-dimensional array.
    
        Parameters
        ----------
        buffer : buffer_like
            An object that exposes the buffer interface.
        dtype : data-type, optional
            Data-type of the returned array; default: float.
        count : int, optional
            Number of items to read. ``-1`` means all data in the buffer.
        offset : int, optional
            Start reading the buffer from this offset; default: 0.
    
        Notes
        -----
        If the buffer has data that is not in machine byte-order, this should
        be specified as part of the data-type, e.g.::
    
          >>> dt = np.dtype(int)
          >>> dt = dt.newbyteorder('>')
          >>> np.frombuffer(buf, dtype=dt)
    
        The data of the resulting array will not be byteswapped, but will be
        interpreted correctly.
    
        Examples
        --------
        >>> s = 'hello world'
        >>> np.frombuffer(s, dtype='S1', count=5, offset=6)
        array(['w', 'o', 'r', 'l', 'd'],
              dtype='|S1')
    """
    pass

def fromfile(file, dtype=None, count=-1, sep=''): # real signature unknown; restored from __doc__
    """
    fromfile(file, dtype=float, count=-1, sep='')
    
        Construct an array from data in a text or binary file.
    
        A highly efficient way of reading binary data with a known data-type,
        as well as parsing simply formatted text files.  Data written using the
        `tofile` method can be read using this function.
    
        Parameters
        ----------
        file : file or str
            Open file object or filename.
        dtype : data-type
            Data type of the returned array.
            For binary files, it is used to determine the size and byte-order
            of the items in the file.
        count : int
            Number of items to read. ``-1`` means all items (i.e., the complete
            file).
        sep : str
            Separator between items if file is a text file.
            Empty ("") separator means the file should be treated as binary.
            Spaces (" ") in the separator match zero or more whitespace characters.
            A separator consisting only of spaces must match at least one
            whitespace.
    
        See also
        --------
        load, save
        ndarray.tofile
        loadtxt : More flexible way of loading data from a text file.
    
        Notes
        -----
        Do not rely on the combination of `tofile` and `fromfile` for
        data storage, as the binary files generated are are not platform
        independent.  In particular, no byte-order or data-type information is
        saved.  Data can be stored in the platform independent ``.npy`` format
        using `save` and `load` instead.
    
        Examples
        --------
        Construct an ndarray:
    
        >>> dt = np.dtype([('time', [('min', int), ('sec', int)]),
        ...                ('temp', float)])
        >>> x = np.zeros((1,), dtype=dt)
        >>> x['time']['min'] = 10; x['temp'] = 98.25
        >>> x
        array([((10, 0), 98.25)],
              dtype=[('time', [('min', '<i4'), ('sec', '<i4')]), ('temp', '<f8')])
    
        Save the raw data to disk:
    
        >>> import os
        >>> fname = os.tmpnam()
        >>> x.tofile(fname)
    
        Read the raw data from disk:
    
        >>> np.fromfile(fname, dtype=dt)
        array([((10, 0), 98.25)],
              dtype=[('time', [('min', '<i4'), ('sec', '<i4')]), ('temp', '<f8')])
    
        The recommended way to store and load data:
    
        >>> np.save(fname, x)
        >>> np.load(fname + '.npy')
        array([((10, 0), 98.25)],
              dtype=[('time', [('min', '<i4'), ('sec', '<i4')]), ('temp', '<f8')])
    """
    pass

def fromiter(iterable, dtype, count=-1): # real signature unknown; restored from __doc__
    """
    fromiter(iterable, dtype, count=-1)
    
        Create a new 1-dimensional array from an iterable object.
    
        Parameters
        ----------
        iterable : iterable object
            An iterable object providing data for the array.
        dtype : data-type
            The data-type of the returned array.
        count : int, optional
            The number of items to read from *iterable*.  The default is -1,
            which means all data is read.
    
        Returns
        -------
        out : ndarray
            The output array.
    
        Notes
        -----
        Specify `count` to improve performance.  It allows ``fromiter`` to
        pre-allocate the output array, instead of resizing it on demand.
    
        Examples
        --------
        >>> iterable = (x*x for x in range(5))
        >>> np.fromiter(iterable, np.float)
        array([  0.,   1.,   4.,   9.,  16.])
    """
    pass

def fromstring(string, dtype=None, count=-1, sep=''): # real signature unknown; restored from __doc__
    """
    fromstring(string, dtype=float, count=-1, sep='')
    
        A new 1-D array initialized from raw binary or text data in a string.
    
        Parameters
        ----------
        string : str
            A string containing the data.
        dtype : data-type, optional
            The data type of the array; default: float.  For binary input data,
            the data must be in exactly this format.
        count : int, optional
            Read this number of `dtype` elements from the data.  If this is
            negative (the default), the count will be determined from the
            length of the data.
        sep : str, optional
            If not provided or, equivalently, the empty string, the data will
            be interpreted as binary data; otherwise, as ASCII text with
            decimal numbers.  Also in this latter case, this argument is
            interpreted as the string separating numbers in the data; extra
            whitespace between elements is also ignored.
    
        Returns
        -------
        arr : ndarray
            The constructed array.
    
        Raises
        ------
        ValueError
            If the string is not the correct size to satisfy the requested
            `dtype` and `count`.
    
        See Also
        --------
        frombuffer, fromfile, fromiter
    
        Examples
        --------
        >>> np.fromstring('\x01\x02', dtype=np.uint8)
        array([1, 2], dtype=uint8)
        >>> np.fromstring('1 2', dtype=int, sep=' ')
        array([1, 2])
        >>> np.fromstring('1, 2', dtype=int, sep=',')
        array([1, 2])
        >>> np.fromstring('\x01\x02\x03\x04\x05', dtype=np.uint8, count=3)
        array([1, 2, 3], dtype=uint8)
    """
    pass

def getbuffer(obj, offset=None, size=None): # real signature unknown; restored from __doc__
    """
    getbuffer(obj [,offset[, size]])
    
        Create a buffer object from the given object referencing a slice of
        length size starting at offset.
    
        Default is the entire buffer. A read-write buffer is attempted followed
        by a read-only buffer.
    
        Parameters
        ----------
        obj : object
    
        offset : int, optional
    
        size : int, optional
    
        Returns
        -------
        buffer_obj : buffer
    
        Examples
        --------
        >>> buf = np.getbuffer(np.ones(5), 1, 3)
        >>> len(buf)
        3
        >>> buf[0]
        '\x00'
        >>> buf
        <read-write buffer for 0x8af1e70, size 3, offset 1 at 0x8ba4ec0>
    """
    pass

def inner(*args, **kwargs): # real signature unknown
    pass

def int_asbuffer(*args, **kwargs): # real signature unknown
    pass

def is_busday(dates, weekmask='1111100', holidays=None, busdaycal=None, out=None): # real signature unknown; restored from __doc__
    """
    is_busday(dates, weekmask='1111100', holidays=None, busdaycal=None, out=None)
    
        Calculates which of the given dates are valid days, and which are not.
    
        .. versionadded:: 1.7.0
    
        Parameters
        ----------
        dates : array_like of datetime64[D]
            The array of dates to process.
        weekmask : str or array_like of bool, optional
            A seven-element array indicating which of Monday through Sunday are
            valid days. May be specified as a length-seven list or array, like
            [1,1,1,1,1,0,0]; a length-seven string, like '1111100'; or a string
            like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for
            weekdays, optionally separated by white space. Valid abbreviations
            are: Mon Tue Wed Thu Fri Sat Sun
        holidays : array_like of datetime64[D], optional
            An array of dates to consider as invalid dates.  They may be
            specified in any order, and NaT (not-a-time) dates are ignored.
            This list is saved in a normalized form that is suited for
            fast calculations of valid days.
        busdaycal : busdaycalendar, optional
            A `busdaycalendar` object which specifies the valid days. If this
            parameter is provided, neither weekmask nor holidays may be
            provided.
        out : array of bool, optional
            If provided, this array is filled with the result.
    
        Returns
        -------
        out : array of bool
            An array with the same shape as ``dates``, containing True for
            each valid day, and False for each invalid day.
    
        See Also
        --------
        busdaycalendar: An object that specifies a custom set of valid days.
        busday_offset : Applies an offset counted in valid days.
        busday_count : Counts how many valid days are in a half-open date range.
    
        Examples
        --------
        >>> # The weekdays are Friday, Saturday, and Monday
        ... np.is_busday(['2011-07-01', '2011-07-02', '2011-07-18'],
        ...                 holidays=['2011-07-01', '2011-07-04', '2011-07-17'])
        array([False, False,  True], dtype='bool')
    """
    pass

def lexsort(keys, axis=-1): # real signature unknown; restored from __doc__
    """
    lexsort(keys, axis=-1)
    
        Perform an indirect sort using a sequence of keys.
    
        Given multiple sorting keys, which can be interpreted as columns in a
        spreadsheet, lexsort returns an array of integer indices that describes
        the sort order by multiple columns. The last key in the sequence is used
        for the primary sort order, the second-to-last key for the secondary sort
        order, and so on. The keys argument must be a sequence of objects that
        can be converted to arrays of the same shape. If a 2D array is provided
        for the keys argument, it's rows are interpreted as the sorting keys and
        sorting is according to the last row, second last row etc.
    
        Parameters
        ----------
        keys : (k,N) array or tuple containing k (N,)-shaped sequences
            The `k` different "columns" to be sorted.  The last column (or row if
            `keys` is a 2D array) is the primary sort key.
        axis : int, optional
            Axis to be indirectly sorted.  By default, sort over the last axis.
    
        Returns
        -------
        indices : (N,) ndarray of ints
            Array of indices that sort the keys along the specified axis.
    
        See Also
        --------
        argsort : Indirect sort.
        ndarray.sort : In-place sort.
        sort : Return a sorted copy of an array.
    
        Examples
        --------
        Sort names: first by surname, then by name.
    
        >>> surnames =    ('Hertz',    'Galilei', 'Hertz')
        >>> first_names = ('Heinrich', 'Galileo', 'Gustav')
        >>> ind = np.lexsort((first_names, surnames))
        >>> ind
        array([1, 2, 0])
    
        >>> [surnames[i] + ", " + first_names[i] for i in ind]
        ['Galilei, Galileo', 'Hertz, Gustav', 'Hertz, Heinrich']
    
        Sort two columns of numbers:
    
        >>> a = [1,5,1,4,3,4,4] # First column
        >>> b = [9,4,0,4,0,2,1] # Second column
        >>> ind = np.lexsort((b,a)) # Sort by a, then by b
        >>> print ind
        [2 0 4 6 5 3 1]
    
        >>> [(a[i],b[i]) for i in ind]
        [(1, 0), (1, 9), (3, 0), (4, 1), (4, 2), (4, 4), (5, 4)]
    
        Note that sorting is first according to the elements of ``a``.
        Secondary sorting is according to the elements of ``b``.
    
        A normal ``argsort`` would have yielded:
    
        >>> [(a[i],b[i]) for i in np.argsort(a)]
        [(1, 9), (1, 0), (3, 0), (4, 4), (4, 2), (4, 1), (5, 4)]
    
        Structured arrays are sorted lexically by ``argsort``:
    
        >>> x = np.array([(1,9), (5,4), (1,0), (4,4), (3,0), (4,2), (4,1)],
        ...              dtype=np.dtype([('x', int), ('y', int)]))
    
        >>> np.argsort(x) # or np.argsort(x, order=('x', 'y'))
        array([2, 0, 4, 6, 5, 3, 1])
    """
    pass

def min_scalar_type(a): # real signature unknown; restored from __doc__
    """
    min_scalar_type(a)
    
        For scalar ``a``, returns the data type with the smallest size
        and smallest scalar kind which can hold its value.  For non-scalar
        array ``a``, returns the vector's dtype unmodified.
    
        Floating point values are not demoted to integers,
        and complex values are not demoted to floats.
    
        Parameters
        ----------
        a : scalar or array_like
            The value whose minimal data type is to be found.
    
        Returns
        -------
        out : dtype
            The minimal data type.
    
        Notes
        -----
        .. versionadded:: 1.6.0
    
        See Also
        --------
        result_type, promote_types, dtype, can_cast
    
        Examples
        --------
        >>> np.min_scalar_type(10)
        dtype('uint8')
    
        >>> np.min_scalar_type(-260)
        dtype('int16')
    
        >>> np.min_scalar_type(3.1)
        dtype('float16')
    
        >>> np.min_scalar_type(1e50)
        dtype('float64')
    
        >>> np.min_scalar_type(np.arange(4,dtype='f8'))
        dtype('float64')
    """
    pass

def nested_iters(*args, **kwargs): # real signature unknown
    pass

def newbuffer(size): # real signature unknown; restored from __doc__
    """
    newbuffer(size)
    
        Return a new uninitialized buffer object.
    
        Parameters
        ----------
        size : int
            Size in bytes of returned buffer object.
    
        Returns
        -------
        newbuffer : buffer object
            Returned, uninitialized buffer object of `size` bytes.
    """
    pass

def promote_types(type1, type2): # real signature unknown; restored from __doc__
    """
    promote_types(type1, type2)
    
        Returns the data type with the smallest size and smallest scalar
        kind to which both ``type1`` and ``type2`` may be safely cast.
        The returned data type is always in native byte order.
    
        This function is symmetric and associative.
    
        Parameters
        ----------
        type1 : dtype or dtype specifier
            First data type.
        type2 : dtype or dtype specifier
            Second data type.
    
        Returns
        -------
        out : dtype
            The promoted data type.
    
        Notes
        -----
        .. versionadded:: 1.6.0
    
        See Also
        --------
        result_type, dtype, can_cast
    
        Examples
        --------
        >>> np.promote_types('f4', 'f8')
        dtype('float64')
    
        >>> np.promote_types('i8', 'f4')
        dtype('float64')
    
        >>> np.promote_types('>i8', '<c8')
        dtype('complex128')
    
        >>> np.promote_types('i1', 'S8')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        TypeError: invalid type promotion
    """
    pass

def putmask(a, mask, values): # real signature unknown; restored from __doc__
    """
    putmask(a, mask, values)
    
        Changes elements of an array based on conditional and input values.
    
        Sets ``a.flat[n] = values[n]`` for each n where ``mask.flat[n]==True``.
    
        If `values` is not the same size as `a` and `mask` then it will repeat.
        This gives behavior different from ``a[mask] = values``.
    
        .. note:: The `putmask` functionality is also provided by `copyto`, which
                  can be significantly faster and in addition is NA-aware
                  (`preservena` keyword).  Replacing `putmask` with
                  ``np.copyto(a, values, where=mask)`` is recommended.
    
        Parameters
        ----------
        a : array_like
            Target array.
        mask : array_like
            Boolean mask array. It has to be the same shape as `a`.
        values : array_like
            Values to put into `a` where `mask` is True. If `values` is smaller
            than `a` it will be repeated.
    
        See Also
        --------
        place, put, take, copyto
    
        Examples
        --------
        >>> x = np.arange(6).reshape(2, 3)
        >>> np.putmask(x, x>2, x**2)
        >>> x
        array([[ 0,  1,  2],
               [ 9, 16, 25]])
    
        If `values` is smaller than `a` it is repeated:
    
        >>> x = np.arange(5)
        >>> np.putmask(x, x>1, [-33, -44])
        >>> x
        array([  0,   1, -33, -44, -33])
    """
    pass

def result_type(*arrays_and_dtypes): # real signature unknown; restored from __doc__
    """
    result_type(*arrays_and_dtypes)
    
        Returns the type that results from applying the NumPy
        type promotion rules to the arguments.
    
        Type promotion in NumPy works similarly to the rules in languages
        like C++, with some slight differences.  When both scalars and
        arrays are used, the array's type takes precedence and the actual value
        of the scalar is taken into account.
    
        For example, calculating 3*a, where a is an array of 32-bit floats,
        intuitively should result in a 32-bit float output.  If the 3 is a
        32-bit integer, the NumPy rules indicate it can't convert losslessly
        into a 32-bit float, so a 64-bit float should be the result type.
        By examining the value of the constant, '3', we see that it fits in
        an 8-bit integer, which can be cast losslessly into the 32-bit float.
    
        Parameters
        ----------
        arrays_and_dtypes : list of arrays and dtypes
            The operands of some operation whose result type is needed.
    
        Returns
        -------
        out : dtype
            The result type.
    
        See also
        --------
        dtype, promote_types, min_scalar_type, can_cast
    
        Notes
        -----
        .. versionadded:: 1.6.0
    
        The specific algorithm used is as follows.
    
        Categories are determined by first checking which of boolean,
        integer (int/uint), or floating point (float/complex) the maximum
        kind of all the arrays and the scalars are.
    
        If there are only scalars or the maximum category of the scalars
        is higher than the maximum category of the arrays,
        the data types are combined with :func:`promote_types`
        to produce the return value.
    
        Otherwise, `min_scalar_type` is called on each array, and
        the resulting data types are all combined with :func:`promote_types`
        to produce the return value.
    
        The set of int values is not a subset of the uint values for types
        with the same number of bits, something not reflected in
        :func:`min_scalar_type`, but handled as a special case in `result_type`.
    
        Examples
        --------
        >>> np.result_type(3, np.arange(7, dtype='i1'))
        dtype('int8')
    
        >>> np.result_type('i4', 'c8')
        dtype('complex128')
    
        >>> np.result_type(3.0, -2)
        dtype('float64')
    """
    pass

def scalar(dtype, obj): # real signature unknown; restored from __doc__
    """
    scalar(dtype, obj)
    
        Return a new scalar array of the given type initialized with obj.
    
        This function is meant mainly for pickle support. `dtype` must be a
        valid data-type descriptor. If `dtype` corresponds to an object
        descriptor, then `obj` can be any object, otherwise `obj` must be a
        string. If `obj` is not given, it will be interpreted as None for object
        type and as zeros for all other types.
    """
    pass

def set_datetimeparse_function(*args, **kwargs): # real signature unknown
    pass

def set_numeric_ops(**ops): # known case of numpy.core.multiarray.set_numeric_ops
    """
    set_numeric_ops(op1=func1, op2=func2, ...)
    
        Set numerical operators for array objects.
    
        Parameters
        ----------
        op1, op2, ... : callable
            Each ``op = func`` pair describes an operator to be replaced.
            For example, ``add = lambda x, y: np.add(x, y) % 5`` would replace
            addition by modulus 5 addition.
    
        Returns
        -------
        saved_ops : list of callables
            A list of all operators, stored before making replacements.
    
        Notes
        -----
        .. WARNING::
           Use with care!  Incorrect usage may lead to memory errors.
    
        A function replacing an operator cannot make use of that operator.
        For example, when replacing add, you may not use ``+``.  Instead,
        directly call ufuncs.
    
        Examples
        --------
        >>> def add_mod5(x, y):
        ...     return np.add(x, y) % 5
        ...
        >>> old_funcs = np.set_numeric_ops(add=add_mod5)
    
        >>> x = np.arange(12).reshape((3, 4))
        >>> x + x
        array([[0, 2, 4, 1],
               [3, 0, 2, 4],
               [1, 3, 0, 2]])
    
        >>> ignore = np.set_numeric_ops(**old_funcs) # restore operators
    """
    pass

def set_string_function(f, repr=1): # real signature unknown; restored from __doc__
    """
    set_string_function(f, repr=1)
    
        Internal method to set a function to be used when pretty printing arrays.
    """
    pass

def set_typeDict(dict): # real signature unknown; restored from __doc__
    """
    set_typeDict(dict)
    
        Set the internal dictionary that can look up an array type using a
        registered code.
    """
    pass

def test_interrupt(*args, **kwargs): # real signature unknown
    pass

def where(condition, x=None, y=None): # real signature unknown; restored from __doc__
    """
    where(condition, [x, y])
    
        Return elements, either from `x` or `y`, depending on `condition`.
    
        If only `condition` is given, return ``condition.nonzero()``.
    
        Parameters
        ----------
        condition : array_like, bool
            When True, yield `x`, otherwise yield `y`.
        x, y : array_like, optional
            Values from which to choose. `x` and `y` need to have the same
            shape as `condition`.
    
        Returns
        -------
        out : ndarray or tuple of ndarrays
            If both `x` and `y` are specified, the output array contains
            elements of `x` where `condition` is True, and elements from
            `y` elsewhere.
    
            If only `condition` is given, return the tuple
            ``condition.nonzero()``, the indices where `condition` is True.
    
        See Also
        --------
        nonzero, choose
    
        Notes
        -----
        If `x` and `y` are given and input arrays are 1-D, `where` is
        equivalent to::
    
            [xv if c else yv for (c,xv,yv) in zip(condition,x,y)]
    
        Examples
        --------
        >>> np.where([[True, False], [True, True]],
        ...          [[1, 2], [3, 4]],
        ...          [[9, 8], [7, 6]])
        array([[1, 8],
               [3, 4]])
    
        >>> np.where([[0, 1], [1, 0]])
        (array([0, 1]), array([1, 0]))
    
        >>> x = np.arange(9.).reshape(3, 3)
        >>> np.where( x > 5 )
        (array([2, 2, 2]), array([0, 1, 2]))
        >>> x[np.where( x > 3.0 )]               # Note: result is 1D.
        array([ 4.,  5.,  6.,  7.,  8.])
        >>> np.where(x < 5, x, -1)               # Note: broadcasting.
        array([[ 0.,  1.,  2.],
               [ 3.,  4., -1.],
               [-1., -1., -1.]])
    
        Find the indices of elements of `x` that are in `goodvalues`.
    
        >>> goodvalues = [3, 4, 7]
        >>> ix = np.in1d(x.ravel(), goodvalues).reshape(x.shape)
        >>> ix
        array([[False, False, False],
               [ True,  True, False],
               [False,  True, False]], dtype=bool)
        >>> np.where(ix)
        (array([1, 1, 2]), array([0, 1, 1]))
    """
    pass

def zeros(shape, dtype=None, order='C'): # real signature unknown; restored from __doc__
    """
    zeros(shape, dtype=float, order='C')
    
        Return a new array of given shape and type, filled with zeros.
    
        Parameters
        ----------
        shape : int or sequence of ints
            Shape of the new array, e.g., ``(2, 3)`` or ``2``.
        dtype : data-type, optional
            The desired data-type for the array, e.g., `numpy.int8`.  Default is
            `numpy.float64`.
        order : {'C', 'F'}, optional
            Whether to store multidimensional data in C- or Fortran-contiguous
            (row- or column-wise) order in memory.
    
        Returns
        -------
        out : ndarray
            Array of zeros with the given shape, dtype, and order.
    
        See Also
        --------
        zeros_like : Return an array of zeros with shape and type of input.
        ones_like : Return an array of ones with shape and type of input.
        empty_like : Return an empty array with shape and type of input.
        ones : Return a new array setting values to one.
        empty : Return a new uninitialized array.
    
        Examples
        --------
        >>> np.zeros(5)
        array([ 0.,  0.,  0.,  0.,  0.])
    
        >>> np.zeros((5,), dtype=numpy.int)
        array([0, 0, 0, 0, 0])
    
        >>> np.zeros((2, 1))
        array([[ 0.],
               [ 0.]])
    
        >>> s = (2,2)
        >>> np.zeros(s)
        array([[ 0.,  0.],
               [ 0.,  0.]])
    
        >>> np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]) # custom dtype
        array([(0, 0), (0, 0)],
              dtype=[('x', '<i4'), ('y', '<i4')])
    """
    pass

def _fastCopyAndTranspose(a): # real signature unknown; restored from __doc__
    """ _fastCopyAndTranspose(a) """
    pass

def _get_ndarray_c_version(): # real signature unknown; restored from __doc__
    """
    _get_ndarray_c_version()
    
        Return the compile time NDARRAY_VERSION number.
    """
    pass

def _reconstruct(subtype, shape, dtype): # real signature unknown; restored from __doc__
    """
    _reconstruct(subtype, shape, dtype)
    
        Construct an empty array. Used by Pickles.
    """
    pass

def _vec_string(*args, **kwargs): # real signature unknown
    pass

# classes

class broadcast(object):
    """
    Produce an object that mimics broadcasting.
    
        Parameters
        ----------
        in1, in2, ... : array_like
            Input parameters.
    
        Returns
        -------
        b : broadcast object
            Broadcast the input parameters against one another, and
            return an object that encapsulates the result.
            Amongst others, it has ``shape`` and ``nd`` properties, and
            may be used as an iterator.
    
        Examples
        --------
        Manually adding two vectors, using broadcasting:
    
        >>> x = np.array([[1], [2], [3]])
        >>> y = np.array([4, 5, 6])
        >>> b = np.broadcast(x, y)
    
        >>> out = np.empty(b.shape)
        >>> out.flat = [u+v for (u,v) in b]
        >>> out
        array([[ 5.,  6.,  7.],
               [ 6.,  7.,  8.],
               [ 7.,  8.,  9.]])
    
        Compare against built-in broadcasting:
    
        >>> x + y
        array([[5, 6, 7],
               [6, 7, 8],
               [7, 8, 9]])
    """
    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset()
        
            Reset the broadcasted result's iterator(s).
        
            Parameters
            ----------
            None
        
            Returns
            -------
            None
        
            Examples
            --------
            >>> x = np.array([1, 2, 3])
            >>> y = np.array([[4], [5], [6]]
            >>> b = np.broadcast(x, y)
            >>> b.index
            0
            >>> b.next(), b.next(), b.next()
            ((1, 4), (2, 4), (3, 4))
            >>> b.index
            3
            >>> b.reset()
            >>> b.index
            0
        """
        pass

    def __init__(self, x, y): # real signature unknown; restored from __doc__
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """current index in broadcasted result

    Examples
    --------
    >>> x = np.array([[1], [2], [3]])
    >>> y = np.array([4, 5, 6])
    >>> b = np.broadcast(x, y)
    >>> b.index
    0
    >>> b.next(), b.next(), b.next()
    ((1, 4), (1, 5), (1, 6))
    >>> b.index
    3"""

    iters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tuple of iterators along ``self``'s "components."

    Returns a tuple of `numpy.flatiter` objects, one for each "component"
    of ``self``.

    See Also
    --------
    numpy.flatiter

    Examples
    --------
    >>> x = np.array([1, 2, 3])
    >>> y = np.array([[4], [5], [6]])
    >>> b = np.broadcast(x, y)
    >>> row, col = b.iters
    >>> row.next(), col.next()
    (1, 4)"""

    nd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of dimensions of broadcasted result.

    Examples
    --------
    >>> x = np.array([1, 2, 3])
    >>> y = np.array([[4], [5], [6]])
    >>> b = np.broadcast(x, y)
    >>> b.nd
    2"""

    numiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of iterators possessed by the broadcasted result.

    Examples
    --------
    >>> x = np.array([1, 2, 3])
    >>> y = np.array([[4], [5], [6]])
    >>> b = np.broadcast(x, y)
    >>> b.numiter
    2"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shape of broadcasted result.

    Examples
    --------
    >>> x = np.array([1, 2, 3])
    >>> y = np.array([[4], [5], [6]])
    >>> b = np.broadcast(x, y)
    >>> b.shape
    (3, 3)"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total size of broadcasted result.

    Examples
    --------
    >>> x = np.array([1, 2, 3])
    >>> y = np.array([[4], [5], [6]])
    >>> b = np.broadcast(x, y)
    >>> b.size
    9"""



class busdaycalendar(object):
    """
    busdaycalendar(weekmask='1111100', holidays=None)
    
        A business day calendar object that efficiently stores information
        defining valid days for the busday family of functions.
    
        The default valid days are Monday through Friday ("business days").
        A busdaycalendar object can be specified with any set of weekly
        valid days, plus an optional "holiday" dates that always will be invalid.
    
        Once a busdaycalendar object is created, the weekmask and holidays
        cannot be modified.
    
        .. versionadded:: 1.7.0
    
        Parameters
        ----------
        weekmask : str or array_like of bool, optional
            A seven-element array indicating which of Monday through Sunday are
            valid days. May be specified as a length-seven list or array, like
            [1,1,1,1,1,0,0]; a length-seven string, like '1111100'; or a string
            like "Mon Tue Wed Thu Fri", made up of 3-character abbreviations for
            weekdays, optionally separated by white space. Valid abbreviations
            are: Mon Tue Wed Thu Fri Sat Sun
        holidays : array_like of datetime64[D], optional
            An array of dates to consider as invalid dates, no matter which
            weekday they fall upon.  Holiday dates may be specified in any
            order, and NaT (not-a-time) dates are ignored.  This list is
            saved in a normalized form that is suited for fast calculations
            of valid days.
    
        Returns
        -------
        out : busdaycalendar
            A business day calendar object containing the specified
            weekmask and holidays values.
    
        See Also
        --------
        is_busday : Returns a boolean array indicating valid days.
        busday_offset : Applies an offset counted in valid days.
        busday_count : Counts how many valid days are in a half-open date range.
    
        Attributes
        ----------
        Note: once a busdaycalendar object is created, you cannot modify the
        weekmask or holidays.  The attributes return copies of internal data.
        weekmask : (copy) seven-element array of bool
        holidays : (copy) sorted array of datetime64[D]
    
        Examples
        --------
        >>> # Some important days in July
        ... bdd = np.busdaycalendar(
        ...             holidays=['2011-07-01', '2011-07-04', '2011-07-17'])
        >>> # Default is Monday to Friday weekdays
        ... bdd.weekmask
        array([ True,  True,  True,  True,  True, False, False], dtype='bool')
        >>> # Any holidays already on the weekend are removed
        ... bdd.holidays
        array(['2011-07-01', '2011-07-04'], dtype='datetime64[D]')
    """
    def __init__(self, weekmask='1111100', holidays=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    holidays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A copy of the holiday array indicating additional invalid days."""

    weekmask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A copy of the seven-element boolean mask indicating valid days."""



class dtype(object):
    """
    dtype(obj, align=False, copy=False)
    
        Create a data type object.
    
        A numpy array is homogeneous, and contains elements described by a
        dtype object. A dtype object can be constructed from different
        combinations of fundamental numeric types.
    
        Parameters
        ----------
        obj
            Object to be converted to a data type object.
        align : bool, optional
            Add padding to the fields to match what a C compiler would output
            for a similar C-struct. Can be ``True`` only if `obj` is a dictionary
            or a comma-separated string. If a struct dtype is being created,
            this also sets a sticky alignment flag ``isalignedstruct``.
        copy : bool, optional
            Make a new copy of the data-type object. If ``False``, the result
            may just be a reference to a built-in data-type object.
    
        See also
        --------
        result_type
    
        Examples
        --------
        Using array-scalar type:
    
        >>> np.dtype(np.int16)
        dtype('int16')
    
        Record, one field name 'f1', containing int16:
    
        >>> np.dtype([('f1', np.int16)])
        dtype([('f1', '<i2')])
    
        Record, one field named 'f1', in itself containing a record with one field:
    
        >>> np.dtype([('f1', [('f1', np.int16)])])
        dtype([('f1', [('f1', '<i2')])])
    
        Record, two fields: the first field contains an unsigned int, the
        second an int32:
    
        >>> np.dtype([('f1', np.uint), ('f2', np.int32)])
        dtype([('f1', '<u4'), ('f2', '<i4')])
    
        Using array-protocol type strings:
    
        >>> np.dtype([('a','f8'),('b','S10')])
        dtype([('a', '<f8'), ('b', '|S10')])
    
        Using comma-separated field formats.  The shape is (2,3):
    
        >>> np.dtype("i4, (2,3)f8")
        dtype([('f0', '<i4'), ('f1', '<f8', (2, 3))])
    
        Using tuples.  ``int`` is a fixed type, 3 the field's shape.  ``void``
        is a flexible type, here of size 10:
    
        >>> np.dtype([('hello',(np.int,3)),('world',np.void,10)])
        dtype([('hello', '<i4', 3), ('world', '|V10')])
    
        Subdivide ``int16`` into 2 ``int8``'s, called x and y.  0 and 1 are
        the offsets in bytes:
    
        >>> np.dtype((np.int16, {'x':(np.int8,0), 'y':(np.int8,1)}))
        dtype(('<i2', [('x', '|i1'), ('y', '|i1')]))
    
        Using dictionaries.  Two fields named 'gender' and 'age':
    
        >>> np.dtype({'names':['gender','age'], 'formats':['S1',np.uint8]})
        dtype([('gender', '|S1'), ('age', '|u1')])
    
        Offsets in bytes, here 0 and 25:
    
        >>> np.dtype({'surname':('S25',0),'age':(np.uint8,25)})
        dtype([('surname', '|S25'), ('age', '|u1')])
    """
    def newbyteorder(self, new_order='S'): # real signature unknown; restored from __doc__
        """
        newbyteorder(new_order='S')
        
            Return a new dtype with a different byte order.
        
            Changes are also made in all fields and sub-arrays of the data type.
        
            Parameters
            ----------
            new_order : string, optional
                Byte order to force; a value from the byte order
                specifications below.  The default value ('S') results in
                swapping the current byte order.
                `new_order` codes can be any of::
        
                 * 'S' - swap dtype from current to opposite endian
                 * {'<', 'L'} - little endian
                 * {'>', 'B'} - big endian
                 * {'=', 'N'} - native order
                 * {'|', 'I'} - ignore (no change to byte order)
        
                The code does a case-insensitive check on the first letter of
                `new_order` for these alternatives.  For example, any of '>'
                or 'B' or 'b' or 'brian' are valid to specify big-endian.
        
            Returns
            -------
            new_dtype : dtype
                New dtype object with the given change to the byte order.
        
            Notes
            -----
            Changes are also made in all fields and sub-arrays of the data type.
        
            Examples
            --------
            >>> import sys
            >>> sys_is_le = sys.byteorder == 'little'
            >>> native_code = sys_is_le and '<' or '>'
            >>> swapped_code = sys_is_le and '>' or '<'
            >>> native_dt = np.dtype(native_code+'i2')
            >>> swapped_dt = np.dtype(swapped_code+'i2')
            >>> native_dt.newbyteorder('S') == swapped_dt
            True
            >>> native_dt.newbyteorder() == swapped_dt
            True
            >>> native_dt == swapped_dt.newbyteorder('S')
            True
            >>> native_dt == swapped_dt.newbyteorder('=')
            True
            >>> native_dt == swapped_dt.newbyteorder('N')
            True
            >>> native_dt == native_dt.newbyteorder('|')
            True
            >>> np.dtype('<i2') == native_dt.newbyteorder('<')
            True
            >>> np.dtype('<i2') == native_dt.newbyteorder('L')
            True
            >>> np.dtype('>i2') == native_dt.newbyteorder('>')
            True
            >>> np.dtype('>i2') == native_dt.newbyteorder('B')
            True
        """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
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

    def __init__(self, obj, align=False, copy=False): # real signature unknown; restored from __doc__
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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The required alignment (bytes) of this data-type according to the compiler.

    More information is available in the C-API section of the manual."""

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    byteorder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A character indicating the byte-order of this data-type object.

    One of:

    ===  ==============
    '='  native
    '<'  little-endian
    '>'  big-endian
    '|'  not applicable
    ===  ==============

    All built-in data-type objects have byteorder either '=' or '|'.

    Examples
    --------

    >>> dt = np.dtype('i2')
    >>> dt.byteorder
    '='
    >>> # endian is not relevant for 8 bit numbers
    >>> np.dtype('i1').byteorder
    '|'
    >>> # or ASCII strings
    >>> np.dtype('S2').byteorder
    '|'
    >>> # Even if specific code is given, and it is native
    >>> # '=' is the byteorder
    >>> import sys
    >>> sys_is_le = sys.byteorder == 'little'
    >>> native_code = sys_is_le and '<' or '>'
    >>> swapped_code = sys_is_le and '>' or '<'
    >>> dt = np.dtype(native_code + 'i2')
    >>> dt.byteorder
    '='
    >>> # Swapped code shows up as itself
    >>> dt = np.dtype(swapped_code + 'i2')
    >>> dt.byteorder == swapped_code
    True"""

    char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unique character code for each of the 21 different built-in types."""

    descr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Array-interface compliant full description of the data-type.

    The format is that required by the 'descr' key in the
    `__array_interface__` attribute."""

    fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary of named fields defined for this data type, or ``None``.

    The dictionary is indexed by keys that are the names of the fields.
    Each entry in the dictionary is a tuple fully describing the field::

      (dtype, offset[, title])

    If present, the optional title can be any object (if it is a string
    or unicode then it will also be a key in the fields dictionary,
    otherwise it's meta-data). Notice also that the first two elements
    of the tuple can be passed directly as arguments to the ``ndarray.getfield``
    and ``ndarray.setfield`` methods.

    See Also
    --------
    ndarray.getfield, ndarray.setfield

    Examples
    --------

    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
    >>> print dt.fields
    {'grades': (dtype(('float64',(2,))), 16), 'name': (dtype('|S16'), 0)}"""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bit-flags describing how this data type is to be interpreted.

    Bit-masks are in `numpy.core.multiarray` as the constants
    `ITEM_HASOBJECT`, `LIST_PICKLE`, `ITEM_IS_POINTER`, `NEEDS_INIT`,
    `NEEDS_PYAPI`, `USE_GETITEM`, `USE_SETITEM`. A full explanation
    of these flags is in C-API documentation; they are largely useful
    for user-defined data-types."""

    hasobject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean indicating whether this dtype contains any reference-counted
    objects in any fields or sub-dtypes.

    Recall that what is actually in the ndarray memory representing
    the Python object is the memory address of that object (a pointer).
    Special handling may be required, and this attribute is useful for
    distinguishing data types that may contain arbitrary Python objects
    and data-types that won't."""

    isalignedstruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean indicating whether the dtype is a struct which maintains
    field alignment. This flag is sticky, so when combining multiple
    structs together, it is preserved and produces new dtypes which
    are also aligned."""

    isbuiltin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Integer indicating how this dtype relates to the built-in dtypes.

    Read-only.

    =  ========================================================================
    0  if this is a structured array type, with fields
    1  if this is a dtype compiled into numpy (such as ints, floats etc)
    2  if the dtype is for a user-defined numpy type
       A user-defined type uses the numpy C-API machinery to extend
       numpy to handle a new array type. See
       :ref:`user.user-defined-data-types` in the Numpy manual.
    =  ========================================================================

    Examples
    --------
    >>> dt = np.dtype('i2')
    >>> dt.isbuiltin
    1
    >>> dt = np.dtype('f8')
    >>> dt.isbuiltin
    1
    >>> dt = np.dtype([('field1', 'f8')])
    >>> dt.isbuiltin
    0"""

    isnative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Boolean indicating whether the byte order of this dtype is native
    to the platform."""

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The element size of this data-type object.

    For 18 of the 21 types this number is fixed by the data-type.
    For the flexible data-types, this number can be anything."""

    kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A character code (one of 'biufcSUV') identifying the general kind of data."""

    metadata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A bit-width name for this data-type.

    Un-sized flexible data-type objects do not have this attribute."""

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ordered list of field names, or ``None`` if there are no fields.

    The names are ordered according to increasing byte offset. This can be
    used, for example, to walk through all of the named fields in offset order.

    Examples
    --------

    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
    >>> dt.names
    ('name', 'grades')"""

    num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A unique number for each of the 21 different built-in types.

    These are roughly ordered from least-to-most precision."""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Shape tuple of the sub-array if this data type describes a sub-array,
    and ``()`` otherwise."""

    str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The array-protocol typestring of this data-type object."""

    subdtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tuple ``(item_dtype, shape)`` if this `dtype` describes a sub-array, and
    None otherwise.

    The *shape* is the fixed shape of the sub-array described by this
    data type, and *item_dtype* the data type of the array.

    If a field whose dtype object has this attribute is retrieved,
    then the extra dimensions implied by *shape* are tacked on to
    the end of the retrieved array."""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type object used to instantiate a scalar of this data-type."""



class flagsobj(object):
    # no doc
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    aligned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    behaved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    carray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    c_contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    farray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fnc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    forc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fortran = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_contiguous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    owndata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    updateifcopy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writeable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class flatiter(object):
    """
    Flat iterator object to iterate over arrays.
    
        A `flatiter` iterator is returned by ``x.flat`` for any array `x`.
        It allows iterating over the array as if it were a 1-D array,
        either in a for-loop or by calling its `next` method.
    
        Iteration is done in C-contiguous style, with the last index varying the
        fastest. The iterator can also be indexed using basic slicing or
        advanced indexing.
    
        See Also
        --------
        ndarray.flat : Return a flat iterator over an array.
        ndarray.flatten : Returns a flattened copy of an array.
    
        Notes
        -----
        A `flatiter` iterator can not be constructed directly from Python code
        by calling the `flatiter` constructor.
    
        Examples
        --------
        >>> x = np.arange(6).reshape(2, 3)
        >>> fl = x.flat
        >>> type(fl)
        <type 'numpy.flatiter'>
        >>> for item in fl:
        ...     print item
        ...
        0
        1
        2
        3
        4
        5
    
        >>> fl[2:4]
        array([2, 3])
    """
    def copy(self): # real signature unknown; restored from __doc__
        """
        copy()
        
            Get a copy of the iterator as a 1-D array.
        
            Examples
            --------
            >>> x = np.arange(6).reshape(2, 3)
            >>> x
            array([[0, 1, 2],
                   [3, 4, 5]])
            >>> fl = x.flat
            >>> fl.copy()
            array([0, 1, 2, 3, 4, 5])
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def __array__(self, type=None): # real signature unknown; restored from __doc__
        """ __array__(type=None) Get array from iterator """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
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

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A reference to the array that is iterated over.

    Examples
    --------
    >>> x = np.arange(5)
    >>> fl = x.flat
    >>> fl.base is x
    True"""

    coords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An N-dimensional tuple of current coordinates.

    Examples
    --------
    >>> x = np.arange(6).reshape(2, 3)
    >>> fl = x.flat
    >>> fl.coords
    (0, 0)
    >>> fl.next()
    0
    >>> fl.coords
    (0, 1)"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current flat index into the array.

    Examples
    --------
    >>> x = np.arange(6).reshape(2, 3)
    >>> fl = x.flat
    >>> fl.index
    0
    >>> fl.next()
    0
    >>> fl.index
    1"""



class ndarray(object):
    """
    ndarray(shape, dtype=float, buffer=None, offset=0,
                strides=None, order=None)
    
        An array object represents a multidimensional, homogeneous array
        of fixed-size items.  An associated data-type object describes the
        format of each element in the array (its byte-order, how many bytes it
        occupies in memory, whether it is an integer, a floating point number,
        or something else, etc.)
    
        Arrays should be constructed using `array`, `zeros` or `empty` (refer
        to the See Also section below).  The parameters given here refer to
        a low-level method (`ndarray(...)`) for instantiating an array.
    
        For more information, refer to the `numpy` module and examine the
        the methods and attributes of an array.
    
        Parameters
        ----------
        (for the __new__ method; see Notes below)
    
        shape : tuple of ints
            Shape of created array.
        dtype : data-type, optional
            Any object that can be interpreted as a numpy data type.
        buffer : object exposing buffer interface, optional
            Used to fill the array with data.
        offset : int, optional
            Offset of array data in buffer.
        strides : tuple of ints, optional
            Strides of data in memory.
        order : {'C', 'F'}, optional
            Row-major or column-major order.
    
        Attributes
        ----------
        T : ndarray
            Transpose of the array.
        data : buffer
            The array's elements, in memory.
        dtype : dtype object
            Describes the format of the elements in the array.
        flags : dict
            Dictionary containing information related to memory use, e.g.,
            'C_CONTIGUOUS', 'OWNDATA', 'WRITEABLE', etc.
        flat : numpy.flatiter object
            Flattened version of the array as an iterator.  The iterator
            allows assignments, e.g., ``x.flat = 3`` (See `ndarray.flat` for
            assignment examples; TODO).
        imag : ndarray
            Imaginary part of the array.
        real : ndarray
            Real part of the array.
        size : int
            Number of elements in the array.
        itemsize : int
            The memory use of each array element in bytes.
        nbytes : int
            The total number of bytes required to store the array data,
            i.e., ``itemsize * size``.
        ndim : int
            The array's number of dimensions.
        shape : tuple of ints
            Shape of the array.
        strides : tuple of ints
            The step-size required to move from one element to the next in
            memory. For example, a contiguous ``(3, 4)`` array of type
            ``int16`` in C-order has strides ``(8, 2)``.  This implies that
            to move from element to element in memory requires jumps of 2 bytes.
            To move from row-to-row, one needs to jump 8 bytes at a time
            (``2 * 4``).
        ctypes : ctypes object
            Class containing properties of the array needed for interaction
            with ctypes.
        base : ndarray
            If the array is a view into another array, that array is its `base`
            (unless that array is also a view).  The `base` array is where the
            array data is actually stored.
    
        See Also
        --------
        array : Construct an array.
        zeros : Create an array, each element of which is zero.
        empty : Create an array, but leave its allocated memory unchanged (i.e.,
                it contains "garbage").
        dtype : Create a data-type.
    
        Notes
        -----
        There are two modes of creating an array using ``__new__``:
    
        1. If `buffer` is None, then only `shape`, `dtype`, and `order`
           are used.
        2. If `buffer` is an object exposing the buffer interface, then
           all keywords are interpreted.
    
        No ``__init__`` method is needed because the array is fully initialized
        after the ``__new__`` method.
    
        Examples
        --------
        These examples illustrate the low-level `ndarray` constructor.  Refer
        to the `See Also` section above for easier ways of constructing an
        ndarray.
    
        First mode, `buffer` is None:
    
        >>> np.ndarray(shape=(2,2), dtype=float, order='F')
        array([[ -1.13698227e+002,   4.25087011e-303],
               [  2.88528414e-306,   3.27025015e-309]])         #random
    
        Second mode:
    
        >>> np.ndarray((2,), buffer=np.array([1,2,3]),
        ...            offset=np.int_().itemsize,
        ...            dtype=int) # offset = 1*itemsize, i.e. skip first element
        array([2, 3])
    """
    def all(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.all(axis=None, out=None)
        
            Returns True if all elements evaluate to True.
        
            Refer to `numpy.all` for full documentation.
        
            See Also
            --------
            numpy.all : equivalent function
        """
        pass

    def any(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.any(axis=None, out=None)
        
            Returns True if any of the elements of `a` evaluate to True.
        
            Refer to `numpy.any` for full documentation.
        
            See Also
            --------
            numpy.any : equivalent function
        """
        pass

    def argmax(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.argmax(axis=None, out=None)
        
            Return indices of the maximum values along the given axis.
        
            Refer to `numpy.argmax` for full documentation.
        
            See Also
            --------
            numpy.argmax : equivalent function
        """
        pass

    def argmin(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.argmin(axis=None, out=None)
        
            Return indices of the minimum values along the given axis of `a`.
        
            Refer to `numpy.argmin` for detailed documentation.
        
            See Also
            --------
            numpy.argmin : equivalent function
        """
        pass

    def argsort(self, axis=-1, kind='quicksort', order=None): # real signature unknown; restored from __doc__
        """
        a.argsort(axis=-1, kind='quicksort', order=None)
        
            Returns the indices that would sort this array.
        
            Refer to `numpy.argsort` for full documentation.
        
            See Also
            --------
            numpy.argsort : equivalent function
        """
        pass

    def astype(self, dtype, order='K', casting='unsafe', subok=True, copy=True): # real signature unknown; restored from __doc__
        """
        a.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)
        
            Copy of the array, cast to a specified type.
        
            Parameters
            ----------
            dtype : str or dtype
                Typecode or data-type to which the array is cast.
            order : {'C', 'F', 'A', or 'K'}, optional
                Controls the memory layout order of the result.
                'C' means C order, 'F' means Fortran order, 'A'
                means 'F' order if all the arrays are Fortran contiguous,
                'C' order otherwise, and 'K' means as close to the
                order the array elements appear in memory as possible.
                Default is 'K'.
            casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
                Controls what kind of data casting may occur. Defaults to 'unsafe'
                for backwards compatibility.
        
                  * 'no' means the data types should not be cast at all.
                  * 'equiv' means only byte-order changes are allowed.
                  * 'safe' means only casts which can preserve values are allowed.
                  * 'same_kind' means only safe casts or casts within a kind,
                    like float64 to float32, are allowed.
                  * 'unsafe' means any data conversions may be done.
            subok : bool, optional
                If True, then sub-classes will be passed-through (default), otherwise
                the returned array will be forced to be a base-class array.
            copy : bool, optional
                By default, astype always returns a newly allocated array. If this
                is set to false, and the `dtype`, `order`, and `subok`
                requirements are satisfied, the input array is returned instead
                of a copy.
        
            Raises
            ------
            ComplexWarning :
                When casting from complex to float or int. To avoid this,
                one should use ``a.real.astype(t)``.
        
            Examples
            --------
            >>> x = np.array([1, 2, 2.5])
            >>> x
            array([ 1. ,  2. ,  2.5])
        
            >>> x.astype(int)
            array([1, 2, 2])
        """
        pass

    def byteswap(self, inplace): # real signature unknown; restored from __doc__
        """
        a.byteswap(inplace)
        
            Swap the bytes of the array elements
        
            Toggle between low-endian and big-endian data representation by
            returning a byteswapped array, optionally swapped in-place.
        
            Parameters
            ----------
            inplace: bool, optional
                If ``True``, swap bytes in-place, default is ``False``.
        
            Returns
            -------
            out: ndarray
                The byteswapped array. If `inplace` is ``True``, this is
                a view to self.
        
            Examples
            --------
            >>> A = np.array([1, 256, 8755], dtype=np.int16)
            >>> map(hex, A)
            ['0x1', '0x100', '0x2233']
            >>> A.byteswap(True)
            array([  256,     1, 13090], dtype=int16)
            >>> map(hex, A)
            ['0x100', '0x1', '0x3322']
        
            Arrays of strings are not swapped
        
            >>> A = np.array(['ceg', 'fac'])
            >>> A.byteswap()
            array(['ceg', 'fac'],
                  dtype='|S3')
        """
        pass

    def choose(self, choices, out=None, mode='raise'): # real signature unknown; restored from __doc__
        """
        a.choose(choices, out=None, mode='raise')
        
            Use an index array to construct a new array from a set of choices.
        
            Refer to `numpy.choose` for full documentation.
        
            See Also
            --------
            numpy.choose : equivalent function
        """
        pass

    def clip(self, a_min, a_max, out=None): # real signature unknown; restored from __doc__
        """
        a.clip(a_min, a_max, out=None)
        
            Return an array whose values are limited to ``[a_min, a_max]``.
        
            Refer to `numpy.clip` for full documentation.
        
            See Also
            --------
            numpy.clip : equivalent function
        """
        pass

    def compress(self, condition, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.compress(condition, axis=None, out=None)
        
            Return selected slices of this array along given axis.
        
            Refer to `numpy.compress` for full documentation.
        
            See Also
            --------
            numpy.compress : equivalent function
        """
        pass

    def conj(self): # real signature unknown; restored from __doc__
        """
        a.conj()
        
            Complex-conjugate all elements.
        
            Refer to `numpy.conjugate` for full documentation.
        
            See Also
            --------
            numpy.conjugate : equivalent function
        """
        pass

    def conjugate(self): # real signature unknown; restored from __doc__
        """
        a.conjugate()
        
            Return the complex conjugate, element-wise.
        
            Refer to `numpy.conjugate` for full documentation.
        
            See Also
            --------
            numpy.conjugate : equivalent function
        """
        pass

    def copy(self, order='C'): # real signature unknown; restored from __doc__
        """
        a.copy(order='C')
        
            Return a copy of the array.
        
            Parameters
            ----------
            order : {'C', 'F', 'A', 'K'}, optional
                Controls the memory layout of the copy. 'C' means C-order,
                'F' means F-order, 'A' means 'F' if `a` is Fortran contiguous,
                'C' otherwise. 'K' means match the layout of `a` as closely
                as possible. (Note that this function and :func:numpy.copy are very
                similar, but have different default values for their order=
                arguments.)
        
            See also
            --------
            numpy.copy
            numpy.copyto
        
            Examples
            --------
            >>> x = np.array([[1,2,3],[4,5,6]], order='F')
        
            >>> y = x.copy()
        
            >>> x.fill(0)
        
            >>> x
            array([[0, 0, 0],
                   [0, 0, 0]])
        
            >>> y
            array([[1, 2, 3],
                   [4, 5, 6]])
        
            >>> y.flags['C_CONTIGUOUS']
            True
        """
        pass

    def cumprod(self, axis=None, dtype=None, out=None): # real signature unknown; restored from __doc__
        """
        a.cumprod(axis=None, dtype=None, out=None)
        
            Return the cumulative product of the elements along the given axis.
        
            Refer to `numpy.cumprod` for full documentation.
        
            See Also
            --------
            numpy.cumprod : equivalent function
        """
        pass

    def cumsum(self, axis=None, dtype=None, out=None): # real signature unknown; restored from __doc__
        """
        a.cumsum(axis=None, dtype=None, out=None)
        
            Return the cumulative sum of the elements along the given axis.
        
            Refer to `numpy.cumsum` for full documentation.
        
            See Also
            --------
            numpy.cumsum : equivalent function
        """
        pass

    def diagonal(self, offset=0, axis1=0, axis2=1): # real signature unknown; restored from __doc__
        """
        a.diagonal(offset=0, axis1=0, axis2=1)
        
            Return specified diagonals.
        
            Refer to :func:`numpy.diagonal` for full documentation.
        
            See Also
            --------
            numpy.diagonal : equivalent function
        """
        pass

    def dot(self, b, out=None): # real signature unknown; restored from __doc__
        """
        a.dot(b, out=None)
        
            Dot product of two arrays.
        
            Refer to `numpy.dot` for full documentation.
        
            See Also
            --------
            numpy.dot : equivalent function
        
            Examples
            --------
            >>> a = np.eye(2)
            >>> b = np.ones((2, 2)) * 2
            >>> a.dot(b)
            array([[ 2.,  2.],
                   [ 2.,  2.]])
        
            This array method can be conveniently chained:
        
            >>> a.dot(b).dot(b)
            array([[ 8.,  8.],
                   [ 8.,  8.]])
        """
        pass

    def dump(self, file): # real signature unknown; restored from __doc__
        """
        a.dump(file)
        
            Dump a pickle of the array to the specified file.
            The array can be read back with pickle.load or numpy.load.
        
            Parameters
            ----------
            file : str
                A string naming the dump file.
        """
        pass

    def dumps(self): # real signature unknown; restored from __doc__
        """
        a.dumps()
        
            Returns the pickle of the array as a string.
            pickle.loads or numpy.loads will convert the string back to an array.
        
            Parameters
            ----------
            None
        """
        pass

    def fill(self, value): # real signature unknown; restored from __doc__
        """
        a.fill(value)
        
            Fill the array with a scalar value.
        
            Parameters
            ----------
            value : scalar
                All elements of `a` will be assigned this value.
        
            Examples
            --------
            >>> a = np.array([1, 2])
            >>> a.fill(0)
            >>> a
            array([0, 0])
            >>> a = np.empty(2)
            >>> a.fill(1)
            >>> a
            array([ 1.,  1.])
        """
        pass

    def flatten(self, order='C'): # real signature unknown; restored from __doc__
        """
        a.flatten(order='C')
        
            Return a copy of the array collapsed into one dimension.
        
            Parameters
            ----------
            order : {'C', 'F', 'A'}, optional
                Whether to flatten in C (row-major), Fortran (column-major) order,
                or preserve the C/Fortran ordering from `a`.
                The default is 'C'.
        
            Returns
            -------
            y : ndarray
                A copy of the input array, flattened to one dimension.
        
            See Also
            --------
            ravel : Return a flattened array.
            flat : A 1-D flat iterator over the array.
        
            Examples
            --------
            >>> a = np.array([[1,2], [3,4]])
            >>> a.flatten()
            array([1, 2, 3, 4])
            >>> a.flatten('F')
            array([1, 3, 2, 4])
        """
        pass

    def getfield(self, dtype, offset=0): # real signature unknown; restored from __doc__
        """
        a.getfield(dtype, offset=0)
        
            Returns a field of the given array as a certain type.
        
            A field is a view of the array data with a given data-type. The values in
            the view are determined by the given type and the offset into the current
            array in bytes. The offset needs to be such that the view dtype fits in the
            array dtype; for example an array of dtype complex128 has 16-byte elements.
            If taking a view with a 32-bit integer (4 bytes), the offset needs to be
            between 0 and 12 bytes.
        
            Parameters
            ----------
            dtype : str or dtype
                The data type of the view. The dtype size of the view can not be larger
                than that of the array itself.
            offset : int
                Number of bytes to skip before beginning the element view.
        
            Examples
            --------
            >>> x = np.diag([1.+1.j]*2)
            >>> x[1, 1] = 2 + 4.j
            >>> x
            array([[ 1.+1.j,  0.+0.j],
                   [ 0.+0.j,  2.+4.j]])
            >>> x.getfield(np.float64)
            array([[ 1.,  0.],
                   [ 0.,  2.]])
        
            By choosing an offset of 8 bytes we can select the complex part of the
            array for our view:
        
            >>> x.getfield(np.float64, offset=8)
            array([[ 1.,  0.],
               [ 0.,  4.]])
        """
        pass

    def item(self, *args): # real signature unknown; restored from __doc__
        """
        a.item(*args)
        
            Copy an element of an array to a standard Python scalar and return it.
        
            Parameters
            ----------
            \*args : Arguments (variable number and type)
        
                * none: in this case, the method only works for arrays
                  with one element (`a.size == 1`), which element is
                  copied into a standard Python scalar object and returned.
        
                * int_type: this argument is interpreted as a flat index into
                  the array, specifying which element to copy and return.
        
                * tuple of int_types: functions as does a single int_type argument,
                  except that the argument is interpreted as an nd-index into the
                  array.
        
            Returns
            -------
            z : Standard Python scalar object
                A copy of the specified element of the array as a suitable
                Python scalar
        
            Notes
            -----
            When the data type of `a` is longdouble or clongdouble, item() returns
            a scalar array object because there is no available Python scalar that
            would not lose information. Void arrays return a buffer object for item(),
            unless fields are defined, in which case a tuple is returned.
        
            `item` is very similar to a[args], except, instead of an array scalar,
            a standard Python scalar is returned. This can be useful for speeding up
            access to elements of the array and doing arithmetic on elements of the
            array using Python's optimized math.
        
            Examples
            --------
            >>> x = np.random.randint(9, size=(3, 3))
            >>> x
            array([[3, 1, 7],
                   [2, 8, 3],
                   [8, 5, 3]])
            >>> x.item(3)
            2
            >>> x.item(7)
            5
            >>> x.item((0, 1))
            1
            >>> x.item((2, 2))
            3
        """
        pass

    def itemset(self, *args): # real signature unknown; restored from __doc__
        """
        a.itemset(*args)
        
            Insert scalar into an array (scalar is cast to array's dtype, if possible)
        
            There must be at least 1 argument, and define the last argument
            as *item*.  Then, ``a.itemset(*args)`` is equivalent to but faster
            than ``a[args] = item``.  The item should be a scalar value and `args`
            must select a single item in the array `a`.
        
            Parameters
            ----------
            \*args : Arguments
                If one argument: a scalar, only used in case `a` is of size 1.
                If two arguments: the last argument is the value to be set
                and must be a scalar, the first argument specifies a single array
                element location. It is either an int or a tuple.
        
            Notes
            -----
            Compared to indexing syntax, `itemset` provides some speed increase
            for placing a scalar into a particular location in an `ndarray`,
            if you must do this.  However, generally this is discouraged:
            among other problems, it complicates the appearance of the code.
            Also, when using `itemset` (and `item`) inside a loop, be sure
            to assign the methods to a local variable to avoid the attribute
            look-up at each loop iteration.
        
            Examples
            --------
            >>> x = np.random.randint(9, size=(3, 3))
            >>> x
            array([[3, 1, 7],
                   [2, 8, 3],
                   [8, 5, 3]])
            >>> x.itemset(4, 0)
            >>> x.itemset((2, 2), 9)
            >>> x
            array([[3, 1, 7],
                   [2, 0, 3],
                   [8, 5, 9]])
        """
        pass

    def max(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.max(axis=None, out=None)
        
            Return the maximum along a given axis.
        
            Refer to `numpy.amax` for full documentation.
        
            See Also
            --------
            numpy.amax : equivalent function
        """
        pass

    def mean(self, axis=None, dtype=None, out=None): # real signature unknown; restored from __doc__
        """
        a.mean(axis=None, dtype=None, out=None)
        
            Returns the average of the array elements along given axis.
        
            Refer to `numpy.mean` for full documentation.
        
            See Also
            --------
            numpy.mean : equivalent function
        """
        pass

    def min(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.min(axis=None, out=None)
        
            Return the minimum along a given axis.
        
            Refer to `numpy.amin` for full documentation.
        
            See Also
            --------
            numpy.amin : equivalent function
        """
        pass

    def newbyteorder(self, new_order='S'): # real signature unknown; restored from __doc__
        """
        arr.newbyteorder(new_order='S')
        
            Return the array with the same data viewed with a different byte order.
        
            Equivalent to::
        
                arr.view(arr.dtype.newbytorder(new_order))
        
            Changes are also made in all fields and sub-arrays of the array data
            type.
        
        
        
            Parameters
            ----------
            new_order : string, optional
                Byte order to force; a value from the byte order specifications
                above. `new_order` codes can be any of::
        
                 * 'S' - swap dtype from current to opposite endian
                 * {'<', 'L'} - little endian
                 * {'>', 'B'} - big endian
                 * {'=', 'N'} - native order
                 * {'|', 'I'} - ignore (no change to byte order)
        
                The default value ('S') results in swapping the current
                byte order. The code does a case-insensitive check on the first
                letter of `new_order` for the alternatives above.  For example,
                any of 'B' or 'b' or 'biggish' are valid to specify big-endian.
        
        
            Returns
            -------
            new_arr : array
                New array object with the dtype reflecting given change to the
                byte order.
        """
        pass

    def nonzero(self): # real signature unknown; restored from __doc__
        """
        a.nonzero()
        
            Return the indices of the elements that are non-zero.
        
            Refer to `numpy.nonzero` for full documentation.
        
            See Also
            --------
            numpy.nonzero : equivalent function
        """
        pass

    def prod(self, axis=None, dtype=None, out=None): # real signature unknown; restored from __doc__
        """
        a.prod(axis=None, dtype=None, out=None)
        
            Return the product of the array elements over the given axis
        
            Refer to `numpy.prod` for full documentation.
        
            See Also
            --------
            numpy.prod : equivalent function
        """
        pass

    def ptp(self, axis=None, out=None): # real signature unknown; restored from __doc__
        """
        a.ptp(axis=None, out=None)
        
            Peak to peak (maximum - minimum) value along a given axis.
        
            Refer to `numpy.ptp` for full documentation.
        
            See Also
            --------
            numpy.ptp : equivalent function
        """
        pass

    def put(self, indices, values, mode='raise'): # real signature unknown; restored from __doc__
        """
        a.put(indices, values, mode='raise')
        
            Set ``a.flat[n] = values[n]`` for all `n` in indices.
        
            Refer to `numpy.put` for full documentation.
        
            See Also
            --------
            numpy.put : equivalent function
        """
        pass

    def ravel(self, order=None): # real signature unknown; restored from __doc__
        """
        a.ravel([order])
        
            Return a flattened array.
        
            Refer to `numpy.ravel` for full documentation.
        
            See Also
            --------
            numpy.ravel : equivalent function
        
            ndarray.flat : a flat iterator on the array.
        """
        pass

    def repeat(self, repeats, axis=None): # real signature unknown; restored from __doc__
        """
        a.repeat(repeats, axis=None)
        
            Repeat elements of an array.
        
            Refer to `numpy.repeat` for full documentation.
        
            See Also
            --------
            numpy.repeat : equivalent function
        """
        pass

    def reshape(self, shape, order='C'): # real signature unknown; restored from __doc__
        """
        a.reshape(shape, order='C')
        
            Returns an array containing the same data with a new shape.
        
            Refer to `numpy.reshape` for full documentation.
        
            See Also
            --------
            numpy.reshape : equivalent function
        """
        pass

    def resize(self, new_shape, refcheck=True): # real signature unknown; restored from __doc__
        """
        a.resize(new_shape, refcheck=True)
        
            Change shape and size of array in-place.
        
            Parameters
            ----------
            new_shape : tuple of ints, or `n` ints
                Shape of resized array.
            refcheck : bool, optional
                If False, reference count will not be checked. Default is True.
        
            Returns
            -------
            None
        
            Raises
            ------
            ValueError
                If `a` does not own its own data or references or views to it exist,
                and the data memory must be changed.
        
            SystemError
                If the `order` keyword argument is specified. This behaviour is a
                bug in NumPy.
        
            See Also
            --------
            resize : Return a new array with the specified shape.
        
            Notes
            -----
            This reallocates space for the data area if necessary.
        
            Only contiguous arrays (data elements consecutive in memory) can be
            resized.
        
            The purpose of the reference count check is to make sure you
            do not use this array as a buffer for another Python object and then
            reallocate the memory. However, reference counts can increase in
            other ways so if you are sure that you have not shared the memory
            for this array with another Python object, then you may safely set
            `refcheck` to False.
        
            Examples
            --------
            Shrinking an array: array is flattened (in the order that the data are
            stored in memory), resized, and reshaped:
        
            >>> a = np.array([[0, 1], [2, 3]], order='C')
            >>> a.resize((2, 1))
            >>> a
            array([[0],
                   [1]])
        
            >>> a = np.array([[0, 1], [2, 3]], order='F')
            >>> a.resize((2, 1))
            >>> a
            array([[0],
                   [2]])
        
            Enlarging an array: as above, but missing entries are filled with zeros:
        
            >>> b = np.array([[0, 1], [2, 3]])
            >>> b.resize(2, 3) # new_shape parameter doesn't have to be a tuple
            >>> b
            array([[0, 1, 2],
                   [3, 0, 0]])
        
            Referencing an array prevents resizing...
        
            >>> c = a
            >>> a.resize((1, 1))
            Traceback (most recent call last):
            ...
            ValueError: cannot resize an array that has been referenced ...
        
            Unless `refcheck` is False:
        
            >>> a.resize((1, 1), refcheck=False)
            >>> a
            array([[0]])
            >>> c
            array([[0]])
        """
        pass

    def round(self, decimals=0, out=None): # real signature unknown; restored from __doc__
        """
        a.round(decimals=0, out=None)
        
            Return `a` with each element rounded to the given number of decimals.
        
            Refer to `numpy.around` for full documentation.
        
            See Also
            --------
            numpy.around : equivalent function
        """
        pass

    def searchsorted(self, v, side='left', sorter=None): # real signature unknown; restored from __doc__
        """
        a.searchsorted(v, side='left', sorter=None)
        
            Find indices where elements of v should be inserted in a to maintain order.
        
            For full documentation, see `numpy.searchsorted`
        
            See Also
            --------
            numpy.searchsorted : equivalent function
        """
        pass

    def setfield(self, val, dtype, offset=0): # real signature unknown; restored from __doc__
        """
        a.setfield(val, dtype, offset=0)
        
            Put a value into a specified place in a field defined by a data-type.
        
            Place `val` into `a`'s field defined by `dtype` and beginning `offset`
            bytes into the field.
        
            Parameters
            ----------
            val : object
                Value to be placed in field.
            dtype : dtype object
                Data-type of the field in which to place `val`.
            offset : int, optional
                The number of bytes into the field at which to place `val`.
        
            Returns
            -------
            None
        
            See Also
            --------
            getfield
        
            Examples
            --------
            >>> x = np.eye(3)
            >>> x.getfield(np.float64)
            array([[ 1.,  0.,  0.],
                   [ 0.,  1.,  0.],
                   [ 0.,  0.,  1.]])
            >>> x.setfield(3, np.int32)
            >>> x.getfield(np.int32)
            array([[3, 3, 3],
                   [3, 3, 3],
                   [3, 3, 3]])
            >>> x
            array([[  1.00000000e+000,   1.48219694e-323,   1.48219694e-323],
                   [  1.48219694e-323,   1.00000000e+000,   1.48219694e-323],
                   [  1.48219694e-323,   1.48219694e-323,   1.00000000e+000]])
            >>> x.setfield(np.eye(3), np.int32)
            >>> x
            array([[ 1.,  0.,  0.],
                   [ 0.,  1.,  0.],
                   [ 0.,  0.,  1.]])
        """
        pass

    def setflags(self, write=None, align=None, uic=None): # real signature unknown; restored from __doc__
        """
        a.setflags(write=None, align=None, uic=None)
        
            Set array flags WRITEABLE, ALIGNED, and UPDATEIFCOPY, respectively.
        
            These Boolean-valued flags affect how numpy interprets the memory
            area used by `a` (see Notes below). The ALIGNED flag can only
            be set to True if the data is actually aligned according to the type.
            The UPDATEIFCOPY flag can never be set to True. The flag WRITEABLE
            can only be set to True if the array owns its own memory, or the
            ultimate owner of the memory exposes a writeable buffer interface,
            or is a string. (The exception for string is made so that unpickling
            can be done without copying memory.)
        
            Parameters
            ----------
            write : bool, optional
                Describes whether or not `a` can be written to.
            align : bool, optional
                Describes whether or not `a` is aligned properly for its type.
            uic : bool, optional
                Describes whether or not `a` is a copy of another "base" array.
        
            Notes
            -----
            Array flags provide information about how the memory area used
            for the array is to be interpreted. There are 6 Boolean flags
            in use, only three of which can be changed by the user:
            UPDATEIFCOPY, WRITEABLE, and ALIGNED.
        
            WRITEABLE (W) the data area can be written to;
        
            ALIGNED (A) the data and strides are aligned appropriately for the hardware
            (as determined by the compiler);
        
            UPDATEIFCOPY (U) this array is a copy of some other array (referenced
            by .base). When this array is deallocated, the base array will be
            updated with the contents of this array.
        
            All flags can be accessed using their first (upper case) letter as well
            as the full name.
        
            Examples
            --------
            >>> y
            array([[3, 1, 7],
                   [2, 0, 0],
                   [8, 5, 9]])
            >>> y.flags
              C_CONTIGUOUS : True
              F_CONTIGUOUS : False
              OWNDATA : True
              WRITEABLE : True
              ALIGNED : True
              UPDATEIFCOPY : False
            >>> y.setflags(write=0, align=0)
            >>> y.flags
              C_CONTIGUOUS : True
              F_CONTIGUOUS : False
              OWNDATA : True
              WRITEABLE : False
              ALIGNED : False
              UPDATEIFCOPY : False
            >>> y.setflags(uic=1)
            Traceback (most recent call last):
              File "<stdin>", line 1, in <module>
            ValueError: cannot set UPDATEIFCOPY flag to True
        """
        pass

    def sort(self, axis=-1, kind='quicksort', order=None): # real signature unknown; restored from __doc__
        """
        a.sort(axis=-1, kind='quicksort', order=None)
        
            Sort an array, in-place.
        
            Parameters
            ----------
            axis : int, optional
                Axis along which to sort. Default is -1, which means sort along the
                last axis.
            kind : {'quicksort', 'mergesort', 'heapsort'}, optional
                Sorting algorithm. Default is 'quicksort'.
            order : list, optional
                When `a` is an array with fields defined, this argument specifies
                which fields to compare first, second, etc.  Not all fields need be
                specified.
        
            See Also
            --------
            numpy.sort : Return a sorted copy of an array.
            argsort : Indirect sort.
            lexsort : Indirect stable sort on multiple keys.
            searchsorted : Find elements in sorted array.
        
            Notes
            -----
            See ``sort`` for notes on the different sorting algorithms.
        
            Examples
            --------
            >>> a = np.array([[1,4], [3,1]])
            >>> a.sort(axis=1)
            >>> a
            array([[1, 4],
                   [1, 3]])
            >>> a.sort(axis=0)
            >>> a
            array([[1, 3],
                   [1, 4]])
        
            Use the `order` keyword to specify a field to use when sorting a
            structured array:
        
            >>> a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
            >>> a.sort(order='y')
            >>> a
            array([('c', 1), ('a', 2)],
                  dtype=[('x', '|S1'), ('y', '<i4')])
        """
        pass

    def squeeze(self, axis=None): # real signature unknown; restored from __doc__
        """
        a.squeeze(axis=None)
        
            Remove single-dimensional entries from the shape of `a`.
        
            Refer to `numpy.squeeze` for full documentation.
        
            See Also
            --------
            numpy.squeeze : equivalent function
        """
        pass

    def std(self, axis=None, dtype=None, out=None, ddof=0): # real signature unknown; restored from __doc__
        """
        a.std(axis=None, dtype=None, out=None, ddof=0)
        
            Returns the standard deviation of the array elements along given axis.
        
            Refer to `numpy.std` for full documentation.
        
            See Also
            --------
            numpy.std : equivalent function
        """
        pass

    def sum(self, axis=None, dtype=None, out=None): # real signature unknown; restored from __doc__
        """
        a.sum(axis=None, dtype=None, out=None)
        
            Return the sum of the array elements over the given axis.
        
            Refer to `numpy.sum` for full documentation.
        
            See Also
            --------
            numpy.sum : equivalent function
        """
        pass

    def swapaxes(self, axis1, axis2): # real signature unknown; restored from __doc__
        """
        a.swapaxes(axis1, axis2)
        
            Return a view of the array with `axis1` and `axis2` interchanged.
        
            Refer to `numpy.swapaxes` for full documentation.
        
            See Also
            --------
            numpy.swapaxes : equivalent function
        """
        pass

    def take(self, indices, axis=None, out=None, mode='raise'): # real signature unknown; restored from __doc__
        """
        a.take(indices, axis=None, out=None, mode='raise')
        
            Return an array formed from the elements of `a` at the given indices.
        
            Refer to `numpy.take` for full documentation.
        
            See Also
            --------
            numpy.take : equivalent function
        """
        pass

    def tofile(self, fid, sep="", format="%s"): # real signature unknown; restored from __doc__
        """
        a.tofile(fid, sep="", format="%s")
        
            Write array to a file as text or binary (default).
        
            Data is always written in 'C' order, independent of the order of `a`.
            The data produced by this method can be recovered using the function
            fromfile().
        
            Parameters
            ----------
            fid : file or str
                An open file object, or a string containing a filename.
            sep : str
                Separator between array items for text output.
                If "" (empty), a binary file is written, equivalent to
                ``file.write(a.tostring())``.
            format : str
                Format string for text file output.
                Each entry in the array is formatted to text by first converting
                it to the closest Python type, and then using "format" % item.
        
            Notes
            -----
            This is a convenience function for quick storage of array data.
            Information on endianness and precision is lost, so this method is not a
            good choice for files intended to archive data or transport data between
            machines with different endianness. Some of these problems can be overcome
            by outputting the data as text files, at the expense of speed and file
            size.
        """
        pass

    def tolist(self): # real signature unknown; restored from __doc__
        """
        a.tolist()
        
            Return the array as a (possibly nested) list.
        
            Return a copy of the array data as a (nested) Python list.
            Data items are converted to the nearest compatible Python type.
        
            Parameters
            ----------
            none
        
            Returns
            -------
            y : list
                The possibly nested list of array elements.
        
            Notes
            -----
            The array may be recreated, ``a = np.array(a.tolist())``.
        
            Examples
            --------
            >>> a = np.array([1, 2])
            >>> a.tolist()
            [1, 2]
            >>> a = np.array([[1, 2], [3, 4]])
            >>> list(a)
            [array([1, 2]), array([3, 4])]
            >>> a.tolist()
            [[1, 2], [3, 4]]
        """
        pass

    def tostring(self, order='C'): # real signature unknown; restored from __doc__
        """
        a.tostring(order='C')
        
            Construct a Python string containing the raw data bytes in the array.
        
            Constructs a Python string showing a copy of the raw contents of
            data memory. The string can be produced in either 'C' or 'Fortran',
            or 'Any' order (the default is 'C'-order). 'Any' order means C-order
            unless the F_CONTIGUOUS flag in the array is set, in which case it
            means 'Fortran' order.
        
            Parameters
            ----------
            order : {'C', 'F', None}, optional
                Order of the data for multidimensional arrays:
                C, Fortran, or the same as for the original array.
        
            Returns
            -------
            s : str
                A Python string exhibiting a copy of `a`'s raw data.
        
            Examples
            --------
            >>> x = np.array([[0, 1], [2, 3]])
            >>> x.tostring()
            '\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
            >>> x.tostring('C') == x.tostring()
            True
            >>> x.tostring('F')
            '\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00'
        """
        pass

    def trace(self, offset=0, axis1=0, axis2=1, dtype=None, out=None): # real signature unknown; restored from __doc__
        """
        a.trace(offset=0, axis1=0, axis2=1, dtype=None, out=None)
        
            Return the sum along diagonals of the array.
        
            Refer to `numpy.trace` for full documentation.
        
            See Also
            --------
            numpy.trace : equivalent function
        """
        pass

    def transpose(self, *axes): # real signature unknown; restored from __doc__
        """
        a.transpose(*axes)
        
            Returns a view of the array with axes transposed.
        
            For a 1-D array, this has no effect. (To change between column and
            row vectors, first cast the 1-D array into a matrix object.)
            For a 2-D array, this is the usual matrix transpose.
            For an n-D array, if axes are given, their order indicates how the
            axes are permuted (see Examples). If axes are not provided and
            ``a.shape = (i[0], i[1], ... i[n-2], i[n-1])``, then
            ``a.transpose().shape = (i[n-1], i[n-2], ... i[1], i[0])``.
        
            Parameters
            ----------
            axes : None, tuple of ints, or `n` ints
        
             * None or no argument: reverses the order of the axes.
        
             * tuple of ints: `i` in the `j`-th place in the tuple means `a`'s
               `i`-th axis becomes `a.transpose()`'s `j`-th axis.
        
             * `n` ints: same as an n-tuple of the same ints (this form is
               intended simply as a "convenience" alternative to the tuple form)
        
            Returns
            -------
            out : ndarray
                View of `a`, with axes suitably permuted.
        
            See Also
            --------
            ndarray.T : Array property returning the array transposed.
        
            Examples
            --------
            >>> a = np.array([[1, 2], [3, 4]])
            >>> a
            array([[1, 2],
                   [3, 4]])
            >>> a.transpose()
            array([[1, 3],
                   [2, 4]])
            >>> a.transpose((1, 0))
            array([[1, 3],
                   [2, 4]])
            >>> a.transpose(1, 0)
            array([[1, 3],
                   [2, 4]])
        """
        pass

    def var(self, axis=None, dtype=None, out=None, ddof=0): # real signature unknown; restored from __doc__
        """
        a.var(axis=None, dtype=None, out=None, ddof=0)
        
            Returns the variance of the array elements, along given axis.
        
            Refer to `numpy.var` for full documentation.
        
            See Also
            --------
            numpy.var : equivalent function
        """
        pass

    def view(self, dtype=None, type=None): # real signature unknown; restored from __doc__
        """
        a.view(dtype=None, type=None)
        
            New view of array with the same data.
        
            Parameters
            ----------
            dtype : data-type, optional
                Data-type descriptor of the returned view, e.g., float32 or int16.
                The default, None, results in the view having the same data-type
                as `a`.
            type : Python type, optional
                Type of the returned view, e.g., ndarray or matrix.  Again, the
                default None results in type preservation.
        
            Notes
            -----
            ``a.view()`` is used two different ways:
        
            ``a.view(some_dtype)`` or ``a.view(dtype=some_dtype)`` constructs a view
            of the array's memory with a different data-type.  This can cause a
            reinterpretation of the bytes of memory.
        
            ``a.view(ndarray_subclass)`` or ``a.view(type=ndarray_subclass)`` just
            returns an instance of `ndarray_subclass` that looks at the same array
            (same shape, dtype, etc.)  This does not cause a reinterpretation of the
            memory.
        
        
            Examples
            --------
            >>> x = np.array([(1, 2)], dtype=[('a', np.int8), ('b', np.int8)])
        
            Viewing array data using a different type and dtype:
        
            >>> y = x.view(dtype=np.int16, type=np.matrix)
            >>> y
            matrix([[513]], dtype=int16)
            >>> print type(y)
            <class 'numpy.matrixlib.defmatrix.matrix'>
        
            Creating a view on a structured array so it can be used in calculations
        
            >>> x = np.array([(1, 2),(3,4)], dtype=[('a', np.int8), ('b', np.int8)])
            >>> xv = x.view(dtype=np.int8).reshape(-1,2)
            >>> xv
            array([[1, 2],
                   [3, 4]], dtype=int8)
            >>> xv.mean(0)
            array([ 2.,  3.])
        
            Making changes to the view changes the underlying array
        
            >>> xv[0,1] = 20
            >>> print x
            [(1, 20) (3, 4)]
        
            Using a view to convert an array to a record array:
        
            >>> z = x.view(np.recarray)
            >>> z.a
            array([1], dtype=int8)
        
            Views share data:
        
            >>> x[0] = (9, 10)
            >>> z[0]
            (9, 10)
        """
        pass

    def __abs__(self): # real signature unknown; restored from __doc__
        """ x.__abs__() <==> abs(x) """
        pass

    def __add__(self, y): # real signature unknown; restored from __doc__
        """ x.__add__(y) <==> x+y """
        pass

    def __and__(self, y): # real signature unknown; restored from __doc__
        """ x.__and__(y) <==> x&y """
        pass

    def __array_prepare__(self, obj): # real signature unknown; restored from __doc__
        """ a.__array_prepare__(obj) -> Object of same type as ndarray object obj. """
        pass

    def __array_wrap__(self, obj): # real signature unknown; restored from __doc__
        """ a.__array_wrap__(obj) -> Object of same type as ndarray object a. """
        pass

    def __array__(self, dtype=None): # known case of numpy.core.multiarray.ndarray.__array__
        """
        a.__array__(|dtype) -> reference if type unchanged, copy otherwise.
        
            Returns either a new reference to self if dtype is not given or a new array
            of provided data type if dtype is different from the current dtype of the
            array.
        """
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __copy__(self, order=None): # real signature unknown; restored from __doc__
        """
        a.__copy__([order])
        
            Return a copy of the array.
        
            Parameters
            ----------
            order : {'C', 'F', 'A'}, optional
                If order is 'C' (False) then the result is contiguous (default).
                If order is 'Fortran' (True) then the result has fortran order.
                If order is 'Any' (None) then the result has fortran order
                only if the array already is in fortran order.
        """
        pass

    def __deepcopy__(self): # real signature unknown; restored from __doc__
        """
        a.__deepcopy__() -> Deep copy of array.
        
            Used if copy.deepcopy is called on an array.
        """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __delslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__delslice__(i, j) <==> del x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __divmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__divmod__(y) <==> divmod(x, y) """
        pass

    def __div__(self, y): # real signature unknown; restored from __doc__
        """ x.__div__(y) <==> x/y """
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __float__(self): # real signature unknown; restored from __doc__
        """ x.__float__() <==> float(x) """
        pass

    def __floordiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__floordiv__(y) <==> x//y """
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

    def __hex__(self): # real signature unknown; restored from __doc__
        """ x.__hex__() <==> hex(x) """
        pass

    def __iadd__(self, y): # real signature unknown; restored from __doc__
        """ x.__iadd__(y) <==> x+=y """
        pass

    def __iand__(self, y): # real signature unknown; restored from __doc__
        """ x.__iand__(y) <==> x&=y """
        pass

    def __idiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__idiv__(y) <==> x/=y """
        pass

    def __ifloordiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__ifloordiv__(y) <==> x//y """
        pass

    def __ilshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__ilshift__(y) <==> x<<=y """
        pass

    def __imod__(self, y): # real signature unknown; restored from __doc__
        """ x.__imod__(y) <==> x%=y """
        pass

    def __imul__(self, y): # real signature unknown; restored from __doc__
        """ x.__imul__(y) <==> x*=y """
        pass

    def __index__(self): # real signature unknown; restored from __doc__
        """ x[y:z] <==> x[y.__index__():z.__index__()] """
        pass

    def __init__(self, shape, dtype=None, buffer=None, offset=0, strides=None, order=None): # real signature unknown; restored from __doc__
        pass

    def __int__(self): # real signature unknown; restored from __doc__
        """ x.__int__() <==> int(x) """
        pass

    def __invert__(self): # real signature unknown; restored from __doc__
        """ x.__invert__() <==> ~x """
        pass

    def __ior__(self, y): # real signature unknown; restored from __doc__
        """ x.__ior__(y) <==> x|=y """
        pass

    def __ipow__(self, y): # real signature unknown; restored from __doc__
        """ x.__ipow__(y) <==> x**=y """
        pass

    def __irshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__irshift__(y) <==> x>>=y """
        pass

    def __isub__(self, y): # real signature unknown; restored from __doc__
        """ x.__isub__(y) <==> x-=y """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __itruediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__itruediv__(y) <==> x/y """
        pass

    def __ixor__(self, y): # real signature unknown; restored from __doc__
        """ x.__ixor__(y) <==> x^=y """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __long__(self): # real signature unknown; restored from __doc__
        """ x.__long__() <==> long(x) """
        pass

    def __lshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__lshift__(y) <==> x<<y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __mod__(self, y): # real signature unknown; restored from __doc__
        """ x.__mod__(y) <==> x%y """
        pass

    def __mul__(self, y): # real signature unknown; restored from __doc__
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self): # real signature unknown; restored from __doc__
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __oct__(self): # real signature unknown; restored from __doc__
        """ x.__oct__() <==> oct(x) """
        pass

    def __or__(self, y): # real signature unknown; restored from __doc__
        """ x.__or__(y) <==> x|y """
        pass

    def __pos__(self): # real signature unknown; restored from __doc__
        """ x.__pos__() <==> +x """
        pass

    def __pow__(self, y, z=None): # real signature unknown; restored from __doc__
        """ x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        pass

    def __radd__(self, y): # real signature unknown; restored from __doc__
        """ x.__radd__(y) <==> y+x """
        pass

    def __rand__(self, y): # real signature unknown; restored from __doc__
        """ x.__rand__(y) <==> y&x """
        pass

    def __rdivmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdivmod__(y) <==> divmod(y, x) """
        pass

    def __rdiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rdiv__(y) <==> y/x """
        pass

    def __reduce__(self): # real signature unknown; restored from __doc__
        """
        a.__reduce__()
        
            For pickling.
        """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __rfloordiv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rfloordiv__(y) <==> y//x """
        pass

    def __rlshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rlshift__(y) <==> y<<x """
        pass

    def __rmod__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmod__(y) <==> y%x """
        pass

    def __rmul__(self, y): # real signature unknown; restored from __doc__
        """ x.__rmul__(y) <==> y*x """
        pass

    def __ror__(self, y): # real signature unknown; restored from __doc__
        """ x.__ror__(y) <==> y|x """
        pass

    def __rpow__(self, x, z=None): # real signature unknown; restored from __doc__
        """ y.__rpow__(x[, z]) <==> pow(x, y[, z]) """
        pass

    def __rrshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rrshift__(y) <==> y>>x """
        pass

    def __rshift__(self, y): # real signature unknown; restored from __doc__
        """ x.__rshift__(y) <==> x>>y """
        pass

    def __rsub__(self, y): # real signature unknown; restored from __doc__
        """ x.__rsub__(y) <==> y-x """
        pass

    def __rtruediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__rtruediv__(y) <==> y/x """
        pass

    def __rxor__(self, y): # real signature unknown; restored from __doc__
        """ x.__rxor__(y) <==> y^x """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __setslice__(self, i, j, y): # real signature unknown; restored from __doc__
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
                   
                   Use  of negative indices is not supported.
        """
        pass

    def __setstate__(self, version, shape, dtype, isfortran, rawdata): # real signature unknown; restored from __doc__
        """
        a.__setstate__(version, shape, dtype, isfortran, rawdata)
        
            For unpickling.
        
            Parameters
            ----------
            version : int
                optional pickle version. If omitted defaults to 0.
            shape : tuple
            dtype : data-type
            isFortran : bool
            rawdata : string or list
                a binary string with the data (or a list if 'a' is an object array)
        """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    def __sub__(self, y): # real signature unknown; restored from __doc__
        """ x.__sub__(y) <==> x-y """
        pass

    def __truediv__(self, y): # real signature unknown; restored from __doc__
        """ x.__truediv__(y) <==> x/y """
        pass

    def __xor__(self, y): # real signature unknown; restored from __doc__
        """ x.__xor__(y) <==> x^y """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Base object if memory is from some other object.

    Examples
    --------
    The base of an array that owns its memory is None:

    >>> x = np.array([1,2,3,4])
    >>> x.base is None
    True

    Slicing creates a view, whose memory is shared with x:

    >>> y = x[2:]
    >>> y.base is x
    True"""

    ctypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An object to simplify the interaction of the array with the ctypes
    module.

    This attribute creates an object that makes it easier to use arrays
    when calling shared libraries with the ctypes module. The returned
    object has, among others, data, shape, and strides attributes (see
    Notes below) which themselves return ctypes objects that can be used
    as arguments to a shared library.

    Parameters
    ----------
    None

    Returns
    -------
    c : Python object
        Possessing attributes data, shape, strides, etc.

    See Also
    --------
    numpy.ctypeslib

    Notes
    -----
    Below are the public attributes of this object which were documented
    in "Guide to NumPy" (we have omitted undocumented public attributes,
    as well as documented private attributes):

    * data: A pointer to the memory area of the array as a Python integer.
      This memory area may contain data that is not aligned, or not in correct
      byte-order. The memory area may not even be writeable. The array
      flags and data-type of this array should be respected when passing this
      attribute to arbitrary C-code to avoid trouble that can include Python
      crashing. User Beware! The value of this attribute is exactly the same
      as self._array_interface_['data'][0].

    * shape (c_intp*self.ndim): A ctypes array of length self.ndim where
      the basetype is the C-integer corresponding to dtype('p') on this
      platform. This base-type could be c_int, c_long, or c_longlong
      depending on the platform. The c_intp type is defined accordingly in
      numpy.ctypeslib. The ctypes array contains the shape of the underlying
      array.

    * strides (c_intp*self.ndim): A ctypes array of length self.ndim where
      the basetype is the same as for the shape attribute. This ctypes array
      contains the strides information from the underlying array. This strides
      information is important for showing how many bytes must be jumped to
      get to the next element in the array.

    * data_as(obj): Return the data pointer cast to a particular c-types object.
      For example, calling self._as_parameter_ is equivalent to
      self.data_as(ctypes.c_void_p). Perhaps you want to use the data as a
      pointer to a ctypes array of floating-point data:
      self.data_as(ctypes.POINTER(ctypes.c_double)).

    * shape_as(obj): Return the shape tuple as an array of some other c-types
      type. For example: self.shape_as(ctypes.c_short).

    * strides_as(obj): Return the strides tuple as an array of some other
      c-types type. For example: self.strides_as(ctypes.c_longlong).

    Be careful using the ctypes attribute - especially on temporary
    arrays or arrays constructed on the fly. For example, calling
    ``(a+b).ctypes.data_as(ctypes.c_void_p)`` returns a pointer to memory
    that is invalid because the array created as (a+b) is deallocated
    before the next Python statement. You can avoid this problem using
    either ``c=a+b`` or ``ct=(a+b).ctypes``. In the latter case, ct will
    hold a reference to the array until ct is deleted or re-assigned.

    If the ctypes module is not available, then the ctypes attribute
    of array objects still returns something useful, but ctypes objects
    are not returned and errors may be raised instead. In particular,
    the object will still have the as parameter attribute which will
    return an integer equal to the data attribute.

    Examples
    --------
    >>> import ctypes
    >>> x
    array([[0, 1],
           [2, 3]])
    >>> x.ctypes.data
    30439712
    >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_long))
    <ctypes.LP_c_long object at 0x01F01300>
    >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_long)).contents
    c_long(0)
    >>> x.ctypes.data_as(ctypes.POINTER(ctypes.c_longlong)).contents
    c_longlong(4294967296L)
    >>> x.ctypes.shape
    <numpy.core._internal.c_long_Array_2 object at 0x01FFD580>
    >>> x.ctypes.shape_as(ctypes.c_long)
    <numpy.core._internal.c_long_Array_2 object at 0x01FCE620>
    >>> x.ctypes.strides
    <numpy.core._internal.c_long_Array_2 object at 0x01FCE620>
    >>> x.ctypes.strides_as(ctypes.c_longlong)
    <numpy.core._internal.c_longlong_Array_2 object at 0x01F01300>"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Python buffer object pointing to the start of the array's data."""

    dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Data-type of the array's elements.

    Parameters
    ----------
    None

    Returns
    -------
    d : numpy dtype object

    See Also
    --------
    numpy.dtype

    Examples
    --------
    >>> x
    array([[0, 1],
           [2, 3]])
    >>> x.dtype
    dtype('int32')
    >>> type(x.dtype)
    <type 'numpy.dtype'>"""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about the memory layout of the array.

    Attributes
    ----------
    C_CONTIGUOUS (C)
        The data is in a single, C-style contiguous segment.
    F_CONTIGUOUS (F)
        The data is in a single, Fortran-style contiguous segment.
    OWNDATA (O)
        The array owns the memory it uses or borrows it from another object.
    WRITEABLE (W)
        The data area can be written to.  Setting this to False locks
        the data, making it read-only.  A view (slice, etc.) inherits WRITEABLE
        from its base array at creation time, but a view of a writeable
        array may be subsequently locked while the base array remains writeable.
        (The opposite is not true, in that a view of a locked array may not
        be made writeable.  However, currently, locking a base object does not
        lock any views that already reference it, so under that circumstance it
        is possible to alter the contents of a locked array via a previously
        created writeable view onto it.)  Attempting to change a non-writeable
        array raises a RuntimeError exception.
    ALIGNED (A)
        The data and strides are aligned appropriately for the hardware.
    UPDATEIFCOPY (U)
        This array is a copy of some other array. When this array is
        deallocated, the base array will be updated with the contents of
        this array.

    FNC
        F_CONTIGUOUS and not C_CONTIGUOUS.
    FORC
        F_CONTIGUOUS or C_CONTIGUOUS (one-segment test).
    BEHAVED (B)
        ALIGNED and WRITEABLE.
    CARRAY (CA)
        BEHAVED and C_CONTIGUOUS.
    FARRAY (FA)
        BEHAVED and F_CONTIGUOUS and not C_CONTIGUOUS.

    Notes
    -----
    The `flags` object can be accessed dictionary-like (as in ``a.flags['WRITEABLE']``),
    or by using lowercased attribute names (as in ``a.flags.writeable``). Short flag
    names are only supported in dictionary access.

    Only the UPDATEIFCOPY, WRITEABLE, and ALIGNED flags can be changed by
    the user, via direct assignment to the attribute or dictionary entry,
    or by calling `ndarray.setflags`.

    The array flags cannot be set arbitrarily:

    - UPDATEIFCOPY can only be set ``False``.
    - ALIGNED can only be set ``True`` if the data is truly aligned.
    - WRITEABLE can only be set ``True`` if the array owns its own memory
      or the ultimate owner of the memory exposes a writeable buffer
      interface or is a string."""

    flat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A 1-D iterator over the array.

    This is a `numpy.flatiter` instance, which acts similarly to, but is not
    a subclass of, Python's built-in iterator object.

    See Also
    --------
    flatten : Return a copy of the array collapsed into one dimension.

    flatiter

    Examples
    --------
    >>> x = np.arange(1, 7).reshape(2, 3)
    >>> x
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> x.flat[3]
    4
    >>> x.T
    array([[1, 4],
           [2, 5],
           [3, 6]])
    >>> x.T.flat[3]
    5
    >>> type(x.flat)
    <type 'numpy.flatiter'>

    An assignment example:

    >>> x.flat = 3; x
    array([[3, 3, 3],
           [3, 3, 3]])
    >>> x.flat[[1,4]] = 1; x
    array([[3, 1, 3],
           [3, 1, 3]])"""

    imag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The imaginary part of the array.

    Examples
    --------
    >>> x = np.sqrt([1+0j, 0+1j])
    >>> x.imag
    array([ 0.        ,  0.70710678])
    >>> x.imag.dtype
    dtype('float64')"""

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Length of one array element in bytes.

    Examples
    --------
    >>> x = np.array([1,2,3], dtype=np.float64)
    >>> x.itemsize
    8
    >>> x = np.array([1,2,3], dtype=np.complex128)
    >>> x.itemsize
    16"""

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total bytes consumed by the elements of the array.

    Notes
    -----
    Does not include memory consumed by non-element attributes of the
    array object.

    Examples
    --------
    >>> x = np.zeros((3,5,2), dtype=np.complex128)
    >>> x.nbytes
    480
    >>> np.prod(x.shape) * x.itemsize
    480"""

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of array dimensions.

    Examples
    --------
    >>> x = np.array([1, 2, 3])
    >>> x.ndim
    1
    >>> y = np.zeros((2, 3, 4))
    >>> y.ndim
    3"""

    real = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The real part of the array.

    Examples
    --------
    >>> x = np.sqrt([1+0j, 0+1j])
    >>> x.real
    array([ 1.        ,  0.70710678])
    >>> x.real.dtype
    dtype('float64')

    See Also
    --------
    numpy.real : equivalent function"""

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tuple of array dimensions.

    Notes
    -----
    May be used to "reshape" the array, as long as this would not
    require a change in the total number of elements

    Examples
    --------
    >>> x = np.array([1, 2, 3, 4])
    >>> x.shape
    (4,)
    >>> y = np.zeros((2, 3, 4))
    >>> y.shape
    (2, 3, 4)
    >>> y.shape = (3, 8)
    >>> y
    array([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])
    >>> y.shape = (3, 6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: total size of new array must be unchanged"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of elements in the array.

    Equivalent to ``np.prod(a.shape)``, i.e., the product of the array's
    dimensions.

    Examples
    --------
    >>> x = np.zeros((3, 5, 2), dtype=np.complex128)
    >>> x.size
    30
    >>> np.prod(x.shape)
    30"""

    strides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tuple of bytes to step in each dimension when traversing an array.

    The byte offset of element ``(i[0], i[1], ..., i[n])`` in an array `a`
    is::

        offset = sum(np.array(i) * a.strides)

    A more detailed explanation of strides can be found in the
    "ndarray.rst" file in the NumPy reference guide.

    Notes
    -----
    Imagine an array of 32-bit integers (each 4 bytes)::

      x = np.array([[0, 1, 2, 3, 4],
                    [5, 6, 7, 8, 9]], dtype=np.int32)

    This array is stored in memory as 40 bytes, one after the other
    (known as a contiguous block of memory).  The strides of an array tell
    us how many bytes we have to skip in memory to move to the next position
    along a certain axis.  For example, we have to skip 4 bytes (1 value) to
    move to the next column, but 20 bytes (5 values) to get to the same
    position in the next row.  As such, the strides for the array `x` will be
    ``(20, 4)``.

    See Also
    --------
    numpy.lib.stride_tricks.as_strided

    Examples
    --------
    >>> y = np.reshape(np.arange(2*3*4), (2,3,4))
    >>> y
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])
    >>> y.strides
    (48, 16, 4)
    >>> y[1,1,1]
    17
    >>> offset=sum(y.strides * np.array((1,1,1)))
    >>> offset/y.itemsize
    17

    >>> x = np.reshape(np.arange(5*6*7*8), (5,6,7,8)).transpose(2,3,1,0)
    >>> x.strides
    (32, 4, 224, 1344)
    >>> i = np.array([3,5,2,2])
    >>> offset = sum(i * x.strides)
    >>> x[3,5,2,2]
    813
    >>> offset / x.itemsize
    813"""

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Same as self.transpose(), except that self is returned if
    self.ndim < 2.

    Examples
    --------
    >>> x = np.array([[1.,2.],[3.,4.]])
    >>> x
    array([[ 1.,  2.],
           [ 3.,  4.]])
    >>> x.T
    array([[ 1.,  3.],
           [ 2.,  4.]])
    >>> x = np.array([1.,2.,3.,4.])
    >>> x
    array([ 1.,  2.,  3.,  4.])
    >>> x.T
    array([ 1.,  2.,  3.,  4.])"""

    __array_finalize__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """None."""

    __array_interface__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Array protocol: Python side."""

    __array_priority__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Array priority."""

    __array_struct__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Array protocol: C-struct side."""



class nditer(object):
    """
    Efficient multi-dimensional iterator object to iterate over arrays.
        To get started using this object, see the
        :ref:`introductory guide to array iteration <arrays.nditer>`.
    
        Parameters
        ----------
        op : ndarray or sequence of array_like
            The array(s) to iterate over.
        flags : sequence of str, optional
            Flags to control the behavior of the iterator.
    
              * "buffered" enables buffering when required.
              * "c_index" causes a C-order index to be tracked.
              * "f_index" causes a Fortran-order index to be tracked.
              * "multi_index" causes a multi-index, or a tuple of indices
                with one per iteration dimension, to be tracked.
              * "common_dtype" causes all the operands to be converted to
                a common data type, with copying or buffering as necessary.
              * "delay_bufalloc" delays allocation of the buffers until
                a reset() call is made. Allows "allocate" operands to
                be initialized before their values are copied into the buffers.
              * "external_loop" causes the `values` given to be
                one-dimensional arrays with multiple values instead of
                zero-dimensional arrays.
              * "grow_inner" allows the `value` array sizes to be made
                larger than the buffer size when both "buffered" and
                "external_loop" is used.
              * "ranged" allows the iterator to be restricted to a sub-range
                of the iterindex values.
              * "refs_ok" enables iteration of reference types, such as
                object arrays.
              * "reduce_ok" enables iteration of "readwrite" operands
                which are broadcasted, also known as reduction operands.
              * "zerosize_ok" allows `itersize` to be zero.
        op_flags : list of list of str, optional
            This is a list of flags for each operand. At minimum, one of
            "readonly", "readwrite", or "writeonly" must be specified.
    
              * "readonly" indicates the operand will only be read from.
              * "readwrite" indicates the operand will be read from and written to.
              * "writeonly" indicates the operand will only be written to.
              * "no_broadcast" prevents the operand from being broadcasted.
              * "contig" forces the operand data to be contiguous.
              * "aligned" forces the operand data to be aligned.
              * "nbo" forces the operand data to be in native byte order.
              * "copy" allows a temporary read-only copy if required.
              * "updateifcopy" allows a temporary read-write copy if required.
              * "allocate" causes the array to be allocated if it is None
                in the `op` parameter.
              * "no_subtype" prevents an "allocate" operand from using a subtype.
              * "arraymask" indicates that this operand is the mask to use
                for selecting elements when writing to operands with the
                'writemasked' flag set. The iterator does not enforce this,
                but when writing from a buffer back to the array, it only
                copies those elements indicated by this mask.
              * 'writemasked' indicates that only elements where the chosen
                'arraymask' operand is True will be written to.
        op_dtypes : dtype or tuple of dtype(s), optional
            The required data type(s) of the operands. If copying or buffering
            is enabled, the data will be converted to/from their original types.
        order : {'C', 'F', 'A', or 'K'}, optional
            Controls the iteration order. 'C' means C order, 'F' means
            Fortran order, 'A' means 'F' order if all the arrays are Fortran
            contiguous, 'C' order otherwise, and 'K' means as close to the
            order the array elements appear in memory as possible. This also
            affects the element memory order of "allocate" operands, as they
            are allocated to be compatible with iteration order.
            Default is 'K'.
        casting : {'no', 'equiv', 'safe', 'same_kind', 'unsafe'}, optional
            Controls what kind of data casting may occur when making a copy
            or buffering.  Setting this to 'unsafe' is not recommended,
            as it can adversely affect accumulations.
    
              * 'no' means the data types should not be cast at all.
              * 'equiv' means only byte-order changes are allowed.
              * 'safe' means only casts which can preserve values are allowed.
              * 'same_kind' means only safe casts or casts within a kind,
                like float64 to float32, are allowed.
              * 'unsafe' means any data conversions may be done.
        op_axes : list of list of ints, optional
            If provided, is a list of ints or None for each operands.
            The list of axes for an operand is a mapping from the dimensions
            of the iterator to the dimensions of the operand. A value of
            -1 can be placed for entries, causing that dimension to be
            treated as "newaxis".
        itershape : tuple of ints, optional
            The desired shape of the iterator. This allows "allocate" operands
            with a dimension mapped by op_axes not corresponding to a dimension
            of a different operand to get a value not equal to 1 for that
            dimension.
        buffersize : int, optional
            When buffering is enabled, controls the size of the temporary
            buffers. Set to 0 for the default value.
    
        Attributes
        ----------
        dtypes : tuple of dtype(s)
            The data types of the values provided in `value`. This may be
            different from the operand data types if buffering is enabled.
        finished : bool
            Whether the iteration over the operands is finished or not.
        has_delayed_bufalloc : bool
            If True, the iterator was created with the "delay_bufalloc" flag,
            and no reset() function was called on it yet.
        has_index : bool
            If True, the iterator was created with either the "c_index" or
            the "f_index" flag, and the property `index` can be used to
            retrieve it.
        has_multi_index : bool
            If True, the iterator was created with the "multi_index" flag,
            and the property `multi_index` can be used to retrieve it.
        index :
            When the "c_index" or "f_index" flag was used, this property
            provides access to the index. Raises a ValueError if accessed
            and `has_index` is False.
        iterationneedsapi : bool
            Whether iteration requires access to the Python API, for example
            if one of the operands is an object array.
        iterindex : int
            An index which matches the order of iteration.
        itersize : int
            Size of the iterator.
        itviews :
            Structured view(s) of `operands` in memory, matching the reordered
            and optimized iterator access pattern.
        multi_index :
            When the "multi_index" flag was used, this property
            provides access to the index. Raises a ValueError if accessed
            accessed and `has_multi_index` is False.
        ndim : int
            The iterator's dimension.
        nop : int
            The number of iterator operands.
        operands : tuple of operand(s)
            The array(s) to be iterated over.
        shape : tuple of ints
            Shape tuple, the shape of the iterator.
        value :
            Value of `operands` at current iteration. Normally, this is a
            tuple of array scalars, but if the flag "external_loop" is used,
            it is a tuple of one dimensional arrays.
    
        Notes
        -----
        `nditer` supersedes `flatiter`.  The iterator implementation behind
        `nditer` is also exposed by the Numpy C API.
    
        The Python exposure supplies two iteration interfaces, one which follows
        the Python iterator protocol, and another which mirrors the C-style
        do-while pattern.  The native Python approach is better in most cases, but
        if you need the iterator's coordinates or index, use the C-style pattern.
    
        Examples
        --------
        Here is how we might write an ``iter_add`` function, using the
        Python iterator protocol::
    
            def iter_add_py(x, y, out=None):
                addop = np.add
                it = np.nditer([x, y, out], [],
                            [['readonly'], ['readonly'], ['writeonly','allocate']])
                for (a, b, c) in it:
                    addop(a, b, out=c)
                return it.operands[2]
    
        Here is the same function, but following the C-style pattern::
    
            def iter_add(x, y, out=None):
                addop = np.add
    
                it = np.nditer([x, y, out], [],
                            [['readonly'], ['readonly'], ['writeonly','allocate']])
    
                while not it.finished:
                    addop(it[0], it[1], out=it[2])
                    it.iternext()
    
                return it.operands[2]
    
        Here is an example outer product function::
    
            def outer_it(x, y, out=None):
                mulop = np.multiply
    
                it = np.nditer([x, y, out], ['external_loop'],
                        [['readonly'], ['readonly'], ['writeonly', 'allocate']],
                        op_axes=[range(x.ndim)+[-1]*y.ndim,
                                 [-1]*x.ndim+range(y.ndim),
                                 None])
    
                for (a, b, c) in it:
                    mulop(a, b, out=c)
    
                return it.operands[2]
    
            >>> a = np.arange(2)+1
            >>> b = np.arange(3)+1
            >>> outer_it(a,b)
            array([[1, 2, 3],
                   [2, 4, 6]])
    
        Here is an example function which operates like a "lambda" ufunc::
    
            def luf(lamdaexpr, *args, **kwargs):
                "luf(lambdaexpr, op1, ..., opn, out=None, order='K', casting='safe', buffersize=0)"
                nargs = len(args)
                op = (kwargs.get('out',None),) + args
                it = np.nditer(op, ['buffered','external_loop'],
                        [['writeonly','allocate','no_broadcast']] +
                                        [['readonly','nbo','aligned']]*nargs,
                        order=kwargs.get('order','K'),
                        casting=kwargs.get('casting','safe'),
                        buffersize=kwargs.get('buffersize',0))
                while not it.finished:
                    it[0] = lamdaexpr(*it[1:])
                    it.iternext()
                return it.operands[0]
    
            >>> a = np.arange(5)
            >>> b = np.ones(5)
            >>> luf(lambda i,j:i*i + j/2, a, b)
            array([  0.5,   1.5,   4.5,   9.5,  16.5])
    """
    def copy(self): # real signature unknown; restored from __doc__
        """
        copy()
        
            Get a copy of the iterator in its current state.
        
            Examples
            --------
            >>> x = np.arange(10)
            >>> y = x + 1
            >>> it = np.nditer([x, y])
            >>> it.next()
            (array(0), array(1))
            >>> it2 = it.copy()
            >>> it2.next()
            (array(1), array(2))
        """
        pass

    def debug_print(self): # real signature unknown; restored from __doc__
        """
        debug_print()
        
            Print the current state of the `nditer` instance and debug info to stdout.
        """
        pass

    def enable_external_loop(self): # real signature unknown; restored from __doc__
        """
        enable_external_loop()
        
            When the "external_loop" was not used during construction, but
            is desired, this modifies the iterator to behave as if the flag
            was specified.
        """
        pass

    def iternext(self): # real signature unknown; restored from __doc__
        """
        iternext()
        
            Check whether iterations are left, and perform a single internal iteration
            without returning the result.  Used in the C-style pattern do-while
            pattern.  For an example, see `nditer`.
        
            Returns
            -------
            iternext : bool
                Whether or not there are iterations left.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def remove_axis(self, i): # real signature unknown; restored from __doc__
        """
        remove_axis(i)
        
            Removes axis `i` from the iterator. Requires that the flag "multi_index"
            be enabled.
        """
        pass

    def remove_multi_index(self): # real signature unknown; restored from __doc__
        """
        remove_multi_index()
        
            When the "multi_index" flag was specified, this removes it, allowing
            the internal iteration structure to be optimized further.
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset()
        
            Reset the iterator to its initial state.
        """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __delslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__delslice__(i, j) <==> del x[i:j]
                   
                   Use of negative indices is not supported.
        """
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

    def __init__(self, x=None, y=None, out=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    def __setslice__(self, i, j, y): # real signature unknown; restored from __doc__
        """
        x.__setslice__(i, j, y) <==> x[i:j]=y
                   
                   Use  of negative indices is not supported.
        """
        pass

    dtypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    finished = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_delayed_bufalloc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_multi_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterationneedsapi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterindex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    iterrange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    itersize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    itviews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    multi_index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    operands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

DATETIMEUNITS = None # (!) real value is ''

typeinfo = {} # real value of type <type 'dict'> replaced

_ARRAY_API = None # (!) real value is ''

_flagdict = {
    'A': 256,
    'ALIGNED': 256,
    'C': 1,
    'CONTIGUOUS': 1,
    'C_CONTIGUOUS': 1,
    'F': 2,
    'FORTRAN': 2,
    'F_CONTIGUOUS': 2,
    'O': 4,
    'OWNDATA': 4,
    'U': 4096,
    'UPDATEIFCOPY': 4096,
    'W': 1024,
    'WRITEABLE': 1024,
}

