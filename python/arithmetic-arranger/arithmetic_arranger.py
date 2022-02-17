def arithmetic_arranger(problems, show_answers="False"):
    # Error if user inputs more than five problems to solve.
    if len(problems) > 5:
        return "Error: Too many problems."

    # Creates lists in which to save each element of the problems before building the strings.
    first_operands = list()
    second_operands = list()
    operators = list()
    widths = list()
    results = list()

    for problem in problems:
        # Split first in order to doerror checking
        chopped = problem.split()
        # Error if operator is not + or -
        if chopped[1] != '+' and chopped[1] != '-':
            return "Error: Operator must be '+' or '-'."
        # Error if the operands contain non-digits
        if not chopped[0].isdigit() or not chopped[2].isdigit():
            return "Error: Numbers must only contain digits."
        # Error if the user inputs numbers longer than four digits
        if len(chopped[0]) > 4 or len(chopped[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Split each problem into its individual components and adds them to the list
        results.append(str(eval(problem)))
        first_operands.append(chopped[0])
        second_operands.append(chopped[2])
        operators.append(chopped[1])
        # The operator must have only one space between it and the longest operand.
        # This is achieved saving the length of the longest operand, and adding 2 to it (for the operator and a space)
        widths.append(len(max(chopped, key=len)) + 2)

    first_row = ''
    second_row = ''
    third_row = ''
    fourth_row = ''

    for i in range(len(problems)):
        # The first row must be the first-operands right aligned.
        first_row += first_operands[i].rjust(widths[i]) + '    '
    # Second row is the operator and the second-operand right aligned.
        second_row += operators[i] + \
            second_operands[i].rjust(widths[i] - len(operators[i])) + '    '
    # Third row is composed of as many dashes as the longest line in the problem (i.e the width)
        third_row += '-'*widths[i] + '    '
    # Fourth row is the result of the operations right-aligned
        fourth_row += results[i].rjust(widths[i]) + '    '

    # Concatenate every row into the finaul result to be output, using \n for newlines.
    # Use r.strip to remove the trailing four spaces at the end of the line.
    arranged_problems = first_row.rstrip() + '\n' + second_row.rstrip() + \
        '\n' + third_row.rstrip()

    # If the function call includes a 'True' argument, then also show the solution of the problem.
    if show_answers is True:
        arranged_problems += '\n' + fourth_row.rstrip()

    return arranged_problems
