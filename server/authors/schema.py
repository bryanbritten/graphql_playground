import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorInput(graphene.InputObjectType):
    author_name = graphene.String()
    year_born = graphene.String()
    year_died = graphene.String()
    country = graphene.String()
    books_written = graphene.Int()

class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, author_name=graphene.String())

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_author(self, info, author_name):
        return Author.objects.get(pk=author_name)

class CreateAuthor(graphene.Mutation):
    class Arguments:
        author_data = AuthorInput(required=True)
    
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, author_data=None):
        author_instance = Author(
            author_name = author_data.author_name,
            year_born = author_data.year_born,
            year_died = author_data.year_died,
            country = author_data.country,
            books_written = author_data.books_written
        )
        author_instance.save()
        
        return CreateAuthor(author=author_instance)

class UpdateAuthor(graphene.Mutation):
    class Arguments:
        author_data = AuthorInput(required=True)
    
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, author_data=None):
        author_instance = Author.objects.get(pk=author_data.name)

        if author_instance:
            author_instance.author_name = author_data.author_name
            author_instance.year_born = author_data.year_born
            author_instance.year_died = author_data.year_died
            author_instance.country = author_data.country
            author_instance.books_written = author_data.books_written

            return UpdateAuthor(author=author_instance)
        return UpdateAuthor(author=None)

class DeleteAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
    
    author = graphene.Field(AuthorType)

    @staticmethod
    def mutate(root, info, id):
        author_instance = Author.objects.get(pk=id)
        author_instance.delete()

        return None

class Mutation(graphene.ObjectType):
        create_author = CreateAuthor.Field()
        update_author = UpdateAuthor.Field()
        delete_author = DeleteAuthor.Field()
