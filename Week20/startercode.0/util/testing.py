import sys

class Testing:

    def __init__(self, precision=3, *args, **kwargs):
        # sys.tracebacklimit = 1
        self._precision = precision
        self._errmsg = kwargs.get('errmsg') or "Not quite."
        self._successmsg = kwargs.get('successmsg') or "Good job!"

    def assert_equal(self, *args):
        '''
        This is a wrapper for unittest.TestCase.assertEqual.
        Must have > python v3.1.

        Asserts that groups of things (generic type) are similar.
        Must be input as groups of tuples.

        If the values do not compare equal, the test will fail.

        In addition, if first and second are the exact same type and one of
        list, tuple, dict, set, frozenset or str or any type that a subclass
        registers with addTypeEqualityFunc() the type-specific equality
        function will be called in order to generate a more useful default
        error message (see also the list of type-specific methods).

        Example:
            assert_equal((list1, list2), (dict3, dict4))

        Returns None if all set groups are similar to each other.
        '''
        import unittest

        for arg in args:
            if not isinstance(arg, tuple):
                raise Exception('Input set pairs not a tuple')
            if arg.__len__() != 2:
                raise Exception('Need exactly two sets to compare per tuple')
            for el in arg:
                if not (isinstance(el, list) or \
                        isinstance(el, tuple) or \
                        isinstance(el, dict) or \
                        isinstance(el, set) or \
                        isinstance(el, frozenset) or \
                        isinstance(el, str)):
                    raise Exception('Input must be of type list, tuple, '
                                    'dict, set, or frozenset')
            unittest.TestCase().assertEqual(arg[0], arg[1], msg=self._errmsg)
        return

    def assert_frames(self, *args):
        '''
        Asserts that groups of dataframes are similar.
        Frames must be input as tuples.

        Example:
            assert_frames((X_train_ans, X_train), (X_test_ans, X_test))

        Returns None if all frame groups are similar to each other.
        '''
        import pandas as pd

        for frames in args:
            if not isinstance(frames, tuple):
                raise Exception('Input frame pairs not a tuple')
            if frames.__len__() != 2:
                raise Exception('Need exactly two frames to compare per tuple')
            for frame in frames:
                if not isinstance(frame, pd.core.frame.DataFrame):
                    raise Exception('Input frames must be of type pandas.core.fram'
                                    'e.DataFrame')
            pd.testing.assert_frame_equal(
                frames[0],
                frames[1],
                check_names=False,
                check_like=True,
                check_less_precise=self._precision
            )
        return

    def assert_series(self, *args):
        '''
        Asserts that groups of series are similar.
        Series must be input as tuples.

        Example:
            assert_series((y_train_ans, y_train), (y_test_ans, y_test))

        Returns None if all series groups are similar to each other.
        '''
        import pandas as pd

        for series in args:
            if not isinstance(series, tuple):
                raise Exception('Input series pairs not a tuple')
            if series.__len__() != 2:
                raise Exception('Need exactly two series to compare per tuple')
            for serie in series:
                if not isinstance(serie, pd.core.series.Series):
                    raise Exception('Input series must be of type pandas.core.seri'
                                    'es.Series')
            pd.testing.assert_series_equal(
                series[0],
                series[1],
                check_less_precise=self._precision
            )
        return

    def assert_arrays(self, *args):
        '''
        Asserts that groups of arrays are similar.
        Arrays must be input as tuples.

        Example:
            assert_arrays((arr1, arr2), (arr3, arr4))

        Returns None if all array groups are similar to each other.
        '''
        import numpy as np
        import collections

        for arrays in args:
            if not isinstance(arrays, tuple):
                raise Exception('Input array pairs not a tuple')
            if arrays.__len__() != 2:
                raise Exception('Need exactly two arrays to compare per tuple')
            for array in arrays:
                if not (isinstance(array, collections.Sequence) or \
                        isinstance(array, np.ndarray)):
                    raise Exception('Input series must be of array-like')
            np.testing.assert_array_almost_equal(
                arrays[0],
                arrays[1],
                decimal=self._precision,
                verbose=False,
                err_msg=self._errmsg
            )
        return

    def assert_ints(self, *args):
        '''
        Asserts that groups of ints are similar.
        Ints must be input as tuples.

        Example:
            assert_ints((int1, int2), (int3, int4))

        Returns None if all int groups are similar to each other.
        '''
        import math

        for ints in args:
            if not isinstance(ints, tuple):
                raise Exception('Input int pairs not a tuple')
            if ints.__len__() != 2:
                raise Exception('Need exactly two ints to compare per tuple')
            for i in ints:
                if not isinstance(i, int):
                    raise Exception('Input number must be an integer')
            assert ints[0] == ints[1], self._errmsg
        return

    def assert_floats(self, *args):
        '''
        Asserts that groups of floats are similar.
        Floats must be input as tuples.

        Example:
            assert_floats((float1, float2), (float3, float4))

        Returns None if all float groups are similar to each other.
        '''
        import math

        for floats in args:
            if not isinstance(floats, tuple):
                raise Exception('Input float pairs not a tuple')
            if floats.__len__() != 2:
                raise Exception('Need exactly two floats to compare per tuple')
            for f in floats:
                if not isinstance(f, float):
                    raise Exception('Input number must be a float')
            assert math.isclose(
                floats[0],
                floats[1],
                rel_tol=10**-self._precision
            ), self._errmsg
        return

    def assert_letter_answer(self, *args):
        '''
        Validates single letter answer responses (i.e. 'a', 'b', 'c').
        Strings must be input as tuples.

        Example:
            assert_strings((string1, string2), (string3, string4))

        Returns None if all string groups are similar to each other.
        '''
        import re

        for strings in args:
            if not isinstance(strings, tuple):
                raise Exception('Input string pairs not a tuple')
            if strings.__len__() != 2:
                raise Exception('Need exactly two strings to compare per tuple')
            res = [str(), str()]
            for i, string in enumerate(strings):
                if not isinstance(string, str):
                    raise Exception('Input must be a string')
                regex_output = re.findall(r'[A-Za-z]', string)
                if regex_output.__len__() == 0:
                    raise AssertionError("No answer found in parsed string.")
                if regex_output.__len__() > 1:
                    raise AssertionError("Please enter one answer only.")
                res[i] = regex_output[0]

            assert res[0].lower() == res[1].lower(), self._errmsg
        return

    def print_success(self):
        '''
        Prints success message to student upon passing assertion
        '''
        print(self._successmsg)

if __name__ == '__main__':
    print("Not a script")
