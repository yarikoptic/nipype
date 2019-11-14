# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import RigidRegistration


def test_RigidRegistration_inputs():
    input_map = dict(
        FixedImageFileName=dict(argstr="%s", extensions=None, position=-2,),
        MovingImageFileName=dict(argstr="%s", extensions=None, position=-1,),
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        fixedsmoothingfactor=dict(argstr="--fixedsmoothingfactor %d",),
        histogrambins=dict(argstr="--histogrambins %d",),
        initialtransform=dict(argstr="--initialtransform %s", extensions=None,),
        iterations=dict(argstr="--iterations %s", sep=",",),
        learningrate=dict(argstr="--learningrate %s", sep=",",),
        movingsmoothingfactor=dict(argstr="--movingsmoothingfactor %d",),
        outputtransform=dict(argstr="--outputtransform %s", hash_files=False,),
        resampledmovingfilename=dict(
            argstr="--resampledmovingfilename %s", hash_files=False,
        ),
        spatialsamples=dict(argstr="--spatialsamples %d",),
        testingmode=dict(argstr="--testingmode ",),
        translationscale=dict(argstr="--translationscale %f",),
    )
    inputs = RigidRegistration.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RigidRegistration_outputs():
    output_map = dict(
        outputtransform=dict(extensions=None,),
        resampledmovingfilename=dict(extensions=None,),
    )
    outputs = RigidRegistration.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
