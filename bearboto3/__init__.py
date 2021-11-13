"""Ensures a supported version of python is being used,
as well as handling appropriate imports based on the current
python version.
"""


from sys import version_info

MIN_PYTHON_VER = (3, 6, 2)
PYTHON_VER_SPLIT = (3, 9)

assert version_info >= MIN_PYTHON_VER

if version_info >= PYTHON_VER_SPLIT:
    # pylint: disable=no-name-in-module
    from typing import Annotated
else:
    from typing_extensions import Annotated
