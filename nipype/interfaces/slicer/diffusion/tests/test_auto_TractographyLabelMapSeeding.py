# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..diffusion import TractographyLabelMapSeeding


def test_TractographyLabelMapSeeding_inputs():
    input_map = dict(
        InputVolume=dict(
            argstr='%s',
            position=-2,
        ),
        OutputFibers=dict(
            argstr='%s',
            hash_files=False,
            position=-1,
        ),
        args=dict(argstr='%s', ),
        clthreshold=dict(argstr='--clthreshold %f', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        inputroi=dict(argstr='--inputroi %s', ),
        integrationsteplength=dict(argstr='--integrationsteplength %f', ),
        label=dict(argstr='--label %d', ),
        maximumlength=dict(argstr='--maximumlength %f', ),
        minimumlength=dict(argstr='--minimumlength %f', ),
        name=dict(argstr='--name %s', ),
        outputdirectory=dict(
            argstr='--outputdirectory %s',
            hash_files=False,
        ),
        randomgrid=dict(argstr='--randomgrid ', ),
        seedspacing=dict(argstr='--seedspacing %f', ),
        stoppingcurvature=dict(argstr='--stoppingcurvature %f', ),
        stoppingmode=dict(argstr='--stoppingmode %s', ),
        stoppingvalue=dict(argstr='--stoppingvalue %f', ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        useindexspace=dict(argstr='--useindexspace ', ),
        writetofile=dict(argstr='--writetofile ', ),
    )
    inputs = TractographyLabelMapSeeding.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_TractographyLabelMapSeeding_outputs():
    output_map = dict(
        OutputFibers=dict(position=-1, ),
        outputdirectory=dict(),
    )
    outputs = TractographyLabelMapSeeding.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
