from graphene import ObjectType, String, Schema
class Query(ObjectType):
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya'

schema = Schema(query=Query)

query_string = '{hello}'
result = schema.execute(query_string)
print(result.data['hello'])

query_with_argument = '{hello(name:"Jairo")}'
result = schema.execute(query_with_argument)
print(result.data['hello'])

query_goodbye = '{goodbye}'
result = schema.execute(query_goodbye)
print(result.data['goodbye'])