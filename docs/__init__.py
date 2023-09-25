import logging
import re

from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.event_bus import EventBus, Event
from aries_cloudagent.core.profile import Profile
from aries_cloudagent.core.protocol_registry import ProtocolRegistry
from ..plugins.acapy_plugin_qa.acapy_plugin_qa.v1_0.handlers.question_handler import QuestionHandler
from ..plugins.acapy_plugin_qa.acapy_plugin_qa.v1_0.message_types import MESSAGE_TYPES
from ..plugins.acapy_plugin_qa.acapy_plugin_qa.v1_0.models.qa_exchange_record import QAExchangeRecord, QAExchangeRecordSchema

LOGGER = logging.getLogger(__name__)

async def setup(context: InjectionContext):
    """Register to handle events."""
    LOGGER.info("> qa plugin setup...")
    protocol_registry = context.inject(ProtocolRegistry)
    assert protocol_registry

    protocol_registry.register_message_types(MESSAGE_TYPES)

    event_bus = context.inject(EventBus)
    if not event_bus:
        raise ValueError("EventBus missing in context")
    
    event_bus.subscribe(
        re.compile(
            f"^{QAExchangeRecord.EVENT_NAMESPACE}::"
            f"{QAExchangeRecord.RECORD_TOPIC}::.*$"
        ),
        qa_msg_event_handler,
    )
    LOGGER.info("> qa plugin setup...")

def qa_msg_event_handler(profile: Profile, event: Event):
    LOGGER.info("> qa plugin qa_msg_event_handler")
    LOGGER.debug(event.payload)

    msg: QAExchangeRecord = QAExchangeRecord.deserialize(event.payload)
    if msg.role == QAExchangeRecord.ROLE_RESPONDER:
        LOGGER.info(" it is for role responder i.e. rcvd a question")
    elif msg.role == QAExchangeRecord.ROLE_QUESTIONER:
        LOGGER.info(" it is for role QUESTIONER i.e. rcvd answer? ")



