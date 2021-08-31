import add from "../../src/calculator";
import { formatTestName } from "../utils";

const testCases = [
    { name: "given a string with a single value should return the same value", input: "42", expected: 42 }
];

describe("Step 1 - Sum up to 2 comma separated values.", function() {
    testCases.forEach(({name, input, expected}, i) => {
        test(formatTestName(1, i+1, name, input, expected), () => {
            expect(add(input)).toEqual(expected);
        });
    });
});