# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.mrtrix.tensors import DWI2SphericalHarmonicsImage

def test_DWI2SphericalHarmonicsImage_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    encoding_file=dict(argstr='-grad %s',
    mandatory=True,
    position=1,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    maximum_harmonic_order=dict(argstr='-lmax %s',
    ),
    normalise=dict(argstr='-normalise',
    position=3,
    ),
    out_filename=dict(argstr='%s',
    genfile=True,
    position=-1,
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    )
    inputs = DWI2SphericalHarmonicsImage.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_DWI2SphericalHarmonicsImage_outputs():
    output_map = dict(spherical_harmonics_image=dict(),
    )
    outputs = DWI2SphericalHarmonicsImage.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

