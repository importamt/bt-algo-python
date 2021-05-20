from programmers.hash.unfinished_runner import unfinished_runner

cases = [
    {
        "case": {
            "participant": ["leo", "kiki", "eden"],
            "completion": ["eden", "kiki"]
        },
        "expected": "leo"
    },

    {
        "case": {
            "participant": ["marina", "josipa", "nikola", "vinko", "filipa"],
            "completion": ["josipa", "filipa", "marina", "nikola"]
        },
        "expected": "vinko"
    },

    {
        "case": {
            "participant": ["mislav", "stanko", "mislav", "ana"],
            "completion": ["stanko", "ana", "mislav"]
        },
        "expected": "mislav"
    },
]


def main():
    is_success = True
    for case in cases:
        result = unfinished_runner.unfinished_runner(case['case']['participant'], case['case']['completion'])
        if result != case['expected']:
            print("FAIL! : RESULT", result, ", EXPECTED : ", case['expected'])
            is_success = False
            break
    if is_success:
        print("SUCCESS!")
    return


if __name__ == '__main__':
    main()
