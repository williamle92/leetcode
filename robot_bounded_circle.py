'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.
Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.
Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.
 

Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
'''


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
#         We create two coordinates, one for direction and one for position
#       we set the position to north bcause that is its position initially
        dirX, dirY = (0,1)
        x,y = (0,0)
        
        for instruction in instructions:
#             If it is G, then we + 1 in the direction it is facing, note direction never goes above 1

            if instruction == "G":
                x, y = (dirX + x, dirY + y)
            
            elif instruction == "L":
#                 Now we are going to turn the direction left which means that the X and Y will invert and we multiply the X coordinate by -1
#                 e.g. from starting (0,1) -> (-1,0) -> (0,-1), (1, 0) -> (0, 1)
                
                dirX, dirY = (-1 * dirY, dirX)
            else:
                dirX, dirY = (dirY, -1*dirX)
        
#         two conditions we are checking for since this is running in a loop forever, one is when it returns to the same initial position at the end or when it ends, the direction is not faced the same direction it started from. If the direction is not facing the same, it will eventually return to the initial position after running forever, but if its direction is the same as its initial position throughout then it will keep on going. 
        return (x,y) == (0,0) or (dirX,dirY) != (0,1)
                