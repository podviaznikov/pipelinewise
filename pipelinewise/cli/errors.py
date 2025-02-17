class BinaryExecutableNotFound(Exception):
    """Raised if binary executable not found"""

    def __init__(self, bin_path):
        msg = f'{bin_path} not found.'
        super().__init__(msg)


class StreamBufferTooLargeException(Exception):
    """Raised if stream buffer size is greater than the max allowed size"""

    def __init__(self, buffer_size, max_buffer_size):
        msg = (
            f'{buffer_size}M buffer size is too large. The maximum allowed stream buffer size is '
            f'{max_buffer_size}M'
        )
        super().__init__(msg)


class InvalidTransformationException(Exception):
    """Raised if invalid transformation config is found"""


class DuplicateConfigException(Exception):
    """Raised if a duplicate tap/target config is found"""


class InvalidConfigException(Exception):
    """Raised if an invalid config is found"""
