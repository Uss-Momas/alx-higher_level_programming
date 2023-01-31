#!/usr/bin/python3
import sys


def is_valid_state(state):
    # check if it is a valid solution
    return True


def get_candidates(state):
    return []


def search(state, solutions):
    if is_valid_state(state):
        solutions.append(state.copy())
        # return

    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)


def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    a = []
    for i in range(N):
        a.append([i, None])


if __name__ == "__main__":
    main()
