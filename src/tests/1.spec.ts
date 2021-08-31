import add from "../calculator";
import { ChallengeStep, escapeNewLines } from "./utils";
import { expect } from 'chai';
import 'mocha';

const steps: ChallengeStep[] = [
    { Title: "given an empty string should return", TestCases: [{Input: "", Expected: 0}]},
    { Title: "given a string with a single value should return the same value", TestCases: [{Input: "42", Expected: 42}]},
    { Title: "given a string with two comma separated values should return the sum of them", TestCases: [{Input: "2,2", Expected: 4}]},
    { Title: "given a string with N comma separated values should return the sum of all of them", TestCases: [{Input: "1,2,3,4,5", Expected: 15}]},
    { Title: "should accept either commas and/or new lines ('\\n') as value separators.", TestCases: [{Input: "1\n2,3", Expected: 6}]},
];

steps.forEach((step, stepIndex) => {
    describe(`Step ${stepIndex} - ${step.Title}`, () => {
        step.TestCases.forEach((testCase, testCaseIndex) => {
            it(`input: "${escapeNewLines(testCase.Input)}"; expected: ${testCase.Expected}`, () => {
                expect(add(testCase.Input)).to.equal(testCase.Expected);
            });
        });
    });
});
