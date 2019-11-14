# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..dcmstack import DcmStack


def test_DcmStack_inputs():
    input_map = dict(
        dicom_files=dict(mandatory=True,),
        embed_meta=dict(),
        exclude_regexes=dict(),
        force_read=dict(usedefault=True,),
        include_regexes=dict(),
        out_ext=dict(usedefault=True,),
        out_format=dict(),
        out_path=dict(),
    )
    inputs = DcmStack.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DcmStack_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = DcmStack.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
