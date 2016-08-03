# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..preprocess import Denoise


def test_Denoise_inputs():
    input_map = dict(block_radius=dict(),
    in_file=dict(mandatory=True,
    ),
    in_mask=dict(),
    noise_mask=dict(),
    noise_model=dict(mandatory=True,
    usedefault=True,
    ),
    patch_radius=dict(),
    signal_mask=dict(),
    snr=dict(),
    )
    inputs = Denoise.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Denoise_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Denoise.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
