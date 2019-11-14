# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..c3 import C3dAffineTool


def test_C3dAffineTool_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        fsl2ras=dict(argstr="-fsl2ras", position=4,),
        itk_transform=dict(argstr="-oitk %s", hash_files=False, position=5,),
        reference_file=dict(argstr="-ref %s", extensions=None, position=1,),
        source_file=dict(argstr="-src %s", extensions=None, position=2,),
        transform_file=dict(argstr="%s", extensions=None, position=3,),
    )
    inputs = C3dAffineTool.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_C3dAffineTool_outputs():
    output_map = dict(itk_transform=dict(extensions=None,),)
    outputs = C3dAffineTool.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
