[![CircleCI](https://circleci.com/gh/giantswarm/k8s-dns-node-cache-app/tree/main.svg?style=svg)](https://circleci.com/gh/giantswarm/k8s-dns-node-cache-app/tree/main) [![Docker Repository on Quay](https://quay.io/repository/giantswarm/k8s-dns-node-cache/status "Docker Repository on Quay")](https://quay.io/repository/giantswarm/k8s-dns-node-cache)

# k8s-dns-node-cache-app

This repository contains a Giant Swarm managed app that deploys the [Node Local DNS strategy](https://kubernetes.io/docs/tasks/administer-cluster/nodelocaldns/) in a kubernetes cluster.

NodeLocal DNSCache improves Cluster DNS performance by running a dns caching agent on cluster nodes as a DaemonSet.
In today's architecture, Pods in ClusterFirst DNS mode reach out to a kube-dns serviceIP for DNS queries.
This is translated to a kube-dns/CoreDNS endpoint via iptables rules added by kube-proxy.
With this new architecture, Pods will reach out to the dns caching agent running on the same node, thereby avoiding iptables DNAT rules and connection tracking.
The local caching agent will query kube-dns service for cache misses of cluster hostnames(cluster.local suffix by default).

## Installation and configuration

This App is meant to be a drop-in add-on that can be installed with default configuration in any Giant Swarm cluster.
The app will be running as a daemonset alongside the already existing `coreDNS` app, dramatically improving DNS resolution
performances with a very small footprint in terms of system resources.

## Network Policies

When installing `k8s-dns-node-cache-app` you need to ensure any other workload running in the cluster has access to the new DNS service.
This is an example network policy you might need to create:

```
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-node-local-dns-for-my-app
  podSelector:
    matchLabels:
      app: web
  policyTypes:
    - Egress
  egress:
  - to:
    - podSelector:
        matchLabels:
          k8s-app: k8s-dns-node-cache
    ports:
    - protocol: UDP
      port: 53
    - protocol: UDP
      port: 1053
  - to:
    - podSelector:
        matchLabels:
          k8s-app: coredns
    ports:
    - protocol: UDP
      port: 53
    - protocol: UDP
      port: 1053
```

## Performance improvements

Without the `k8s-dns-node-cache` app installed:

```
DNS Performance Testing Tool
Version 2.2.1

[Status] Command line: dnsperf -l 300 -s 172.31.0.10 -Q 1000 -d /opt/records.txt
[Status] Sending queries (to 172.31.0.10)
[Status] Started at: Fri Mar  4 10:40:50 2022
[Status] Stopping after 300.000000 seconds
[Status] Testing complete (time limit)

Statistics:

  Queries sent:         300000
  Queries completed:    300000 (100.00%)
  Queries lost:         0 (0.00%)

  Response codes:       NOERROR 300000 (100.00%)
  Average packet size:  request 55, response 108
  Run time (s):         300.000111
  Queries per second:   999.999630

  Average Latency (s):  0.000129 (min 0.000066, max 0.018556)
  Latency StdDev (s):   0.000146

```

With the `k8s-dns-node-cache` app installed:
```

```

## Known issues and limitations

- The upstream application only works with `kube-proxy`-based clusters. It will NOT work when using other `Kubernetes Service` implementations such as `Cilium` for example.
- This app only works with `kube-proxy` in `iptables` more. The upstream application works in `IPVS` mode as well, but the Giant Swarm app does not support that use case.
- After removing the application previously installed in the cluster, it might take some time for the injected `iptables` rules to be deleted. 
  While that happens, DNS queries will fail for all pods running in that node will fail. We suggest rolling or rebooting all nodes after deleting this app.
