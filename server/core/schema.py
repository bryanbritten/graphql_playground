import graphene
from authors.schema import Query as AuthorQuery
from authors.schema import Mutation as AuthorMutation
from books.schema import Query as BookQuery
from books.schema import Mutation as BookMutation

class Query(BookQuery, AuthorQuery):
    pass

class Mutation(BookMutation, AuthorMutation):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)