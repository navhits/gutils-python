"""
All constants, credentials and secrets go here.
"""
import os
from typing import Optional

# pylint: disable=line-too-long
# pylint: disable=invalid-name
def Secret(environment_variable: str,
        required: bool, default_value: Optional[str] = None) -> None:
    """
    This function checks and imports the environment variables and raises exception if they are not set.
    """
    value = os.getenv(environment_variable)
    if not value and default_value:
        value = default_value
    if required and not value:
        raise Exception(f"'{environment_variable}' environment variable is not set. Please set it before execution.")
    return value
