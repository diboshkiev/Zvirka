from collections import namedtuple
from configparser import ConfigParser

# instantiate config
config = ConfigParser()
# parse existing file
config.read('settings.ini')

# read values from a section [general_settings]
input_polk = config.get('general_settings', 'input_polk')
sheet_polk = config.get('general_settings', 'sheet_polk')
header_row_polk = config.getint('general_settings', 'header_row_polk')


input_4bo = config.get('general_settings', 'input_4bo')
sheet_4bo = config.get('general_settings', 'sheet_4bo')
header_row_4bo = config.getint('general_settings', 'header_row_4bo')

use_cols_polk = config.get('general_settings', 'use_cols_polk')

use_cols_4bo = config.get('general_settings', 'use_cols_4bo')

use_cols_polk_names = config.get('general_settings', 'use_cols_polk_names').split()
use_cols_4bo_names = config.get('general_settings', 'use_cols_4bo_names').split()

general_settings_factory = namedtuple('general_settings', 'input_polk sheet_polk header_row_polk '
                                                          'use_cols_polk input_4bo sheet_4bo header_row_4bo '
                                                          'use_cols_4bo use_cols_polk_names use_cols_4bo_names')
general_settings = general_settings_factory(input_polk, sheet_polk, header_row_polk, use_cols_polk,
                                            input_4bo, sheet_4bo, header_row_4bo, use_cols_4bo,
                                            use_cols_polk_names, use_cols_4bo_names)



