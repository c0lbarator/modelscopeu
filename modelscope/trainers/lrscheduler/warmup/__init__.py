# Copyright (c) Alibaba, Inc. and its affiliates.

from typing import TYPE_CHECKING

#from modelscope.utils.import_utils import LazyImportModule


if TYPE_CHECKING:
    from .base import BaseWarmup
    from .warmup import ConstantWarmup, ExponentialWarmup, LinearWarmup

else:
    _import_structure = {
        'base': ['BaseWarmup'],
        'warmup': ['ConstantWarmup', 'ExponentialWarmup', 'LinearWarmup']
    }

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
