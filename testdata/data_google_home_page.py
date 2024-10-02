from utilities.base_config_utils import BaseConfig


class DataGoogleHomePage:
    json_data = BaseConfig.get_data_from_json(BaseConfig.get_project_root() + "\\testdata\\Google Search Data.json")

    home_page_data = []

    for key, value in json_data.items():
        home_page_data.append({key: value})

