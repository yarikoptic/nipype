# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.afni.preprocess import Refit
def test_Refit_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    deoblique=dict(argstr='-deoblique',
    ),
    args=dict(argstr='%s',
    ),
    yorigin=dict(argstr='-yorigin %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(copyfile=True,
    mandatory=True,
    position=-1,
    argstr='%s',
    ),
    xorigin=dict(argstr='-xorigin %s',
    ),
    zorigin=dict(argstr='-zorigin %s',
    ),
    )
    inputs = Refit.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_Refit_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Refit.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
