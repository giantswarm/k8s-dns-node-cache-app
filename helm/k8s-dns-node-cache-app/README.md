# k8s-dns-node-cache-app

A Helm chart to run NodeLocal DNSCache in Kubernetes clusters

**Homepage:** <https://github.com/giantswarm/k8s-dns-node-cache-app>

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| name | string | `"k8s-dns-node-cache"` |  |
| namespace | string | `"kube-system"` |  |
| serviceType | string | `"managed"` |  |
| image.registry | string | `"gsoci.azurecr.io"` |  |
| image.name | string | `"giantswarm/k8s-dns-node-cache"` |  |
| image.tag | string | `"1.26.7"` |  |
| updateStrategy.rollingUpdate.maxUnavailable | string | `"10%"` |  |
| cluster.kubernetes.DNS.IP | string | `"172.31.0.10"` |  |
| cluster.kubernetes.DNS.serviceName | string | `"coredns"` |  |
| cluster.kubernetes.LOCAL.IP | string | `"169.254.20.10"` |  |
| cluster.kubernetes.clusterDomain | string | `"cluster.local"` |  |
| ports.prometheus.nodecache | int | `9253` |  |
| ports.prometheus.coredns | int | `9254` |  |
| ports.liveness | int | `8080` |  |
| upstreamService.servicePort | int | `53` |  |
| upstreamService.podPort | int | `1053` |  |
| upstreamService.appName | string | `"coredns"` |  |
| resources.requests.cpu | string | `"50m"` |  |
| resources.requests.memory | string | `"100Mi"` |  |
| configmap.cache.success | int | `30` |  |
| configmap.cache.denial | int | `5` |  |
| configmap.noAAAAResponse | bool | `true` |  |
| configmap.log.enabled | bool | `false` |  |
| ciliumNetworkPolicy.enabled | bool | `true` | Render a CiliumNetworkPolicy. When false, a plain NetworkPolicy is rendered instead. |
| ciliumNetworkPolicy.egress | list | `[]` | Replaces the default CiliumNetworkPolicy egress rules when set. |
| ciliumNetworkPolicy.ingress | list | `[]` | Replaces the default CiliumNetworkPolicy ingress rules when set. |
| ciliumLocalRedirectPolicy.enabled | bool | `true` | Redirect traffic for the cluster DNS Service to the node-local cache with a CiliumLocalRedirectPolicy. |
