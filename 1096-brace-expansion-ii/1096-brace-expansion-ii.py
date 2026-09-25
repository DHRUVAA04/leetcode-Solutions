class Solution:
    def braceExpansionII(self, expression):

        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    part, i = parse(i + 1)
                else:
                    part = {expression[i]}
                    i += 1

                new_current = set()

                for a in current:
                    for b in part:
                        new_current.add(a + b)

                current = new_current

                if i < len(expression) and expression[i] == ',':
                    result.update(current)
                    current = {""}
                    i += 1

            result.update(current)

            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)