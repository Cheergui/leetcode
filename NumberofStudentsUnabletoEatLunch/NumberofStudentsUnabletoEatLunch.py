from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """

        queue_students = deque(students)
        queue_sandwiches = deque(sandwiches)

        while queue_sandwiches:
            if len(set(queue_students)) == 1:
                if queue_students[0] != queue_sandwiches[0]:
                    break
            if queue_students[0] == queue_sandwiches[0]:
                queue_students.popleft()
                queue_sandwiches.popleft()
            else:
                queue_students.append(queue_students.popleft())
        
        return len(queue_students)