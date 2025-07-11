import logging
from yaml import load, FullLoader
import os
from bcutils.bc_utils import (
    create_bc_session,
    get_barchart_downloads,
    update_barchart_downloads,
)

logging.basicConfig(level=logging.INFO)
HOME_PATH = os.path.expanduser("~")
CONFIG_FILE = os.path.join(HOME_PATH,"pst/pysystemtrade-private/private/private_config.yaml")

def download_with_config():
    # run a download session, with config picked up from the passed file
    # See /sample/private_config_sample.yaml
    config = load_config(CONFIG_FILE)
    print("Config file loaded: ", config)
    get_barchart_downloads(
        create_bc_session(config),
        instr_list=config["barchart_download_list"],
        start_year=config["barchart_start_year"],
        end_year=config["barchart_end_year"],
        save_dir=config["barchart_path"],
        do_daily=config["barchart_do_daily"],
        dry_run=config["barchart_dry_run"],
        default_day_count=config["barchart_default_day_count"],
    )


def update_with_config():
    # run an update session, with config picked up from the passed file
    # See /sample/private_config_sample.yaml
    config = load_config(CONFIG_FILE)
    instr_list = config["barchart_update_list"]
    save_dir = config["barchart_path"]
    dry_run = config["barchart_dry_run"]
    for code in instr_list:
        update_barchart_downloads(instr_code=code, save_dir=save_dir, dry_run=dry_run)


def load_config(config_path):
    config_stream = open(config_path, "r")
    return load(config_stream, Loader=FullLoader)


if __name__ == "__main__":
    download_with_config()
    # update_with_config()
