def unfinished_runner(participant, completion):
    runner_map = {}
    for i in range(0, len(participant)):
        if participant[i] not in runner_map:
            runner_map[participant[i]] = 0
        runner_map[participant[i]] += 1

        if i < len(completion):
            if completion[i] not in runner_map:
                runner_map[completion[i]] = 0
            runner_map[completion[i]] -= 1

    answer = next(key for key in runner_map.keys() if runner_map[key] > 0)
    return answer
