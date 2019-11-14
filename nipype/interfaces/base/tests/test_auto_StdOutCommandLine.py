# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..core import StdOutCommandLine


def test_StdOutCommandLine_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        out_file=dict(argstr="> %s", extensions=None, genfile=True, position=-1,),
    )
    inputs = StdOutCommandLine.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
