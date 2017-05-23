# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..model import Cluster


def test_Cluster_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    connectivity=dict(argstr='--connectivity=%d',
    ),
    cope_file=dict(argstr='--cope=%s',
    ),
    dlh=dict(argstr='--dlh=%.10f',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    find_min=dict(argstr='--min',
    usedefault=True,
    ),
    fractional=dict(argstr='--fractional',
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='--in=%s',
    mandatory=True,
    ),
    minclustersize=dict(argstr='--minclustersize',
    usedefault=True,
    ),
    no_table=dict(argstr='--no_table',
    usedefault=True,
    ),
    num_maxima=dict(argstr='--num=%d',
    ),
    out_index_file=dict(argstr='--oindex=%s',
    hash_files=False,
    ),
    out_localmax_txt_file=dict(argstr='--olmax=%s',
    hash_files=False,
    ),
    out_localmax_vol_file=dict(argstr='--olmaxim=%s',
    hash_files=False,
    ),
    out_max_file=dict(argstr='--omax=%s',
    hash_files=False,
    ),
    out_mean_file=dict(argstr='--omean=%s',
    hash_files=False,
    ),
    out_pval_file=dict(argstr='--opvals=%s',
    hash_files=False,
    ),
    out_size_file=dict(argstr='--osize=%s',
    hash_files=False,
    ),
    out_threshold_file=dict(argstr='--othresh=%s',
    hash_files=False,
    ),
    output_type=dict(),
    peak_distance=dict(argstr='--peakdist=%.10f',
    ),
    pthreshold=dict(argstr='--pthresh=%.10f',
    requires=['dlh', 'volume'],
    ),
    std_space_file=dict(argstr='--stdvol=%s',
    ),
    terminal_output=dict(nohash=True,
    ),
    threshold=dict(argstr='--thresh=%.10f',
    mandatory=True,
    ),
    use_mm=dict(argstr='--mm',
    usedefault=True,
    ),
    volume=dict(argstr='--volume=%d',
    ),
    warpfield_file=dict(argstr='--warpvol=%s',
    ),
    xfm_file=dict(argstr='--xfm=%s',
    ),
    )
    inputs = Cluster.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Cluster_outputs():
    output_map = dict(index_file=dict(),
    localmax_txt_file=dict(),
    localmax_vol_file=dict(),
    max_file=dict(),
    mean_file=dict(),
    pval_file=dict(),
    size_file=dict(),
    threshold_file=dict(),
    )
    outputs = Cluster.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
