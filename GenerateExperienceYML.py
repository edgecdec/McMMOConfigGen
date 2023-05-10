import os
from Constants.ExperienceConstants import *
from Util import *


def create_experience_config():
    yaml = create_yaml_str_from_dir(EXPERIENCE_TEMPLATE_DIR_PATH)[1:]
    write_obj_to_file(yaml, EXPERIENCE_MCMMO_FILE_PATH)

