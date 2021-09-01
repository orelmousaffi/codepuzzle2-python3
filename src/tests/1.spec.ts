import add from "../calculator";
import { EscapeNewLines, IErrorTestCase, IValueTestCase } from "./utils";
import { expect } from 'chai';
import 'mocha';
import { steps } from "./steps";

steps.forEach((step, stepIndex) => {
    describe(`Step ${stepIndex + 1} - ${step.Title}`, () => {
        step.TestCases.forEach((testCase, testCaseIndex) => {
            if ("Error" in testCase) {
                it(`Test Case ${testCaseIndex + 1} - input: "${EscapeNewLines(testCase.Input)}"; expected error: "${testCase.Error}"`, () => {
                    expect(() => add(testCase.Input)).to.Throw((testCase).Error);
                }); 
            } else {
                it(`Test Case ${testCaseIndex + 1} - input: "${EscapeNewLines(testCase.Input)}"; expected value: ${testCase.Expected}`, () => {
                    expect(add(testCase.Input)).to.equal(testCase.Expected);
                });
            }
        });
    });
});
