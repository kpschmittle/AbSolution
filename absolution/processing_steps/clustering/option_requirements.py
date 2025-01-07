import click

from absolution.consts import ClusteringMethods
from absolution.option_utils import DependentlyRequiredOption


class ClusteringAlgorithmOption(click.Option):
    def process_value(self, ctx, value):
        value = super(ClusteringAlgorithmOption, self).process_value(ctx, value)
        return ClusteringMethods(value)

class MinClusterSizeOption(DependentlyRequiredOption):
    DEPENDEE_VALUES = (
        ClusteringMethods.linclust,
        ClusteringMethods.linclust_man,
        ClusteringMethods.mmseqs,
        ClusteringMethods.clonotyping
    )
    DEPENDEE_NAME = 'clustering_algorithm'


class MaxClusterSizeOption(DependentlyRequiredOption):
    DEPENDEE_VALUES = (
        ClusteringMethods.linclust,
        ClusteringMethods.linclust_man,
        ClusteringMethods.mmseqs,
        ClusteringMethods.clonotyping
    )
    DEPENDEE_NAME = 'clustering_algorithm'


