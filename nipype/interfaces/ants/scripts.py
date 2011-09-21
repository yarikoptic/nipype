"""The ANTS module provides classes for interfacing with commands from the Advanced Normalization Tools module
--------
See the docstrings of the individual classes for examples.

"""

from glob import glob
import os
import warnings
from nipype.utils.filemanip import fname_presuffix, split_filename
from nipype.interfaces.base import CommandLineInputSpec, CommandLine, traits, TraitedSpec, File, InputMultiPath, Directory
from nipype.interfaces.traits_extension import isdefined

def ANTSScript(func):
    """Base support for ANTS scripts
    """
    import os, os.path as op
    try:
        antspath = os.environ['ANTSPATH']
    except KeyError:
        raise Exception('ANTSPATH not set')
    return op.join(antspath,func)
#    return 'bash ' + op.join(antspath,func)

class BuildTemplateInputSpec(CommandLineInputSpec):
    """
    buildtemplateparallel.sh -d ImageDimension -o OUTPREFIX <other options> <images>

    Example Case:

     echo " bash buildtemplateparallel.sh -d 3 -m 30x50x20 -t GR  -s CC -c 1 -o MY -z InitialTemplate.nii.gz  *RF*T1x.nii.gz "
     echo " in this case you use 30x50x20 iterations per registration "
     echo " 4 iterations over template creation (that is the default) "
     echo " with Greedy-SyN and CC metrics to guide the mapping. "
     echo " Output is prepended with MY and the initial template is InitialTemplate.nii.gz (optional). "
     echo " the -c option is set to 1 which will try to use SGE to distribute the computation. "
     echo " if you do not have SGE, use -c 0 or -c 2 --- read the help."
    """
    image_dimension = traits.Enum(3, 2, 4, argstr='-d %d', mandatory=True, usedefault=True, position=1,
        desc='ImageDimension: 2 or 3 (for 2 or 3 Dimensional registration)'\
        'ImageDimension: 4 (for 3 dimensional registration of time-series; requires FSL)')

    images = InputMultiPath(File, exists=True, argstr='%s', position=-1,
        desc='List of images in the current directory, eg *_t1.nii.gz. Should be at the end' \
          'of the command.', copyfile=True)

    similarity_metric = traits.Enum('CC', 'MI', 'SMI', 'PR', 'MSQ', 'PSE', 'JTB',
        argstr='-s %s',
        desc='Similarity metric. See ANTS? for the details')

    transformation_model = traits.Enum('GR', 'Diff', 'Elast', 'Exp', 'SyN', usedefault=True,
        argstr='-t %s',
        desc='Transformation model. See ANTS? for the details')

    output_prefix = traits.Str('template_', argstr='-o %s', position=2, usedefault=True,
        desc='A prefix that is prepended to all output files.')

    target_volume = File(exists=True, argstr='-z %s',
        desc='Use this this volume as the target of all inputs. When not used, the script '
            'will create an unbiased starting point by averaging all inputs. Use the full path!')

    parallel_computation = traits.Enum(0, 1, 2,
        argstr='-c %s', mandatory=True, usedefault=True,
        desc='Control for parallel computation (default 0) '
             '-- 0 == run serially, 1 == SGE qsub, 2 == use PEXEC (localhost)')

    gradient_step_size = traits.Float(0.25, argstr='-g %d', usedefault=True,
        desc='Gradient step size (default 0.25) -- smaller magnitude results in more cautious steps')

    iteration_limit = traits.Int(4, argstr='-i %d', usedefault=True,
        desc='Iteration limit (default 4) -- iterations of the template construction (Iteration limit)*NumImages registrations.')

    rigid_registration = traits.Enum(0, 1,
        argstr='-r %d', mandatory=True, usedefault=True,
        desc='Do rigid-body registration of inputs before creating template '
             '(default 0) -- 0 == off 1 == on. Only useful when you do not '
             'have an initial template')

    number_of_cores = traits.Int(argstr='-j %d',
        desc='Number of cpu cores to use (default: 2; -- requires "-c 2" (PEXEC)')

    max_iterations = traits.List(traits.Int, argstr='-m %s',
        desc='Number of iterations per level -- a vector e.g. : [100,100,20]',
        minlen=3, maxlen=3, sep='x')

    n3_bias_field_correction = traits.Int(1, argstr='-n %d',
        desc='N3BiasFieldCorrection of moving image (default 1) -- 0 == off, 1 == on')

class BuildTemplateOutputSpec(TraitedSpec):
    output = File(exists=True, desc='The output image')
    output_dir = Directory(exists=True)

class BuildTemplate(CommandLine):
    """
    """
    _cmd = ANTSScript('buildtemplateparallel.sh')
    input_spec=BuildTemplateInputSpec
    output_spec=BuildTemplateOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs["output"] = os.path.abspath(self._gen_outfilename())
        return outputs
    def _gen_filename(self, name):
        if name is 'output':
            return self._gen_outfilename()
        else:
            return None
    def _gen_outfilename(self):
        _, name, _  = split_filename(self.inputs.images[0])
        return self.inputs.output_prefix + 'template' + '.nii.gz'

    def write_groups_for_bash(self, python_list):
        return "{" + ",".join(python_list) + "}"

    def _format_arg(self, name, spec, value):
        if name == 'images':
            names = []
            for img in value:
                path, name, ext = split_filename(img)
                names.append(name + ext)
            return spec.argstr% self.write_groups_for_bash(names)
        return super(BuildTemplate, self)._format_arg(name, spec, value)

class SimpleANTSInputSpec(CommandLineInputSpec):
    image_dimension = traits.Enum(3, 2,
        argstr='%d', mandatory=True, usedefault=True, position=1,
        desc='ImageDimension: 2 or 3 (for 2 or 3 Dimensional registration)')

    fixed_image = File(exists=True, argstr='%s', mandatory=True, position=2,
        desc='Fixed image')

    moving_image = File(exists=True, argstr='%s', mandatory=True, position=3,
        desc='Moving image')

    output_prefix = traits.Str('SA_', argstr='%s', position=4, usedefault=True,
        desc='A prefix that is prepended to all output files.')

    max_iterations = traits.List(traits.Int, argstr='%s', position=5,
        desc='Number of iterations per level -- a vector e.g. : [100,100,20]',
        minlen=3, maxlen=3, sep='x')

    labels_to_deform = File(exists=True, argstr='%s', position=6,
        desc='Optional: Labels in fixed image space to deform to moving image')

    do_ants_QC = traits.Bool(argstr='%s', position=7,
        desc='Option: DoANTSQC (boolean)')

class SimpleANTSOutputSpec(TraitedSpec):
    output = File(exists=True, desc='The output image')
    output_dir = Directory(exists=True)

class SimpleANTS(CommandLine):
    """
    echo " USAGE ::  "
    echo "  sh   ants.sh  ImageDimension  fixed.ext  moving.ext  OPTIONAL-OUTPREFIX   OPTIONAL-max-iterations  OPTIONAL-Labels-In-Fixed-Image-Space-To-Deform-To-Moving-Image     Option-DoANTSQC "
    echo " be sure to set ANTSPATH environment variable "
    echo " Max-Iterations in form :    JxKxL where "
    echo "  J = max iterations at coarsest resolution (here, reduce by power of 2^2) "
    echo " K = middle resolution iterations ( here, reduce by power of 2 ) "
    echo " L = fine resolution iterations ( here, full resolution ) -- this level takes much more time per iteration "
    echo " an extra  Ix before JxKxL would add another level "
    echo " Default ierations is  $MAXITERATIONS  -- you can often get away with fewer for many apps "
    echo " Other parameters are updates of the defaults used in the A. Klein evaluation paper in Neuroimage, 2009 "
    """
    _cmd = ANTSScript('ants.sh')
    input_spec=SimpleANTSInputSpec
    output_spec=SimpleANTSOutputSpec
