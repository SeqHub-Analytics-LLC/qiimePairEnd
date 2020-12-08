import sys
import os
import io
import qiime2.plugins



from qiime2.plugins.demux.visualizers import summarize


def demuxVisual(per_sample_seq):
 
    demux_summary = summarize(qiime2.Artifact.load(per_sample_seq))

    demux_summary.visualization
    return demux_summary.visualization


def main():

    demuxVisual(sys.argv[1])


main()