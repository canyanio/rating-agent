from enum import Enum


class MessageQueueName(Enum):
    RATER = "rater"


class MethodName(Enum):
    AUTHORIZATION = "authorization"
    BEGIN_TRANSACTION = "begin_transaction"
    END_TRANSACTION = "end_transaction"
    ROLLBACK_TRANSACTION = "rollback_transaction"
    RECORD_TRANSACTION = "record_transaction"


class MessagePriority(Enum):
    LOWEST = 10
    LOW = 20
    MEDIUM = 30
    HIGH = 40
    HIGHEST = 50
