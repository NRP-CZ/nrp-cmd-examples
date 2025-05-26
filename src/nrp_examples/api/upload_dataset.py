import os

from nrp_cmd import get_sync_client
from nrp_cmd.config import RepositoryConfig
from nrp_cmd.sync_client.streams.memory import MemorySource
from yarl import URL


def main():
    # Get a synchronous client for the repository and configure the token
    client = get_sync_client(
        RepositoryConfig(
            alias="datarepo-test",
            url=URL("https://workflow-repo.test.du.cesnet.cz"),
            token=os.environ.get("NRP_TOKEN", None) or input("Enter your API token: "),
        ),
    )
    # Alternatively, register the repository via nrp-cmd:
    #  nrp-cmd add repository https://workflow-repo.test.du.cesnet.cz datarepo-test
    # and get the client with:
    #
    # client = get_sync_client("datarepo-test")
    #
    dataset_metadata = {
        "metadata": {
            "title": "Test dataset",
        }
    }

    created_record = client.records.create(dataset_metadata, community="generic")
    print(created_record.id)
    print(created_record.links.self_html)

    # upload a file to the dataset from a memory
    m = MemorySource(
        b"Hello, this is a test file.",
        content_type="text/plain",
    )
    client.files.upload(created_record, "test.txt", {"title": "A sample text file"}, m)


if __name__ == "__main__":
    main()
