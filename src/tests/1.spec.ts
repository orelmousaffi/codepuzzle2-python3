import add from "../calculator";
import { EscapeNewLines } from "./utils";
import { expect } from 'chai';
import 'mocha';
import { steps } from "./steps";

steps.forEach((step, stepIndex) => {
    describe(`Step ${stepIndex + 1} - ${step.Title}`, () => {
        step.TestCases.forEach((testCase, testCaseIndex) => {
            it(`Test Case ${testCaseIndex + 1} - input: "${EscapeNewLines(testCase.Input)}"; expected: ${testCase.Expected}`, () => {
                expect(add(testCase.Input)).to.equal(testCase.Expected);
            });
        });
    });
});
