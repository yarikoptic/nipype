# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import AlignEpiAnatPy


def test_AlignEpiAnatPy_inputs():
    input_map = dict(
        anat=dict(argstr="-anat %s", copyfile=False, extensions=None, mandatory=True,),
        anat2epi=dict(argstr="-anat2epi",),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        epi2anat=dict(argstr="-epi2anat",),
        epi_base=dict(argstr="-epi_base %s", mandatory=True,),
        epi_strip=dict(argstr="-epi_strip %s",),
        in_file=dict(
            argstr="-epi %s", copyfile=False, extensions=None, mandatory=True,
        ),
        outputtype=dict(),
        py27_path=dict(usedefault=True,),
        save_skullstrip=dict(argstr="-save_skullstrip",),
        suffix=dict(argstr="-suffix %s", usedefault=True,),
        tshift=dict(argstr="-tshift %s", usedefault=True,),
        volreg=dict(argstr="-volreg %s", usedefault=True,),
    )
    inputs = AlignEpiAnatPy.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_AlignEpiAnatPy_outputs():
    output_map = dict(
        anat_al_mat=dict(extensions=None,),
        anat_al_orig=dict(extensions=None,),
        epi_al_mat=dict(extensions=None,),
        epi_al_orig=dict(extensions=None,),
        epi_al_tlrc_mat=dict(extensions=None,),
        epi_reg_al_mat=dict(extensions=None,),
        epi_tlrc_al=dict(extensions=None,),
        epi_vr_al_mat=dict(extensions=None,),
        epi_vr_motion=dict(extensions=None,),
        skullstrip=dict(extensions=None,),
    )
    outputs = AlignEpiAnatPy.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
