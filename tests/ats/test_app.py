from pytest import mark
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.giantswarm_app_platform.app import wait_for_apps_to_run
from pytest_helm_charts.k8s.daemon_set import wait_for_daemon_sets_to_run

@mark.smoke
@mark.functional
@mark.upgrade
def test_k8s_dns_node_cache(kube_cluster: Cluster) -> None:
    assert kube_cluster.kube_client is not None

    # Wait for k8s-dns-node-cache app to run.
    wait_for_apps_to_run(kube_cluster.kube_client, [ "k8s-dns-node-cache-app" ], "kube-system", 60)

    # Wait for k8s-dns-node-cache daemon set to run.
    wait_for_daemon_sets_to_run(kube_cluster.kube_client, [ "k8s-dns-node-cache" ], "kube-system", 60)
