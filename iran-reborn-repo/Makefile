CHAPTERS := $(sort $(wildcard manuscript/ch*.md))
BOOK := manuscript/00-front-matter.md $(CHAPTERS) $(wildcard manuscript/appendix-*.md)

.PHONY: check stats epub clean
check:
	python tools/validate_registry.py
	python tools/lint_manuscript.py
stats:
	python tools/stats.py
epub: check
	mkdir -p build
	pandoc $(BOOK) -o build/iran-reborn.epub --toc \
	  --metadata title="Iran Reborn" --metadata author="National Iran Activists Coalition" --metadata lang=en
clean:
	rm -rf build
