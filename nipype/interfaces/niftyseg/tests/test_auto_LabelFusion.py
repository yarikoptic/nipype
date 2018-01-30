# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..label_fusion import LabelFusion


def test_LabelFusion_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        classifier_type=dict(
            argstr='-%s',
            mandatory=True,
            position=2,
        ),
        conv=dict(argstr='-conv %f', ),
        dilation_roi=dict(),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        file_to_seg=dict(mandatory=True, ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-in %s',
            mandatory=True,
            position=1,
        ),
        kernel_size=dict(),
        mask_file=dict(argstr='-mask %s', ),
        max_iter=dict(argstr='-max_iter %d', ),
        mrf_value=dict(argstr='-MRF_beta %f', ),
        out_file=dict(
            argstr='-out %s',
            name_source=['in_file'],
            name_template='%s',
        ),
        prob_flag=dict(argstr='-outProb', ),
        prob_update_flag=dict(argstr='-prop_update', ),
        proportion=dict(argstr='-prop %s', ),
        set_pq=dict(argstr='-setPQ %f %f', ),
        sm_ranking=dict(
            argstr='-%s',
            position=3,
            usedefault=True,
        ),
        template_file=dict(),
        template_num=dict(),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        unc=dict(argstr='-unc', ),
        unc_thresh=dict(argstr='-uncthres %f', ),
        verbose=dict(argstr='-v %s', ),
    )
    inputs = LabelFusion.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_LabelFusion_outputs():
    output_map = dict(out_file=dict(), )
    outputs = LabelFusion.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
