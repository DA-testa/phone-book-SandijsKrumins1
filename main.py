# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = {}
    for c_query in queries:
        if c_query.type == "add":
           contacts[c_query.number] = c_query.name
        elif c_query.type == "del":
            if c_query.number in contacts:
                del contacts[c_query.number]
        elif c_query.type == "find":
            name = contacts.get(c_query.number, "not found")
            result.append(name)
            

    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

