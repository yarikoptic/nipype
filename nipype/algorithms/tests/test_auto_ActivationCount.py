# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..stats import ActivationCount


def test_ActivationCount_inputs():
    input_map = dict(
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_files=dict(mandatory=True, ),
        threshold=dict(mandatory=True, ),
    )
    inputs = ActivationCount.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ActivationCount_outputs():
    output_map = dict(
        acm_neg=dict(),
        acm_pos=dict(),
        out_file=dict(),
    )
    outputs = ActivationCount.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
