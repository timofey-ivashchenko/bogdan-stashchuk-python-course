def get_fn_invocation_info(fn_name: str, times_invoked: int) -> str:
    return f"Function '{fn_name}' was invoked {times_invoked} times."


argument_list = [
    {'fn_name': 'input', 'times_invoked': 0},
    {'fn_name': 'print', 'times_invoked': 1},
    {'fn_name': 'range', 'times_invoked': 2}
]

arguments_1, arguments_2, arguments_3 = argument_list

print(get_fn_invocation_info(**arguments_1))
print(get_fn_invocation_info(**arguments_2))
print(get_fn_invocation_info(**arguments_3))
