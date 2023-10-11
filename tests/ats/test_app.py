import json
import logging
import os
import shutil
import subprocess  # nosec
import time
from typing import Any

import pykube
import pytest
import requests
import yaml
from pykube import HTTPClient
from pytest_helm_charts.clusters import Cluster
from pytest_helm_charts.giantswarm_app_platform.app import (
    AppCR,
    AppFactoryFunc,
    ConfiguredApp,
)
from pytest_helm_charts.k8s.deployment import wait_for_deployments_to_run
from pytest_helm_charts.k8s.daemon_set import wait_for_daemon_sets_to_run
from pytest_helm_charts.k8s.namespace import ensure_namespace_exists

logger = logging.getLogger(__name__)

timeout: int = 360

app_catalog_url = "https://giantswarm.github.io/giantswarm-catalog/"

app_namespace = "kube-system"
app_name = "k8s-dns-node-cache-app"

@pytest.mark.smoke
def test_api_working(kube_cluster: Cluster) -> None:
    """
    Test if the kubernetes api works
    """
    assert kube_cluster.kube_client is not None
    assert len(pykube.Node.objects(kube_cluster.kube_client)) >= 1

    kube_cluster.kubectl(
        "get ns"
    )


@pytest.mark.smoke
def test_app_deployed(kube_cluster: Cluster):
    app = (
        AppCR.objects(kube_cluster.kube_client)
        .filter(namespace=app_namespace)
        .get_by_name(app_name)
    )
    app_version = app.obj["status"]["version"]
    wait_for_daemon_sets_to_run(
        kube_cluster.kube_client,
        # this is the name of the deployments
        ["k8s-dns-node-cache"],
        app_namespace,
        timeout,
    )
    logger.info(f"k8s-dns-node-cache-app installed in appVersion {app_version}")

