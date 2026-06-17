from graphs import graph

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    response = graph.agent.invoke(
        {
            "messages": [
                {"role":"system","content":"you are helpful assiatent which have access to some tools"
                                           "if user ask general question feel free to reply in helpful manner but if "
                                           "user ask any question and there are tool avavilable for that then use that tool "
                                           "also print tool name used explicitly and also print the answer"},

                {
                    "role": "user",
                    "content": query
                }
            ]
        }
    )

    print(
        "\nAgent:",
        response["messages"][-1].content
    )