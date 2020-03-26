from ..enums import MethodName
from ..schema import agent as schema
from ..services import bus as bus_service


RPC_CALL_EXPIRATION = 10


async def authorization(
    request: schema.AuthorizationRequest, bus: bus_service.BusService
) -> schema.AuthorizationResponse:
    response = (
        await bus.rpc_call(
            method=MethodName.AUTHORIZATION.value,
            expiration=RPC_CALL_EXPIRATION,
            kwargs={'request': request.dict()},
        )
        or {}
    )
    return schema.AuthorizationResponse(
        tenant=request.tenant,
        transaction_tag=request.transaction_tag,
        account_tag=request.account_tag,
        destination_account_tag=request.destination_account_tag,
        **response
    )


async def begin_transaction(
    request: schema.BeginTransactionRequest, bus: bus_service.BusService
) -> schema.BeginTransactionResponse:
    response = (
        await bus.rpc_call(
            method=MethodName.BEGIN_TRANSACTION.value,
            expiration=RPC_CALL_EXPIRATION,
            kwargs={'request': request.dict()},
        )
        or {}
    )
    return schema.BeginTransactionResponse(
        tenant=request.tenant,
        transaction_tag=request.transaction_tag,
        account_tag=request.account_tag,
        destination_account_tag=request.destination_account_tag,
        **response
    )


async def end_transaction(
    request: schema.EndTransactionRequest, bus: bus_service.BusService
) -> schema.EndTransactionResponse:
    response = (
        await bus.rpc_call(
            method=MethodName.END_TRANSACTION.value,
            expiration=RPC_CALL_EXPIRATION,
            kwargs={'request': request.dict()},
        )
        or {}
    )
    return schema.EndTransactionResponse(
        tenant=request.tenant,
        transaction_tag=request.transaction_tag,
        account_tag=request.account_tag,
        destination_account_tag=request.destination_account_tag,
        **response
    )


async def rollback_transaction(
    request: schema.RollbackTransactionRequest, bus: bus_service.BusService
) -> schema.RollbackTransactionResponse:
    response = (
        await bus.rpc_call(
            method=MethodName.ROLLBACK_TRANSACTION.value,
            expiration=RPC_CALL_EXPIRATION,
            kwargs={'request': request.dict()},
        )
        or {}
    )
    return schema.RollbackTransactionResponse(
        tenant=request.tenant,
        transaction_tag=request.transaction_tag,
        account_tag=request.account_tag,
        destination_account_tag=request.destination_account_tag,
        **response
    )


async def record_transaction(
    request: schema.RecordTransactionRequest, bus: bus_service.BusService
) -> schema.RecordTransactionResponse:
    response = (
        await bus.rpc_call(
            method=MethodName.RECORD_TRANSACTION.value,
            expiration=RPC_CALL_EXPIRATION,
            kwargs={'request': request.dict()},
        )
        or {}
    )
    return schema.RecordTransactionResponse(
        tenant=request.tenant,
        transaction_tag=request.transaction_tag,
        account_tag=request.account_tag,
        destination_account_tag=request.destination_account_tag,
        **response
    )
