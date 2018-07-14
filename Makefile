# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = BDD
SOURCEDIR     = doc/source
BUILDDIR      = doc/build
SOURCEDIRDEV  = doc/source-dev
BUILDDIRDEV   = doc/build-dev

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile html-dev

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).


%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIRDEV)" "$(BUILDDIRDEV)" $(SPHINXOPTS) $(O)

html-dev:
	@$(SPHINXBUILD) -M html "$(SOURCEDIRDEV)" "$(BUILDDIRDEV)" $(SPHINXOPTS) $(O)

html-client:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
