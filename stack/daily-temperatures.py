def dailyTemperatures(temperatures):
        stack = []
        answer = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackVal, stackInd = stack.pop()
                answer[stackInd] = i - stackInd
            stack.append([t, i])
        return answer