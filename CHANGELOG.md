# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project's packages adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Disable PSPs for k8s 1.25 and newer.

## [1.1.0] - 2023-01-11

## Changed

- Add app to the `default` app catalog.

## [1.0.1] - 2022-12-19

## Changed

- Added minAllowed CPU and memory to sensible default for node-cache pod.

## [1.0.0] - 2022-10-31

### Changed

- Use CoreDNS as upstream in order to avoid double configuration for internal domains.

## [0.4.0] - 2022-04-21

### Changed

- Separate coredns and node-cache metric ports.

## [0.3.0] - 2022-04-19

### Changed

- Use `kube-system` as namespace.

## [0.2.0] - 2022-03-22

### Added

- Add VerticalPodAutoscaler CR.

## [0.1.0] - 2022-03-08

### Added

- First release featuring upstream version 1.21.4.

[Unreleased]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v0.4.0...v1.0.0
[0.4.0]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/giantswarm/k8s-dns-node-cache-app/compare/v0.0.0...v0.1.0
