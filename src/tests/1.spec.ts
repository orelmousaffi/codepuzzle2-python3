import add from "../calculator";
import { formatTestName } from "./utils";
import { expect } from 'chai';
import 'mocha';

const testCases = [
    { name: "given an empty string should return", input: "", expected: 0 },
    { name: "given a string with a single value should return the same value", input: "42", expected: 42 },
    { name: "given a string with two comma separated values should return the sum of them", input: "2,2", expected: 4 },
    { name: "given a string with N comma separated values should return the sum of all of them", input: "1,2,3,4,5", expected: 15 },
];

describe("Step 1 - Sum comma separated values.", function() {
    testCases.forEach(({name, input, expected}, i) => {
        it(formatTestName(1, i, name, input, expected), () => {
            expect(add(input)).to.equal(expected);
        });
    });
});