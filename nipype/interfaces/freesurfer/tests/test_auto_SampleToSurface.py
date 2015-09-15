# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.utils import SampleToSurface

def test_SampleToSurface_inputs():
    input_map = dict(apply_rot=dict(argstr='--rot %.3f %.3f %.3f',
    ),
    apply_trans=dict(argstr='--trans %.3f %.3f %.3f',
    ),
    args=dict(argstr='%s',
    ),
    cortex_mask=dict(argstr='--cortex',
    xor=['mask_label'],
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    fix_tk_reg=dict(argstr='--fixtkreg',
    ),
    float2int_method=dict(argstr='--float2int %s',
    ),
    frame=dict(argstr='--frame %d',
    ),
    hemi=dict(argstr='--hemi %s',
    mandatory=True,
    ),
    hits_file=dict(argstr='--srchit %s',
    ),
    hits_type=dict(argstr='--srchit_type',
    ),
    ico_order=dict(argstr='--icoorder %d',
    requires=['target_subject'],
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    interp_method=dict(argstr='--interp %s',
    ),
    mask_label=dict(argstr='--mask %s',
    xor=['cortex_mask'],
    ),
    mni152reg=dict(argstr='--mni152reg',
    mandatory=True,
    xor=['reg_file', 'reg_header', 'mni152reg'],
    ),
    no_reshape=dict(argstr='--noreshape',
    xor=['reshape'],
    ),
    out_file=dict(argstr='--o %s',
    genfile=True,
    ),
    out_type=dict(argstr='--out_type %s',
    ),
    override_reg_subj=dict(argstr='--srcsubject %s',
    requires=['subject_id'],
    ),
    projection_stem=dict(mandatory=True,
    xor=['sampling_method'],
    ),
    reference_file=dict(argstr='--ref %s',
    ),
    reg_file=dict(argstr='--reg %s',
    mandatory=True,
    xor=['reg_file', 'reg_header', 'mni152reg'],
    ),
    reg_header=dict(argstr='--regheader %s',
    mandatory=True,
    requires=['subject_id'],
    xor=['reg_file', 'reg_header', 'mni152reg'],
    ),
    reshape=dict(argstr='--reshape',
    xor=['no_reshape'],
    ),
    reshape_slices=dict(argstr='--rf %d',
    ),
    sampling_method=dict(argstr='%s',
    mandatory=True,
    requires=['sampling_range', 'sampling_units'],
    xor=['projection_stem'],
    ),
    sampling_range=dict(),
    sampling_units=dict(),
    scale_input=dict(argstr='--scale %.3f',
    ),
    smooth_surf=dict(argstr='--surf-fwhm %.3f',
    ),
    smooth_vol=dict(argstr='--fwhm %.3f',
    ),
    source_file=dict(argstr='--mov %s',
    mandatory=True,
    ),
    subject_id=dict(),
    subjects_dir=dict(),
    surf_reg=dict(argstr='--surfreg',
    requires=['target_subject'],
    ),
    surface=dict(argstr='--surf %s',
    ),
    target_subject=dict(argstr='--trgsubject %s',
    ),
    terminal_output=dict(nohash=True,
    ),
    vox_file=dict(argstr='--nvox %s',
    ),
    )
    inputs = SampleToSurface.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_SampleToSurface_outputs():
    output_map = dict(hits_file=dict(),
    out_file=dict(),
    vox_file=dict(),
    )
    outputs = SampleToSurface.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

