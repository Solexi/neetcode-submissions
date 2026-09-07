"""
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [j.end for j in intervals]
        rooms = len(starts)

        if intervals == []:
            return 0
        if len(intervals) == 1:
            return 1

        starts.sort()
        ends.sort()


        e = 0
        for s in range(len(starts)):
            if starts[s] >= ends[e]:
                rooms -= 1
                e += 1
        
        print(rooms)
        return rooms
