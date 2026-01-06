SHELL := /bin/bash

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

generate-schema-docs: ## Build the Markdown API docs and UML diagrams
	rm -rf ./docs/schemas/generated
	mkdir -p ./docs/schemas/generated
	python -m tools.documentation --autodoc --associations 5
