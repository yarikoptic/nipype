# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..base import NiftyRegCommand


def test_NiftyRegCommand_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        omp_core_val=dict(argstr="-omp %i", usedefault=True,),
    )
    inputs = NiftyRegCommand.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
