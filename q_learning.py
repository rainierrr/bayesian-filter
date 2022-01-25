from multiprocessing.dummy import current_process


def q_learning(current_idx, action_idx, next_idx, r):
    current_q = 0

    if len(q[current_idx]) == 1:
        current_q = q[current_idx][0]
    else:
        current_q = q[current_idx][action_idx]

    next_max_q = max(q[next_idx])

    next_q = (
        (1-a) * current_q) + (a * (r + (y*next_max_q)))

    if len(q[current_idx]) == 1:
        q[current_idx][0] = next_q
    else:
        q[current_idx][action_idx] = next_q


q = [[-75.00], [-18.75, 2.50], [0.00, 2.50], [50.00]]
a = 0.5
y = 0.9

q_learning(1, 1, 2, 5)
print("ステップ{}実行後: {}".format(1, q))
test = (0.5 * - 75) + (0.5 * (5 + y*2.5))
q_learning(2, 1, 2, 5)
print("ステップ{}実行後: {}".format(2, q))
q_learning(2, 1, 3, 5)
print("ステップ{}実行後: {}".format(3, q))
