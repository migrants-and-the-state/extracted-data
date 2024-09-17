# Migrants and the State:<br>Extracted Data

Here you'll find (meta)data extracted from the M&TS A Files corpus along with useful files and scripts for managing that (meta)data.

E.g.,

+ [`data/metadata_outputs`](data/metadata_outputs/)
  - contains JSON documents of metadata scoped 1 per document image
  - the metadata contained was extracted via spacy LLM ML model
    + see: [Deployment_Framework](https://github.com/Migrants-and-The-State/Deployment_Framework/) and [Model_Trainer](https://github.com/Migrants-and-The-State/Model_Trainer) repos
  - the documents reference the original image as served through a IIIF Image API
    + see: https://nyu-dh.github.io/aperitiiif-batch-migrants-state/
+ [`schemas/document-schema.json`](schemas/document-schema.json)
  - is the machine-readable JSON schema for the documents above
+ [`lib/validate_json_to_schema.py`](lib/validate_json_to_schema.py)
  - a script that checks if every JSON document in `data/metadata_outputs` coheres to the schema

## Getting started

### Prerequisites

You'll need Python, Git, and poetry installed to use the data and run the scripts available in `/lib`. On mac, we recommend using [Homebrew](https://brew.sh/) and [asdf](https://asdf-vm.com/). 

If you already have Homebrew [installed](https://docs.brew.sh/Installation):

#### 1. Install asdf:

```sh
brew install coreutils curl git gh
brew install asdf
```

Then follow [the instructions](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf) for your system to add `asdf` to your shell's `PATH`. If you're using ZSH, for example, you'll run:

```sh
echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ${ZDOTDIR:-~}/.zshrc
source ~/.zshrc
```

#### 2. Install python via asdf
```sh
asdf plugin-add python
asdf plugin-add direnv
asdf direnv setup --shell zsh --version latest # if using ZSH! can replace with bash
```

### 3. Install pipx and poetry
```sh
brew install pipx
pipx ensurepath 
source ~/.zshrc # if using ZSH! can replace with ~/.bashrc
```

## Using this repo

### 1. Clone the project repo and set up local python

``` sh
gh repo clone Migrants-and-The-State/extracted-data && cd extracted-data
adsf install python
poetry install
```
### 2. Run the scipts (so far just schema validation!)

``` sh
poetry run python lib/validate_json_to_schema.py
```

