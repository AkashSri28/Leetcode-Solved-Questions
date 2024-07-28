class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Build the graph using adjacency list representation
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Priority queue to track (current_time, current_vertex, number_of_times_visited)
        pq = [(0, 1, 0)]

        # Keep track of the first and second minimum times to reach each vertex
        first = [float('inf')] * (n + 1)
        second = [float('inf')] * (n + 1)
        first[1] = 0

        while pq:
            current_time, u, count = heapq.heappop(pq)

            # If we reached the nth vertex for the second time, return the time
            if u == n and count == 1:
                return current_time

            # Determine the waiting time at the current vertex based on signal timing
            if (current_time // change) % 2 == 1:  # If the signal is red
                current_time = (current_time // change + 1) * change

            for v in graph[u]:
                next_time = current_time + time

                # If we find a shorter time to reach v, update first and push to pq
                if next_time < first[v]:
                    first[v], next_time = next_time, first[v]
                    heapq.heappush(pq, (first[v], v, 0))

                # If we find a second shorter time to reach v, update second and push to pq
                if first[v] < next_time < second[v]:
                    second[v] = next_time
                    heapq.heappush(pq, (second[v], v, 1))

        # If we exhaust the queue and don't find a valid second minimum path
        return -1
