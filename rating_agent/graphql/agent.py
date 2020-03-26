import graphene  # type: ignore

from datetime import datetime

from graphene.types.resolver import dict_resolver  # type: ignore

from ..services import agent as service
from ..services import bus as bus_service
from ..schema import agent as schema
from .types import BigInt


class AuthorizationResponse(graphene.ObjectType):
    """Authorization response"""

    tenant = graphene.ID(default_value='default')
    transaction_tag = graphene.String(required=True)
    account_tag = graphene.String()
    destination_account_tag = graphene.String()
    authorized = graphene.Boolean()
    authorized_destination = graphene.Boolean()
    unauthorized_account_tag = graphene.String()
    unauthorized_account_reason = graphene.String()
    unauthorized_destination_reason = graphene.String()
    max_available_units = graphene.Int()
    balance = BigInt()
    carriers = graphene.List(graphene.String)


class authorization(graphene.Mutation):
    """Authorization request"""

    class Arguments:
        tenant = graphene.ID(default_value='default')
        transaction_tag = graphene.String(required=True)
        account_tag = graphene.String()
        destination_account_tag = graphene.String()
        source = graphene.String()
        destination = graphene.String()
        timestamp_auth = graphene.DateTime()

    class Meta:
        default_resolver = dict_resolver

    Output = AuthorizationResponse

    async def mutate(
        self,
        info,
        tenant: str = 'default',
        transaction_tag: str = None,
        account_tag: str = None,
        destination_account_tag: str = None,
        source: str = None,
        destination: str = None,
        timestamp_auth: datetime = None,
    ) -> schema.AuthorizationResponse:
        bus = bus_service.get(info.context["request"])
        request = schema.AuthorizationRequest(
            tenant=tenant,
            transaction_tag=transaction_tag,
            account_tag=account_tag,
            destination_account_tag=destination_account_tag,
            source=source,
            destination=destination,
            timestamp_auth=timestamp_auth,
        )
        return await service.authorization(request, bus)


class BeginTransactionResponse(graphene.ObjectType):
    """Begin transaction response"""

    ok = graphene.Boolean()
    tenant = graphene.ID(default_value='default')
    transaction_tag = graphene.String(required=True)
    account_tag = graphene.String()
    destination_account_tag = graphene.String()


class beginTransaction(graphene.Mutation):
    """Begin transaction request"""

    class Arguments:
        tenant = graphene.ID(default_value='default')
        transaction_tag = graphene.String(required=True)
        account_tag = graphene.String()
        destination_account_tag = graphene.String()
        source = graphene.String()
        destination = graphene.String()
        timestamp_begin = graphene.DateTime()

    class Meta:
        default_resolver = dict_resolver

    Output = BeginTransactionResponse

    async def mutate(
        self,
        info,
        tenant: str = 'default',
        transaction_tag: str = None,
        account_tag: str = None,
        destination_account_tag: str = None,
        source: str = None,
        destination: str = None,
        timestamp_begin: datetime = None,
    ) -> schema.BeginTransactionResponse:
        bus = bus_service.get(info.context["request"])
        request = schema.BeginTransactionRequest(
            tenant=tenant,
            transaction_tag=transaction_tag,
            account_tag=account_tag,
            destination_account_tag=destination_account_tag,
            source=source,
            destination=destination,
            timestamp_begin=timestamp_begin,
        )
        return await service.begin_transaction(request, bus)


class EndTransactionResponse(graphene.ObjectType):
    """End transaction response"""

    ok = graphene.Boolean()
    tenant = graphene.ID(default_value='default')
    transaction_tag = graphene.String(required=True)
    account_tag = graphene.String()
    destination_account_tag = graphene.String()


class endTransaction(graphene.Mutation):
    """End transaction request"""

    class Arguments:
        tenant = graphene.ID(default_value='default')
        transaction_tag = graphene.String(required=True)
        account_tag = graphene.String()
        destination_account_tag = graphene.String()
        timestamp_end = graphene.DateTime()

    class Meta:
        default_resolver = dict_resolver

    Output = EndTransactionResponse

    async def mutate(
        self,
        info,
        tenant: str = 'default',
        transaction_tag: str = None,
        account_tag: str = None,
        destination_account_tag: str = None,
        timestamp_end: datetime = None,
    ) -> schema.EndTransactionResponse:
        bus = bus_service.get(info.context["request"])
        request = schema.EndTransactionRequest(
            tenant=tenant,
            transaction_tag=transaction_tag,
            account_tag=account_tag,
            destination_account_tag=destination_account_tag,
            timestamp_end=timestamp_end,
        )
        return await service.end_transaction(request, bus)


class RollbackTransactionResponse(graphene.ObjectType):
    """Rollback transaction response"""

    ok = graphene.Boolean()
    tenant = graphene.ID(default_value='default')
    transaction_tag = graphene.String(required=True)
    account_tag = graphene.String()
    destination_account_tag = graphene.String()


class rollbackTransaction(graphene.Mutation):
    """Rollback transaction request"""

    class Arguments:
        tenant = graphene.ID(default_value='default')
        transaction_tag = graphene.String(required=True)
        account_tag = graphene.String()
        destination_account_tag = graphene.String()

    class Meta:
        default_resolver = dict_resolver

    Output = RollbackTransactionResponse

    async def mutate(
        self,
        info,
        tenant: str = 'default',
        transaction_tag: str = None,
        account_tag: str = None,
        destination_account_tag: str = None,
    ) -> schema.RollbackTransactionResponse:
        bus = bus_service.get(info.context["request"])
        request = schema.RollbackTransactionRequest(
            tenant=tenant,
            transaction_tag=transaction_tag,
            account_tag=account_tag,
            destination_account_tag=destination_account_tag,
        )
        return await service.rollback_transaction(request, bus)


class RecordTransactionResponse(graphene.ObjectType):
    """Record transaction response"""

    ok = graphene.Boolean()
    tenant = graphene.ID(default_value='default')
    transaction_tag = graphene.String(required=True)
    account_tag = graphene.String()
    destination_account_tag = graphene.String()


class recordTransaction(graphene.Mutation):
    """Record transaction request"""

    class Arguments:
        tenant = graphene.ID(default_value='default')
        transaction_tag = graphene.String(required=True)
        account_tag = graphene.String()
        destination_account_tag = graphene.String()
        source = graphene.String()
        destination = graphene.String()
        timestamp_auth = graphene.DateTime()
        timestamp_begin = graphene.DateTime()
        timestamp_end = graphene.DateTime()
        failed = graphene.Boolean()
        failed_reason = graphene.String()

    class Meta:
        default_resolver = dict_resolver

    Output = RecordTransactionResponse

    async def mutate(
        self,
        info,
        tenant: str = 'default',
        transaction_tag: str = None,
        account_tag: str = None,
        destination_account_tag: str = None,
        source: str = None,
        destination: str = None,
        timestamp_auth: datetime = None,
        timestamp_begin: datetime = None,
        timestamp_end: datetime = None,
        failed: bool = False,
        failed_reason: str = None,
    ) -> schema.RecordTransactionResponse:
        bus = bus_service.get(info.context["request"])
        request = schema.RecordTransactionRequest(
            tenant=tenant,
            transaction_tag=transaction_tag,
            account_tag=account_tag,
            destination_account_tag=destination_account_tag,
            source=source,
            destination=destination,
            timestamp_auth=timestamp_auth,
            timestamp_begin=timestamp_auth,
            timestamp_end=timestamp_auth,
            failed=failed,
            failed_reason=failed_reason,
        )
        return await service.record_transaction(request, bus)
