def arithmetic_arranger(problems, solve=False):
    if many_problems(problems):
        return 'Error: Too many problems.'
    if check_operators(problems):
        return "Error: Operator must be '+' or '-'."
    if check_operands(problems):
        return 'Error: Numbers must only contain digits.'
    if check_max_digits(problems):
        return "Error: Numbers cannot be more than four digits."
    arranged_problems = arrange_problems(problems, solve)
    return arranged_problems


# Check if we have too many problems
def many_problems(problems):
    if len(problems) > 5:
        return True


# Check operators are + or -
def check_operators(problems):
    for operation in range(0, len(problems)):
        if '*' in problems[operation] or '/' in problems[operation]:
            return True


# Check operands contain digits only
def check_operands(problems):
    new_problems = problems.copy()
    filter_out = '+- '
    for operation in range(0, len(new_problems)):
        for character in filter_out:
            new_problems[operation] = new_problems[operation].replace(character, '')
    for operation in range(0, len(new_problems)):
        if new_problems[operation].isnumeric() is False:
            return True


# Check that operands within four digits
def check_max_digits(problems):
    print(problems)
    new_problems = problems.copy()
    for operation in range(0, len(new_problems)):
        if '+' in new_problems[operation]:
            new_problems[operation] = new_problems[operation].split(' + ')
        else:
            new_problems[operation] = new_problems[operation].split(' - ')
    for operation in range(0, len(new_problems)):
        for number in new_problems[operation]:
            if len(number) > 4:
                return True


# Returns first line of arithmetic problem
def write_line_one(problems):
    new_problems = problems.copy()
    line_one = ''
    for operation in range(0, len(new_problems)):
        if '+' in new_problems[operation]:
            new_problems[operation] = new_problems[operation].split(' + ')
        else:
            new_problems[operation] = new_problems[operation].split(' - ')
        if len(new_problems[operation][0]) < len(new_problems[operation][1]):
            num_diff = abs(len(new_problems[operation][0]) - len(new_problems[operation][1]))
            for space_counter in range(0, num_diff):
                line_one += ' '
        else:
            pass
        line_one += '  '
        if operation < len(new_problems) - 1:
            line_one = line_one + new_problems[operation][0] + '    '
        else:
            line_one += new_problems[operation][0]
    return line_one


# Returns second line of arithmetic problem
def write_line_two(problems):
    new_problems = problems.copy()
    line_two = ''
    for operation in range(0, len(new_problems)):
        new_problems[operation] = new_problems[operation].split(' ')
        line_two = line_two + new_problems[operation][1] + ' '
        if len(new_problems[operation][2]) < len(new_problems[operation][0]):
            num_diff = abs(len(new_problems[operation][2]) - len(new_problems[operation][0]))
            for space_counter in range(0, num_diff):
                line_two += ' '
        else:
            pass
        if operation < len(new_problems) - 1:
            line_two = line_two + new_problems[operation][2] + '    '
        else:
            line_two += new_problems[operation][2]
    return line_two


# Returns third line of arithmetic problem
def write_line_three(problems):
    new_problems = problems.copy()
    line_three = '--'
    for operation in range(0, len(new_problems)):
        if '+' in new_problems[operation]:
            new_problems[operation] = new_problems[operation].split(' + ')
        else:
            new_problems[operation] = new_problems[operation].split(' - ')

        if len(new_problems[operation][0]) >= len(new_problems[operation][1]):
            for dash_counter in range(0, len(new_problems[operation][0])):
                line_three += '-'
        else:
            for dash_counter in range(0, len(new_problems[operation][1])):
                line_three += '-'
        if operation < len(new_problems) - 1:
            line_three += '    --'
    return line_three


# Returns answer of arithmetic problem
def write_answer(problems):
    new_problems = problems.copy()
    full_answer = ''
    for operation in range(0, len(new_problems)):
        spacing = ''
        if '+' in new_problems[operation]:
            new_problems[operation] = new_problems[operation].split(' + ')
            answer = int(new_problems[operation][0]) + int(new_problems[operation][1])
        else:
            new_problems[operation] = new_problems[operation].split(' - ')
            answer = int(new_problems[operation][0]) - int(new_problems[operation][1])

        if len(new_problems[operation][0]) >= len(new_problems[operation][1]):
            space_compare = abs(2 + len(new_problems[operation][0]) - len(str(answer)))
            for space_counter in range(0, space_compare):
                spacing += '.'
        else:
            space_compare = abs(2 + len(new_problems[operation][1]) - len(str(answer)))
            for space_counter in range(0, space_compare):
                spacing += '.'
        if operation < len(new_problems) - 1:
            answer = spacing + str(answer) + '....'
        else:
            answer = spacing + str(answer)
        full_answer += answer
    full_answer = full_answer.replace('.', ' ')
    return full_answer


# Writes the solution
def arrange_problems(problems, solve):
    if solve is False:
        arranged_problems = write_line_one(problems) + '\n' + write_line_two(problems) + '\n' + write_line_three(
            problems)
    else:
        arranged_problems = write_line_one(problems) + '\n' + write_line_two(problems) + '\n' + write_line_three(
            problems) \
                            + '\n' + write_answer(problems)
    return arranged_problems
