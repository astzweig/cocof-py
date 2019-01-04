# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2019-01-05
### Added
- We now use travis to deploy the package to pypi. That way pypi should always
remain up to date with this repository.

### Fixed
- `cocof` would print a misleading 'unknown file format' error, when the
provided json patch contained syntax errors. We replaced this by a composition
of a general warning and an additional specific note. 
- Due to an error in the file extension normalization process, `cocof` would
recognize a '.yaml' file as YAML, but not '.yml'.

## [1.0.0] - 2019-01-04
### Summertime Madness
The first version has arrived on this warm winter day. We wish good luck!
