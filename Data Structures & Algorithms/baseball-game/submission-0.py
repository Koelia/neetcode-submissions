class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []
        for op in operations:
            if op == "+":
                score.append(score[-1] + score[-2]) #in arrays -1, -2, start from the end
            elif op == "C":
                score.pop()
            elif op == "D":
                score.append(2 * score[-1])
            else:
                score.append(int(op))
        
        return sum(score)