# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..cmtk import CreateMatrix


def test_CreateMatrix_inputs():
    input_map = dict(
        count_region_intersections=dict(usedefault=True,),
        out_endpoint_array_name=dict(extensions=None, genfile=True,),
        out_fiber_length_std_matrix_mat_file=dict(extensions=None, genfile=True,),
        out_intersection_matrix_mat_file=dict(extensions=None, genfile=True,),
        out_matrix_file=dict(extensions=None, genfile=True,),
        out_matrix_mat_file=dict(extensions=None, usedefault=True,),
        out_mean_fiber_length_matrix_mat_file=dict(extensions=None, genfile=True,),
        out_median_fiber_length_matrix_mat_file=dict(extensions=None, genfile=True,),
        resolution_network_file=dict(extensions=None, mandatory=True,),
        roi_file=dict(extensions=None, mandatory=True,),
        tract_file=dict(extensions=None, mandatory=True,),
    )
    inputs = CreateMatrix.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CreateMatrix_outputs():
    output_map = dict(
        endpoint_file=dict(extensions=None,),
        endpoint_file_mm=dict(extensions=None,),
        fiber_label_file=dict(extensions=None,),
        fiber_labels_noorphans=dict(extensions=None,),
        fiber_length_file=dict(extensions=None,),
        fiber_length_std_matrix_mat_file=dict(extensions=None,),
        filtered_tractographies=dict(),
        filtered_tractography=dict(extensions=None,),
        filtered_tractography_by_intersections=dict(extensions=None,),
        intersection_matrix_file=dict(extensions=None,),
        intersection_matrix_mat_file=dict(extensions=None,),
        matlab_matrix_files=dict(),
        matrix_file=dict(extensions=None,),
        matrix_files=dict(),
        matrix_mat_file=dict(extensions=None,),
        mean_fiber_length_matrix_mat_file=dict(extensions=None,),
        median_fiber_length_matrix_mat_file=dict(extensions=None,),
        stats_file=dict(extensions=None,),
    )
    outputs = CreateMatrix.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
