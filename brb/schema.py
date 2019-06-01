import graphene

import brb.scores.schema


class Query(brb.scores.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(graphene.ObjectType):
    create_score_card = brb.scores.schema.ScoreCardMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
