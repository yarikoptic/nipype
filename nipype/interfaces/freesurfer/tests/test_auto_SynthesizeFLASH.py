# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import SynthesizeFLASH


def test_SynthesizeFLASH_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        fixed_weighting=dict(argstr="-w", position=1,),
        flip_angle=dict(argstr="%.2f", mandatory=True, position=3,),
        out_file=dict(argstr="%s", extensions=None, genfile=True,),
        pd_image=dict(argstr="%s", extensions=None, mandatory=True, position=6,),
        subjects_dir=dict(),
        t1_image=dict(argstr="%s", extensions=None, mandatory=True, position=5,),
        te=dict(argstr="%.3f", mandatory=True, position=4,),
        tr=dict(argstr="%.2f", mandatory=True, position=2,),
    )
    inputs = SynthesizeFLASH.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_SynthesizeFLASH_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = SynthesizeFLASH.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
