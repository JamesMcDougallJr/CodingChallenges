import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        print("Read {0} from {1}".format(len(response.content), url))


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print("Downloaded {0} in {1} seconds".format(len(sites), duration))
