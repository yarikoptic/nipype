import nipype.interfaces.io as nio           # Data i/o
import nipype.interfaces.utility as util     # utility
import nipype.pipeline.engine as pe          # pypeline engine
import nipype.interfaces.ants as ants
import nibabel as nb
import os                                    # system functions

data_dir = os.path.abspath('antsdata/brains')
subject_list = ['B1', 'B2', 'B3', 'B4' ,'B5']

#data_dir = os.path.abspath('antsdata/faces')
#subject_list = ['YFace1', 'YFace2', 'YFace3', 'YFace4', 'YFace5','YFace6', 'YFace7', 'YFace8', 'YFace9']

"""
Use infosource node to loop through the subject list and define the input files.
"""

infosource = pe.Node(interface=util.IdentityInterface(fields=['subject_id']), name="infosource")
infosource.iterables = ('subject_id', subject_list)

info = dict(images=[['subject_id']])

"""
Use datasource node to perform the actual data grabbing.
Templates for the associated images are used to obtain the correct images.
"""
datasource = pe.Node(interface=nio.DataGrabber(infields=['subject_id'],
                                               outfields=info.keys()),
                     name = 'datasource')

datasource.inputs.template = "%s"
datasource.inputs.base_directory = data_dir
datasource.inputs.field_template = dict(images='%s.tiff')
datasource.inputs.template_args = info
datasource.inputs.base_directory = data_dir

inputnode = pe.Node(interface=util.IdentityInterface(fields=['subject_id','images']), name='inputnode')

createTemplate = pe.Node(interface=ants.BuildTemplate(), name='createTemplate')
createTemplate.inputs.image_dimension = 2
#createTemplate.inputs.similarity_metric = 'CC'
#createTemplate.inputs.transformation_model = 'GR'
#createTemplate.inputs.max_iterations = [30,50,20]
createTemplate.inputs.output_prefix = 'BTP'

normalize = pe.Workflow(name="normalize")
# bash /usr/lib/ants/buildtemplateparallel.sh -d 2 -o template_ -g 0 -i 4 -m 30x50x20 -c 0 -r 0 -s CC -t GR {B1.tiff,B2.tiff}

ants = pe.Workflow(name="ants_tutorial")
ants.base_dir = os.path.abspath('ants_tutorial/workingdir')

ants.connect([
                    (infosource,datasource,[('subject_id', 'subject_id')]),
                    (datasource,inputnode,[('images','images')]),
                    (infosource,inputnode,[('subject_id','subject_id')]),
                ])

datasink = pe.Node(interface=nio.DataSink(), name="datasink")
datasink.inputs.base_directory = os.path.abspath('ants_tutorial/l1output')

def getimgdir(subject_id):
    import os
    return os.path.join(os.path.abspath('ants_tutorial/workingdir'),'_subject_id_%s' % subject_id)

ants.connect([(inputnode, datasink,[('images','@l1output')]),
                ])

if __name__ == '__main__':
    ants.run()
    ants.write_graph()

def get_nsubs(group_list):
    nsubs = 0
    for grp in group_list.keys():
        nsubs += len(group_list[grp])
    return nsubs

def make_inlist(n, from_node):
    inlist = list()
    connections = list()
    for i in range(1,n+1):
    #    inlist = (from_node + '[{idx}]'.format(idx=i),str('in{num}'.format(num=i)))
        inlist = (from_node,str('in{num}'.format(num=i)))
        connections.append(inlist)
    return connections

group_list = {}
group_list['one'] = subject_list[0:3]
group_list['two'] = subject_list[3:5]

l2infosource = pe.Node(interface=util.IdentityInterface(fields=['subject_id']), name="l2infosource")
l2infosource.inputs.subject_id = subject_list
l2inputnode = pe.Node(interface=util.IdentityInterface(fields=['subject_id','images']), name='l2inputnode')

l2source = pe.Node(nio.DataGrabber(outfields=['images']), name="l2source")
#l2source.inputs.subject_id = subject_list
#l2source.inputs.template_args = dict(images=[['subject_id','subject_id']])
l2source.inputs.template=os.path.abspath('ants_tutorial/l1output/*.tiff')
l2source.inputs.base_directory = data_dir

l2pipeline = pe.Workflow(name="level2")
l2pipeline.base_dir = os.path.abspath('ants_tutorial/l2output')
l2pipeline.connect([
                    (l2infosource,l2source,[('subject_id', 'subject_id')]),
                    (l2source,l2inputnode,[('images','images')]),
                    (l2infosource,l2inputnode,[('subject_id','subject_id')]),
                ])

mergenode = pe.Node(util.Merge(get_nsubs(group_list)), name="mergenode")

subj_connections = make_inlist(get_nsubs(group_list), 'images')
#groupcon.connect([(connectivity,merge_subject_list,subj_connections)])
#l3pipeline = pe.Workflow(name="level3")
#l3pipeline.base_dir = os.path.abspath('ants_tutorial/l3output')

#l2pipeline.connect([(l2inputnode,mergenode,subj_connections)])

#l2pipeline.connect([(mergenode,createTemplate,[('out','images')])])
l2pipeline.connect([(l2source,createTemplate,[('images','images')])])

if __name__ == '__main__':
    l2pipeline.run()
    l2pipeline.write_graph(graph2use='flat')

#if __name__ == '__main__':
    #l3pipeline.run()
    #l3pipeline.write_graph(graph2use='flat')
