from fastapi import APIRouter, Depends

from ..schema import agent as schema
from ..services import agent as service
from ..services import bus

router = APIRouter()


@router.post("/authorization")
async def authorization(
    request: schema.AuthorizationRequest, bus: bus.BusService = Depends(bus.get),
) -> schema.AuthorizationResponse:
    response = await service.authorization(request, bus)
    return response


@router.post("/begin_transaction")
async def begin_transaction(
    request: schema.BeginTransactionRequest, bus: bus.BusService = Depends(bus.get),
) -> schema.BeginTransactionResponse:
    response = await service.begin_transaction(request, bus)
    return response


@router.post("/end_transaction")
async def end_transaction(
    request: schema.EndTransactionRequest, bus: bus.BusService = Depends(bus.get),
) -> schema.EndTransactionResponse:
    response = await service.end_transaction(request, bus)
    return response


@router.post("/rollback_transaction")
async def rollback_transaction(
    request: schema.RollbackTransactionRequest, bus: bus.BusService = Depends(bus.get),
) -> schema.RollbackTransactionResponse:
    response = await service.rollback_transaction(request, bus)
    return response


@router.post("/record_transaction")
async def record_transaction(
    request: schema.RecordTransactionRequest, bus: bus.BusService = Depends(bus.get),
) -> schema.RecordTransactionResponse:
    response = await service.record_transaction(request, bus)
    return response
