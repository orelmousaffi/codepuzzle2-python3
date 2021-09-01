import add from "../calculator";
import { EscapeNewLines, IErrorTestCase, IValueTestCase } from "./utils";
import { expect } from 'chai';
import 'mocha';
import { steps } from "./steps";

steps.forEach((step, stepIndex) => {
    describe(`Step ${stepIndex + 1} - ${step.Title}`, () => {
        step.TestCases.forEach((testCase, testCaseIndex) => {
            if ("Error" in testCase) {
                it(`Test Case ${testCaseIndex + 1} - input: "${EscapeNewLines(testCase.Input)}"; expected error: "${testCase.Error}"`, (done) => {
                    // using the try/catch approach to assert on errors so we can give more feedback to the dev if necessary
                    let result;
                    try {
                        result = add(testCase.Input);
                    } catch(error) {
                        expect(error.message).to.equal(testCase.Error);
                        done();
                    }
                    
                    expect.fail(`An error was expected, but instead the code returned the value: ${result}`);
                }); 
            } else {
                it(`Test Case ${testCaseIndex + 1} - input: "${EscapeNewLines(testCase.Input)}"; expected value: ${testCase.Expected}`, () => {
                    expect(add(testCase.Input)).to.equal(testCase.Expected);
                });
            }
        });
    });
});
