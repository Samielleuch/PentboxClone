import logging
import base64
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class EncoderStrategy(ABC):
    """
    interface that defines the way the encoding is done
    """

    @abstractmethod
    def encode(self, string):
        """
        encode
        """
        pass

    @abstractmethod
    def decode(self, string):
        """
        decode
        """
        pass



class Base64Strategy(EncoderStrategy):
    def encode(self, str):
        logger.info(f"\n encoding Base64: {str}")
        message_bytes = str.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        logger.info(f"\n encoded value: {base64_message}")

    def decode(self, str):
        logger.info(f"\n decoding Base64 :{str}")
        message_bytes = str.encode('ascii')
        base64_bytes = base64.b64decode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        logger.info(f"\n decoded value : {base64_message}")


class ASCCIStrategy(EncoderStrategy):
    def encode(self, str):
        logger.info(f"\n encoding ascci: {str}")
        message_bytes = str.encode('ascii')
        logger.info(f"\n encoded value: {message_bytes}")

    def decode(self, str):
        logger.info(f"\n decoding ascci: {str}")
        message_bytes = str.decode('ascii')
        logger.info(f"\n encoded value: {message_bytes}")
