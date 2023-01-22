# Copyright 2021-2022 The Alibaba Fundamental Vision Team Authors. All rights reserved.
from typing import TYPE_CHECKING

#from modelscope.utils.import_utils import LazyImportModule


if TYPE_CHECKING:
    from .emotion_model import EfficientNetForFaceEmotion

else:
    _import_structure = {'emotion_model': ['EfficientNetForFaceEmotion']}

    import sys

    sys.modules[__name__] = LazyImportModule(
        __name__,
        globals()['__file__'],
        _import_structure,
        module_spec=__spec__,
        extra_objects={},
    )
