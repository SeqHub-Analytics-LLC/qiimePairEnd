import sys
import os
import io
import qiime2.plugins



	

# Filter, denoise, pair, and remove chimeras

from qiime2.plugins.dada2.methods import denoise_paired
from qiime2.plugins import feature_table





# denoising
def denoise(per_sample):
    clean_seq = denoise_paired(qiime2.Artifact.load(per_sample),
                               trunc_len_f=150, trunc_len_r=150,
                               trim_left_f=13, trim_left_r=13, n_threads=4)

    rep_seq=clean_seq.representative_sequences.save("rep_seq.qza")
    table_seq=clean_seq.table.save("table_seq.qza")
    denoiseStats_seq=clean_seq.denoising_stats.save("denoiseStats_seq.qza") 
    return clean_seq


    #Visualize representative sequences
    dada_seq_viz = feature_table.visualizers.summarize(table_seq,
                                                        sample_metadata)
    dada_seq_viz.visualization 
    

    #Visualize feature table

    feature_table_viz = feature_table.visualizers.summarize(qiime2.Artifact.load(tabSeq),
                                                        sample_metadata)
    feature_table_viz.visualization


def main():
    "Input here is the demultiplexed sequence(per_sample_sequences)"
    denoise(sys.argv[1])


main()

