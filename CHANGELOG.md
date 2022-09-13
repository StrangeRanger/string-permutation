# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Replaced `.format()` with `f-string`.
- Updated tdqm requirements to version `4.64.1`.

## [1.1.7] - 2021-05-27

### Changed

- Changed docstrings from `Numpy` to `reST`.
- Update all of the docstrings to include more info.
- Reduced duplicate code.

## [1.1.6] - 2021-03-28

### Changed

- Changed commenting and docstring formatting.

### Fixed

- Fixed PYL-R1705.
- Fixed Pylint - W0107.

## [1.1.5] - 2021-02-19


### Changed

- Update docstrings.
- Minor refactoring.

## [1.1.4] - 2021-01-11

### Changed

- Modified code to use the [black](https://github.com/psf/black) coding style.

## [1.1.3] - 2020-12-13

### Changed

- `tqdm` is no longer optional.
- Reduced duplicate code.
- Update function docstrings.

## [1.1.2] - 2020-11-03

### Changed

- Coding style and commenting changes for better readability.

## [1.1.1] - 2020-07-20

### Added

- `requirements.txt` has been added to easily install required dependencies.

## [1.1.0] - 2020-06-28

### Added

- Added more descriptive comments.
- A progress bar is now displayed when permutations are to be saved to a file.
- Files created that don't have any data written to them will now be removed upon forced or non-forced exiting of the program.
- Additional options on how to continue have been added for whenever you are creating a file that has the same name as a file that already exists.

### Changed

- Displays file sizes with appropriate units (KiB for windows, and KB for everything else).
- Reorganized all of the code to make more sense and easier to read.
- Renamed several functions and variables.

### Fixed

- Cleanly handles `SIGINT` and `SIGTSTP` signals.
- Fixed a few other bugs.

## [1.0.0] - 2020-06-17

First release, that of which was previously a gist.

[unreleased]: https://github.com/StrangeRanger/string-permutation/compare/v1.1.7...HEAD
[1.1.7]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.7
[1.1.6]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.6
[1.1.5]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.5
[1.1.4]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.4
[1.1.3]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.3
[1.1.2]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.2
[1.1.1]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.1
[1.1.0]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.1.0
[1.0.0]: https://github.com/StrangeRanger/string-permutation/releases/tag/v1.0.0
