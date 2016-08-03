# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ...testing import assert_equal
from ..mesh import MeshWarpMaths


def test_MeshWarpMaths_inputs():
    input_map = dict(float_trait=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_surf=dict(mandatory=True,
    ),
    operation=dict(usedefault=True,
    ),
    operator=dict(mandatory=True,
    ),
    out_file=dict(usedefault=True,
    ),
    out_warp=dict(usedefault=True,
    ),
    )
    inputs = MeshWarpMaths.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_MeshWarpMaths_outputs():
    output_map = dict(out_file=dict(),
    out_warp=dict(),
    )
    outputs = MeshWarpMaths.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
