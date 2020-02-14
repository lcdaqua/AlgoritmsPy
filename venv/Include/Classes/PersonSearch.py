from collections import deque

graph = {}
graph ["you"] = ["alice", "bob", "claire"]
graph ["bob"] = ["anuj", "peggy"]
graph ["alice"] = ["peggy"]
graph ["claire"] = ["thom", "jhony"]
graph ["thom"] = []
graph ["jhony"] = []
graph ["peggy"] = []
graph ["anuj"] = []

def search(name):
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print("Проверка " + person)
        if not person in searched:
            if person_is_seller(person):
                print(person + " is mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

def person_is_seller(name):
    return name[-1] == 'm'
