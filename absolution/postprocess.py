import click
from absolution.processing_steps.clustering.option_requirements import ClusteringAlgorithmOption, MinClusterSizeOption
from absolution.consts import ClusteringMethods
from absolution.format_input import FormattedInput
from absolution.processing_steps.abundance_and_enrichment import EnrichmentProcessingStep
from absolution.processing_steps.clustering.clustering_analysis import ClusteringAnalysis


@click.group(chain=True, invoke_without_command=True)
@click.option("-i", "--input_folder", type=click.Path(), help="Full path to input folder", required=True)
@click.option("--combine_all", type=click.BOOL, help="Do you wish to combine all datasets, may reduce efficiency (y/n)", default=False)
def cli(input_folder, combine_all):
    pass


@cli.result_callback()
def process_pipeline(processing_steps, input_folder, combine_all):
    working_dfs = FormattedInput(input_folder, combine_all).format()
    for working_df in working_dfs:
        for processing_step in processing_steps:
            current_df = working_df.copy()
            working_df = processing_step.run(current_df)


@cli.command("abundance")
@click.option("--rounds", type=str, help="Expected number of rounds", required=False)
def abundance(rounds):
    return EnrichmentProcessingStep(rounds)


@cli.command("clustering")

#type=click.Choice([c.value for c in Color])
@click.option("-algorithm", "--clustering_algorithm", type=click.Choice([clustering_method.value for clustering_method in ClusteringMethods], case_sensitive=False), help="Desired clustering algorithm", cls=ClusteringAlgorithmOption)
@click.option("-min_size", "--min_cluster_size", type=int, help="minimum allowed cluster size", cls=MinClusterSizeOption)
@click.option("-max_size", "--max_cluster_size", type=int, help="maximum allowed cluster size", required=False)
def clusetering(clustering_algorithm, min_cluster_size, max_cluster_size): # , min_cluster_size, max_cluster_size, max_time_allowed

    return ClusteringAnalysis(clustering_algorithm, min_cluster_size, max_cluster_size)


@cli.command("liabilities")
@click.option("-custom", "--custom_liability_list", type=click.Path(), help="Full path to the custom liability list", required=False)
def liabilities(custom_liability_list):
    pass


if __name__ == '__main__':
    cli()
