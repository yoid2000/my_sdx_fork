from my_sdx_fork.clustering.common import StitchOwner
from my_sdx_fork.clustering.strategy import NoClustering, SingleClustering
from my_sdx_fork.common import *

from ..conftest import *


def test_no_clustering() -> None:
    forest = load_forest("dummy.csv")
    clusters, _ = NoClustering().build_clusters(forest)
    print(clusters.initial_cluster)
    print(clusters.derived_clusters)
    assert clusters.initial_cluster == [ColumnId(0)]
    assert clusters.derived_clusters == [
        (StitchOwner.SHARED, [], [ColumnId(1)]),
        (StitchOwner.SHARED, [], [ColumnId(2)]),
        (StitchOwner.SHARED, [], [ColumnId(3)]),
    ]


def test_single_clustering() -> None:
    forest = load_forest("dummy.csv")
    clusters, _ = SingleClustering().build_clusters(forest)
    assert clusters.initial_cluster == [ColumnId(0), ColumnId(1), ColumnId(2), ColumnId(3)]
    assert clusters.derived_clusters == []
