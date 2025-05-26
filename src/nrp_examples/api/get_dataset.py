from pathlib import Path

import pandas as pd
from nrp_cmd import get_sync_client
from nrp_cmd.sync_client import resolve_record_id
from nrp_cmd.sync_client.streams.file import FileSink


def main():
    # search for datasets and print them as pandas DataFrame
    zenodo_client = get_sync_client("https://www.zenodo.org")
    records = zenodo_client.records.search(q="title:precipitation", size=10)
    df = records.as_dataframe()
    print(df)

    # get a dataset by its DOI
    doi = "https://doi.org/10.5281/zenodo.7676478"
    client, record_url = resolve_record_id(doi)
    record = client.records.read(record_url)
    print(record.metadata["title"])

    # list all files in the dataset
    files = client.files.list(record)
    df = files.as_dataframe()
    print(df)

    # first csv file
    first_csv = next(f for f in files if f.key.endswith("csv"))

    loaded_csv = pd.read_csv(str(first_csv.links.content))
    print(loaded_csv)

    client.files.download(files[0], FileSink(Path("/tmp/downloaded.bin")))

    # TODO: download record metadata and all files to a folder without using cmdline cli


if __name__ == "__main__":
    main()
