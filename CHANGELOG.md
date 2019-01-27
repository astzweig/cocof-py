# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.2] - 2019-01-27
### Fixed
- Fix the missing argument error volume 2. The changes introduced in
  version 1.2.1 did not solve the problem, they just hid it. We reverted
  those changes and fixed the real cause of the problem.
- Fix an error, that would prevent the data to be written back to the
  file and hence leave you with an empty file.

## [1.2.1] - 2019-01-27
### Fixed
- Fix the missing argument error. Because of a missing default value,
  cocof would not run but instead complain that an argument was missing.
  This has been fixed now.

## [1.2.0] - 2019-01-18
### Added
- Support read and write of `plist` file format (a format mostly found on
Apple's macOS). Supported are both xml and binary plists.

### Changed
- Better error messages. `cocof` showed a single message for a whole group of
errors and sometimes the reason of the message would not be the reason of the
error and hence the message would mislead.

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
