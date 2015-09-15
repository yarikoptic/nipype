# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dipy.tensors import DTI

def test_DTI_inputs():
    input_map = dict(bvals=dict(mandatory=True,
    ),
    bvecs=dict(mandatory=True,
    ),
    in_file=dict(mandatory=True,
    ),
    mask_file=dict(),
    out_filename=dict(genfile=True,
    ),
    )
    inputs = DTI.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DTI_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = DTI.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

