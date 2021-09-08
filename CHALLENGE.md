## Coding Challenge - String Calculator
Based on the [String Calculator TDD Kata](https://osherove.com/tdd-kata-1) by Roy Osherove.

### Rules
- Try not to skip ahead.
- Do one step at a time. The trick is to practice working incrementally.
- The tests are defined and you should only implement the necessary code to make one test pass at any given time.
- The tests will run the `add` function defined in the `src/calculator.ts` file. You should use that function as the wrapper for your code.
- The test runner will stop running when it detects 1 failing test. Every time you implement some code you should run the tests again to check your progress.
- Focus on straight forward cases, don't mind edge cases and invalid inputs.
- Run the tests using the `npm test` command. Read the failing test message and implement the necessary functionality to make the failing test pass. Rinse and repeat.

### Challenge Steps

We're creating a simple string calculator that exports a `add` function. This function receives a string as its input and return an integer representing the result of the operation.

1. This function should return the value `0` every time it receives an empty string as its input. (`add("")` should return `0`)

2. When receiving a string with only one number, it should return the number. (`add("1")` should return `1`)

3. When receiving a string with 2 comma separated values it should return the sum of them. (`add("1,2")`should return `3`)

4. Now allow the `add` function to handle an unknown amount of comma separated numbers.

5. Allow the `add` funtion to also handle new lines between numbers and not just commas. (`add("1,2\n3")`should return `6`)

6. Add support to different delimiters
    - To change a delimiter, the beginning of the string will contain a separate line that looks like this: `"//(delimiter)\n(numbers…)"` for example `"//;\n1;2"` should return 3 where the default delimiter is `";"`.
    - The first line is optional.
    - All existing scenarios should still be supported

7. Calling `add` with a negative number will throw an error `"negatives not allowed"` - and the negative number that was passed. 
    - for example `add("1,-2") -> "negatives not allowed: -2"`
    - If there are multiple negatives, show all of them in the error message.

8. Numbers greater than 1000 should be ignored, so adding 2 + 1001 = 2.

9. Delimiters can be of any length with the following format: `"//[delimiter]\n"` for example: `"//[***]\n1***2***3"` should return `6`.
    - Words are not allowed as delimiters

10. Allow multiple delimiters like this: `"//[delim1][delim2]\n"` for example `"//[*][%]\n1*2%3"` should return `6`.

11. Make sure you can also handle multiple delimiters with length longer than one char
    - Words are still not allowed as delimiters