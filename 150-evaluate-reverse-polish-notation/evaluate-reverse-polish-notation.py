class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:   #tokens = ["2","1","+","3","*"]
            if token in ['+','-','*','/']:
                b = stack.pop()  
                a = stack.pop()   
                
                if token == '+':
                    res = a + b
                elif token == '-':
                    res = a - b
                elif token == '*':
                    res = a * b
                elif token == '/':
                    res = int(a / b)
                stack.append(res)
                
            else:
                stack.append(int(token))

        return stack[0]

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = []
#         for token in tokens:
#             if token in ["+","-","/","*"]:
#                 b = stack.pop()
#                 a = stack.pop()
#                 if token == "+":
#                     res = a+b
#                 elif token == "*":
#                     res = a*b
#                 elif token == "/":
#                     res = int(a/b)
#                 elif token == "-":
#                     res = a-b
#                 stack.append(res)
#             else:
#                 stack.append(int(token))
#         return stack[0]