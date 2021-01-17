import logging
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
        logger.info(f"encoding Base64: {str}")
    def decode(self, str):
        logger.info(f"decoding Base64: {str}")

class ASCCIStrategy(EncoderStrategy):
    def encode(self, str):
        logger.info(f"encoding ascci: {str}")
    def decode(self, str):
        logger.info(f"decoding ascci: {str}")
