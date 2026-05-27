from enum import Enum

from utils.utils import utils


class ItemTypes(Enum):
    PIPELINE = "Pipeline"
    FREESTYLE_PROJECT = "Freestyle project"
    MULTI_CONFIGURATION_PROJECT = "Multi-configuration project"
    FOLDER = "Folder"
    MULTIBRANCH_PIPELINE = "Multibranch Pipeline"
    ORGANIZATION_FOLDER = "Organization Folder"


# case_01 = {
#     "name": utils.faker_en.word(),
#     "description": utils.faker_en.word(),
#     "type": ItemTypes.PIPELINE.value,
# }
#
# case_02 = {
#     "name": utils.faker_en.word(),
#     "description": utils.faker_en.word(),
#     "type": ItemTypes.FREESTYLE_PROJECT.value,
# }
#
# case_03 = {
#     "name": utils.faker_en.word(),
#     "description": utils.faker_en.word(),
#     "type": ItemTypes.MULTI_CONFIGURATION_PROJECT.value,
# }
#
# case_04 = {
#     "name": utils.faker_en.word(),
#     "description": utils.faker_en.word(),
#     "type": ItemTypes.FOLDER.value,
# }
#
# case_05 = {
#     "name": utils.faker_en.word(),
#     "description": utils.faker_en.word(),
#     "type": ItemTypes.MULTIBRANCH_PIPELINE.value,
# }
#
# case_06 = {
#     "name": utils.faker_en.word(),
#     "description": utils.faker_en.word(),
#     "type": ItemTypes.ORGANIZATION_FOLDER.value,
# }
#
#
# test_cases = [case_01, case_02, case_03, case_04, case_05, case_06]
#

test_cases = [
    {
        "name": utils.faker_en.word(),
        "description": utils.faker_en.word(),
        "type": item_type,
    }
    for item_type in ItemTypes
]
