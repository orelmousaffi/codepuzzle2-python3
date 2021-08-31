import add from "../../src/calculator";
import { formatTestName } from "../utils";

const testCases = [
    { name: "given an empty string should return", input: "", expected: 0 },
];

describe("Step 1 - Sum up to 2 comma separated values.", function() {
    testCases.forEach(({name, input, expected}, i) => {
        test(formatTestName(1, i, name, input, expected), () => {
            expect(add(input)).toEqual(expected);
        });
    });
});