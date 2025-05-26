# Invenio for Workflows

## Sample record metadata

Sample record metadata in the invenio-ccmm format are at [datarepo git repository](https://raw.githubusercontent.com/NRP-CZ/datarepo/refs/heads/main/sample_data/dataset.json) .

JSON Schema for validation is at [generated jsonschema in github](https://github.com/NRP-CZ/datarepo/blob/main/datasets/records/jsonschemas/datasets-1.0.0.json) and the model from which this was generated is at [oarepo-model-builder-ccmm](https://github.com/NRP-CZ/oarepo-model-builder-ccmm/blob/main/oarepo_model_builder_ccmm/builtin_models/ccmm.yaml) .

## API usage

See [API examples](./src/nrp_examples/api/) for more examples of how to use the API directly.

## Jupyter notebooks

See [Jupyter notebooks](./src/nrp_examples/jupyter/) for examples of how to use the API from Jupyter notebooks.

## Command-line client

### Installation

Download [`https://raw.githubusercontent.com/NRP-CZ/nrp-cmd/refs/heads/main/nrp-cmd`](https://raw.githubusercontent.com/NRP-CZ/nrp-cmd/refs/heads/main/nrp-cmd), make it executable and place it in your path.

Alternatively, you can create a virtualenv and install it there:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -U setuptools pip wheel
pip install nrp-cmd
```

## Adding a repository

```bash
> nrp-cmd add repository https://workflow-repo.test.du.cesnet.cz/ wfrepo

Adding repository https://workflow-repo.test.du.cesnet.cz/ with alias wfrepo

I will try to open the following url in your browser:
https://workflow-repo.test.du.cesnet.cz//account/settings/applications/tokens/new

Please log in inside the browser.
When the browser tells you that the token has been created, 
copy the token and paste it here.
Press enter to open the page ...

Paste the token here: 
Creating repository with token ...
Added repository wfrepo -> https://workflow-repo.test.du.cesnet.cz/
```

To log in, please use the following credentials at the moment:

```
Username: nrdocstest+datapilot@gmail.com
Password: <ask us for the password>
```

## Creating a record

Download [the sample metadata](https://raw.githubusercontent.com/NRP-CZ/datarepo/refs/heads/main/sample_data/dataset.json) and then invoke:

```bash
❯ nrp-cmd create record dataset.json --repository wfrepo --community generic --set recid 
                                                     
  Record 1m1sg-q4y94                                                                                                         
 ──────────────────────────────────────────────────────────
  ...
title                   Climate Change Impacts on Alpine Plant Communities in the Czech Republic (2015-2020)                 

```

The `--repository` is optional if you've registered just a single repository with the nrp-cmd. The `community` parameter is the community in which the record will be created - this is required at the moment. The `--set` will store the URL of the created record in an internal variable called `recid`:

```bash
❯ nrp-cmd list variables
Variables                                                                         
                                                                                  
  Name    Values                                                                  
 ──────────────────────────────────────────────────────────────────────────────── 
  recid   https://workflow-repo.test.du.cesnet.cz/api/datasets/1m1sg-q4y94/draft 
```

**Note:** Add `-f json` to any call to see the result formatted as a json document. Similarly `-f yaml`

## Uploading files

```bash
nrp-cmd upload file @recid ~/Downloads/ubuntu-24.04-desktop-amd64.iso --repository wfrepo
```

The upload will automatically switch to multipart if the file is bigger and will use direct upload to S3 on the background.

## Publishing the record

```bash
nrp-cmd publish record @recid
```

If the publish fails (for example, required metadata were not filled in), you'll get an error.
Otherwise, the published record will be printed to stdout.

## Downloading record with files

```bash
nrp-cmd download record @recid --repository wfrepo
```
