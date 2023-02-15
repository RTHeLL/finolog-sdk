# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.6] - 2023-02-15
### Added
- add `FinologCountryService`
- add return `bool` in `get_or_create_by_inn`


## [1.0.4] - 2023-02-13
### Added
- add `FinologRequisiteService`
- add `get_or_create_by_inn` in `FinologContractorService`
- add `validate_string_length`


## [1.0.3] - 2023-02-13
### Added
- add payload validation
- add `ValidationError`
- implemented `create_contractor` method
- implemented `update_contractor` method

### Changed
- move client to `client.py`

### Removed
- `__validate_contractor_id` method

## [1.0.1] - 2023-02-10
### Changed
- minor changes

## [1.0.0] - 2023-02-10
### Added
- Project
