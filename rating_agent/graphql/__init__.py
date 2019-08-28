import graphene  # type: ignore

from .agent import (
    authorization,
    beginTransaction,
    endTransaction,
    rollbackTransaction,
    recordTransaction,
)


class Mutations(graphene.ObjectType):
    authorization = authorization.Field(name="authorization")
    beginTransaction = beginTransaction.Field(name="beginTransaction")
    endTransaction = endTransaction.Field(name="endTransaction")
    rollbackTransaction = rollbackTransaction.Field(name="rollbackTransaction")
    recordTransaction = recordTransaction.Field(name="recordTransaction")


schema = graphene.Schema(mutation=Mutations, auto_camelcase=False)
