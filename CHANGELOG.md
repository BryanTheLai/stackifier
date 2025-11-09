# Changelog

All notable changes to Stackifier will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2024-11-09

### Added
- Complete documentation structure with MkDocs
- Contributing guidelines (CONTRIBUTING.md)
- Security policy (SECURITY.md)
- LICENSE file (MIT)
- GitHub issue and PR templates
- CI/CD workflows for testing and publishing
- Comprehensive guides for WhatsApp, LangGraph, LiteLLM, and S3
- API reference documentation
- Project structure documentation

### Changed
- Promoted to stable 1.0.0 release
- Enhanced README with badges and links
- Improved project organization

## [0.1.0] - 2024-11-09

### Added
- Initial release of Stackifier
- TraceHook for event logging
- FileWriter and S3Writer storage backends
- WhatsApp adapters (Meta Cloud API, Twilio)
- LiteLLM integration
- LangChain integration
- LangGraph integration
- OpenRouter integration
- OpenAI-compatible event schema
- Rich metrics (timing, tokens, costs)
- Examples for common use cases

### Features
- Local-first JSONL logging
- Optional S3 cloud storage
- WhatsApp webhook normalization
- Tool call tracking
- Multi-turn conversation support
- Buffered writes for performance

[Unreleased]: https://github.com/BryanTheLai/pip-stackifier/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/BryanTheLai/pip-stackifier/compare/v0.1.0...v1.0.0
[0.1.0]: https://github.com/BryanTheLai/pip-stackifier/releases/tag/v0.1.0
