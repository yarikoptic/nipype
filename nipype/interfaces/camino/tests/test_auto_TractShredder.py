# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..convert import TractShredder


def test_TractShredder_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        bunchsize=dict(
            argstr='%d',
            position=2,
            units='NA',
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='< %s',
            mandatory=True,
            position=-2,
        ),
        offset=dict(
            argstr='%d',
            position=1,
            units='NA',
        ),
        out_file=dict(
            argstr='> %s',
            genfile=True,
            position=-1,
        ),
        space=dict(
            argstr='%d',
            position=3,
            units='NA',
        ),
    )
    inputs = TractShredder.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TractShredder_outputs():
    output_map = dict(shredded=dict(), )
    outputs = TractShredder.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
