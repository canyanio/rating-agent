import graphene  # type: ignore

from .agent import (
    authorization,
    beginTransaction,
    endTransaction,
    rollbackTransaction,
    recordTransaction,
)


class Query(graphene.ObjectType):
    version = graphene.Int()

    def resolve_version(self, *args, **kw):
        return 1


class Mutations(graphene.ObjectType):
    authorization = authorization.Field(name="authorization")
    beginTransaction = beginTransaction.Field(name="beginTransaction")
    endTransaction = endTransaction.Field(name="endTransaction")
    rollbackTransaction = rollbackTransaction.Field(name="rollbackTransaction")
    recordTransaction = recordTransaction.Field(name="recordTransaction")


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)
