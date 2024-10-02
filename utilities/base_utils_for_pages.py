from enum import Enum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseUtilsForPages:
    class WaitConditionTypes(Enum):
        VISIBLE = 1
        CLICKABLE = 2
        PRESENCE = 3
        STALENESS = 4
        INVISIBLE = 5
        VISIBLE_ALL = 6
        PRESENCE_ALL = 7

    def wait_for_element(self, locator, wait_type):
        if wait_type == BaseUtilsForPages.WaitConditionTypes.VISIBLE:
            pass
        elif wait_type == BaseUtilsForPages.WaitConditionTypes.CLICKABLE:
            pass
        elif wait_type == BaseUtilsForPages.WaitConditionTypes.PRESENCE:
            pass
        elif wait_type == BaseUtilsForPages.WaitConditionTypes.STALENESS:
            pass
        elif wait_type == BaseUtilsForPages.WaitConditionTypes.INVISIBLE:
            pass
        elif wait_type == BaseUtilsForPages.WaitConditionTypes.VISIBLE_ALL:
            pass
        elif wait_type == BaseUtilsForPages.WaitConditionTypes.PRESENCE_ALL:
            pass
