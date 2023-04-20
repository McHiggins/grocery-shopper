import offer_finder
import yaml


# loading configuration file
def configloader(path: str):
    """
    This function will load the config file from a given path.
    :param path:
    :return:
    """
    with open(path) as cfg:
        config = yaml.load(cfg, Loader=yaml.FullLoader)
    return config["offer_finder"]


def download_offers(cfg: dict):
    """
    This function will pass the cfg file and start the offer_finder.data_downloader() to
    scrape and download the weekly offers of edeka and penny.
    :param cfg:
    :return:
    """
    offers = offer_finder.data_downloader(cfg)
    return offers


def compare_reader(cfg: dict):
    """
    This function will pass the cfg file and start the offer_finder.reader() to compare the
    standard-einkauf.csv with the penny and edeka offers.
    It will return and write down the dataframe with the matching items.

    :param cfg:
    :return:
    """
    matching_offers = offer_finder.reader(cfg)
    return matching_offers


if __name__ == "__main__":
    cfg_file = configloader(path="../data/config/config_higgins.yaml")
    offers = download_offers(cfg=cfg_file)
    compare_reader = compare_reader(cfg_file)
