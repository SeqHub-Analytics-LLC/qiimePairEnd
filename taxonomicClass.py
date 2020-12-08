import sys
import os
import io
import qiime2.plugins

from qiime2.plugins import metadata, taxa, composition
    
workdir='./'

def taxaClass( reads):
    
    

    gg_classifier = qiime2.Artifact.import_data('TaxonomicClassifier', workdir+'/classifier/')

    taxonomy = feature_classifier.methods.classify_sklearn(reads = qiime2.Artifact.load(reads),
                                                       classifier = gg_classifier)


    return taxonomy

    taxonomy_classification = metadata.visualizers.tabulate(taxonomy.classification.view(qiime2.Metadata))
    taxonomy_classification.visualization

    taxa_bar_plot = taxa.visualizers.barplot(clean_seq.table, taxonomy.classification, sample_metadata)
    taxa_bar_plot.visualization
    

def main():
    "Input is denoised representative sequence"
    denoise(sys.argv[1])


main()
