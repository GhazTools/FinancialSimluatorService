"""
file_name = resource_loader.py
Created On: 2024/02/29
Lasted Updated: 2024/02/29
Description: _FILL OUT HERE_
Edit Log:
2024/02/29
    - Created file
"""

# STANDARD LIBRARY IMPORTS
from importlib.abc import Loader
from importlib.machinery import ModuleSpec
from importlib.util import module_from_spec, spec_from_file_location

from types import ModuleType
from typing import Any, cast

# THIRD PARTY LIBRARY IMPORTS

# LOCAL LIBRARY IMPORTS


# pylint: disable=too-few-public-methods
class ModuleLoader:
    """
    A class used to load modules
    """

    @staticmethod
    def load_object_from_module(
        full_module_path: str, spec_name: str, object_name: str
    ) -> Any:
        """
        Load an object form a module
        """

        module_spec: ModuleSpec = cast(
            ModuleSpec,
            spec_from_file_location(spec_name, full_module_path),
        )
        module: Loader = cast(Loader, module_from_spec(module_spec))
        cast(Loader, module_spec.loader).exec_module(cast(ModuleType, module))

        assert hasattr(module, object_name)
        return getattr(module, object_name)
