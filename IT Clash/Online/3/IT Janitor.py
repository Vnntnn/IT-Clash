class Stairs:
    def __init__(self, n):
        """Initializing class"""
        self.n = n
        self.memo = {0: 1, 1: 1}
        self.sequence_steps = {0: [], 1: [1]}

    def count_ways(self):
        """Find ways to get best stairs and store steps"""
        def fib(n):
            if n in self.memo:
                return self.memo[n], self.sequence_steps[n]

            fibo_size = min(500, n//2 + 1)

            a, seq_a = fib(n - fibo_size)
            b, seq_b = fib(n - fibo_size + 1)

            def calc_next(a, b, steps_left, current_seq):
                if steps_left == 0:
                    return b, current_seq
                new_step = 1 if len(current_seq) == 0 or current_seq[-1] == 2 else 2
                return calc_next(b, a + b, steps_left - 1, current_seq + [new_step])

            result, result_seq = calc_next(a, b, fibo_size - 1, seq_a + seq_b)
            self.memo[n] = result
            self.sequence_steps[n] = result_seq
            return result, result_seq

        return fib(self.n)

    def find_steps(self):
        """Find best 1 step and 2 steps with sequence"""
        n = self.n

        def build_steps(remaining, current_seq):
            if remaining == 0:
                return current_seq
            elif remaining >= 2:
                return build_steps(remaining - 2, current_seq + [2])
            else:
                return build_steps(remaining - 1, current_seq + [1])

        sequence = build_steps(n, [])
        two_steps = sequence.count(2)
        one_step = sequence.count(1)

        return one_step, two_steps, sequence

    def print_result(self):
        """Print result"""
        total_ways, _ = self.count_ways()
        one_step, two_step, best_steps = self.find_steps()

        def make_steps(seq, result=""):
            if not seq:
                return result
            if not result:
                return make_steps(seq[1:], str(seq[0]))
            return make_steps(seq[1:], f"{result} -> {seq[0]}")

        step = make_steps(best_steps)

        print(f"Total ways: {total_ways}")
        print(f"Best steps: {one_step + two_step}")
        print(f"Steps: {step}")
        print(f"F: {one_step} times")
        print(f"L: {two_step} times")

def main():
    """Main function"""
    n = int(input())
    stairs = Stairs(n)
    stairs.print_result()

main()
