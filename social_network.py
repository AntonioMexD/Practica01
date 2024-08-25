# social_network.py

from union_find import UnionFind

def process_events(events, num_users):
    uf = UnionFind(num_users)
    results = []

    for user1, user2 in events:
        uf.union(user1, user2)
        results.append(uf.get_group_count())

    return results

def handle_social_network():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    index = 0
    while index < len(data):
        num_events = int(data[index])
        if num_events == 0:
            break

        events = []
        num_users = 0

        for i in range(1, num_events + 1):
            user1, user2 = map(int, data[index + i].split())
            num_users = max(num_users, user1 + 1, user2 + 1)
            events.append((user1, user2))

        results = process_events(events, num_users)
        for result in results:
            print(result)

        index += num_events + 1
