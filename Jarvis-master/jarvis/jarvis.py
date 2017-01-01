import logging

logger = logging.getLogger(__name__)


class Jarvis(object):

    # Built-in words
    JARVIS_COGNATES = ["jarvis", "gervais", "travis", "tervis", "service"]

    STOP_LISTENING_COGNATES = ["go away", "stop listening", "shut down"]

    @classmethod
    def is_actionable_command(cls, command):
        return any(cognate in command for cognate in cls.JARVIS_COGNATES)

    @classmethod
    def handle_action(cls, command, **kwargs):
        """
        Handles a single text command.
        """

        # Use lowercase for processing.
        command = command.lower()

        logger.debug("Received command: '%s'", command)

        # Determine if this is an actionable command.
        if not cls.is_actionable_command(command):
            return

        if any(cognate in command for cognate in cls.STOP_LISTENING_COGNATES):
            logger.info("Thank you, enjoy your day, sir.")
        else:
            logger.info("Yes sir?")