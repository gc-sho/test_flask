import os
from gc_test_flask import logger

def write_file(data, file_path):
    '''
    Writes certain data to temporary file
    :param data: String of data
    :param file_path: Path to a temporary file
    :returns: Content written to the file
    '''
    try:
        f = open(file_path, 'w+')
        f.write(data)
        f.close()
    except (IOError, OSError) as e:
        logger.exception(e)
        return None, 'Error occured, restart App'

    return data, None

def remove_file(file_list):
    '''
    Removes a temporary file from the host
    :param file_list: List of file paths to delete
    :returns: Boolean
    '''
    try:
        for file in file_list:
            if os.path.isfile(file):
                os.remove(file)
    except (IOError, OSError) as e:
        logger.exception(e)
        return None, 'Error occured, restart App'

    return True, None

def read_file(file_path):
    '''
    Reads from temporary file
    :param file_path: Path to a file
    :returns: Content of the file
    '''
    try:
        # Check if the file exists
        if os.path.isfile(file_path):
            f = open(file_path, 'r')
            # Check if we did really open the file
            if f.mode == 'r':
                contents = f.read()
                f.close()

                return contents, None
        else:
            return None, 'You are not logged in'
    except (IOError, OSError) as e:
        logger.exception(e)
        return None, 'Error occured, restart App'