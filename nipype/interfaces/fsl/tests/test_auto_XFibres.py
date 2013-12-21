# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.dti import XFibres
def test_XFibres_inputs():
    input_map = dict(sample_every=dict(argstr='--sampleevery=%d',
    ),
    no_spat=dict(xor=('no_spat', 'non_linear'),
    argstr='--nospat',
    ),
    n_jumps=dict(argstr='--njumps=%d',
    ),
    seed=dict(argstr='--seed=%d',
    ),
    burn_in=dict(argstr='--burnin=%d',
    ),
    bvecs=dict(mandatory=True,
    argstr='--bvecs=%s',
    ),
    all_ard=dict(xor=('no_ard', 'all_ard'),
    argstr='--allard',
    ),
    n_fibres=dict(argstr='--nfibres=%d',
    ),
    non_linear=dict(xor=('no_spat', 'non_linear'),
    argstr='--nonlinear',
    ),
    logdir=dict(usedefault=True,
    argstr='--logdir=%s',
    ),
    dwi=dict(mandatory=True,
    argstr='--data=%s',
    ),
    fudge=dict(argstr='--fudge=%d',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    no_ard=dict(xor=('no_ard', 'all_ard'),
    argstr='--noard',
    ),
    args=dict(argstr='%s',
    ),
    force_dir=dict(usedefault=True,
    argstr='--forcedir',
    ),
    update_proposal_every=dict(argstr='--updateproposalevery=%d',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    bvals=dict(mandatory=True,
    argstr='--bvals=%s',
    ),
    mask=dict(mandatory=True,
    argstr='--mask=%s',
    ),
    burn_in_no_ard=dict(argstr='--burninnoard=%d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    output_type=dict(),
    model=dict(argstr='--model=%d',
    ),
    )
    inputs = XFibres.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_XFibres_outputs():
    output_map = dict(mean_fsamples=dict(),
    mean_S0samples=dict(),
    dyads=dict(),
    phsamples=dict(),
    fsamples=dict(),
    thsamples=dict(),
    mean_dsamples=dict(),
    )
    outputs = XFibres.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
