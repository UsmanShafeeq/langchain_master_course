def calculator(expr):
    return eval(expr)

def search_tool(query):
    return f"Searching knowledge base for: {query}"

tools = {
    "calc": calculator,
    "search": search_tool
}

cmd = input("Tool (calc/search): ")

if cmd == "calc":
    expr = input("Expression: ")
    print(tools["calc"](expr))

elif cmd == "search":
    q = input("Query: ")
    print(tools["search"](q))