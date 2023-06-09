# Keys and Rooms
#Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        currentKeys = [0]
        tempKeys = []

        while(len(visited) != len(rooms)):
            
            tempVisited = visited.copy()

            #visit all the rooms for the keys that we just gained
            for i in currentKeys:
                for key in rooms[i]:
                    tempKeys.append(key)
                
                visited.add(i)
            
            #We didnt add anymore keys so there are rooms we cant reach
            if(len(tempVisited) == len(visited)):
                return False

            #add the new gains we just got to be visited in next while loop iteration
            currentKeys = tempKeys
            tempKeys = []

        return True


# Create an instance of the Solution class
solution = Solution()

# Example usage
rooms = [[1,3],[3,0,1],[2],[0]]
visited_all_rooms = solution.canVisitAllRooms(rooms)
print(visited_all_rooms)
