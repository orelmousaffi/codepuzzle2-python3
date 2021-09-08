import 'mocha';
import { expect } from 'chai';

import { FormatTestCaseName } from "./utils";
import { steps } from "./steps";

import { add } from "../calculator";

steps.forEach((step, stepIndex) => {
    const stepNbr = stepIndex + 1;

    describe(`Step ${stepNbr} - ${step.Title}`, () => {
        step.TestCases.forEach((testCase, testCaseIndex) => {
            const testCaseNbr = testCaseIndex + 1;
            const testCaseTitle = FormatTestCaseName(stepNbr, testCaseNbr, testCase);

            if ("Error" in testCase) {
                it(testCaseTitle, (done) => {
                    // using the try/catch approach to assert on errors so we can give more feedback to the dev
                    let result;
                    try {
                        result = add(testCase.Input);
                    } catch(error) {
                        expect(error.message).to.equal(testCase.Error, "The error was thrown but its message does not match the expected result.");
                        done();
                    }
                    
                    expect.fail(`An error was expected to be thrown, but instead the code returned the value: ${result}`);
                }); 
            } else {
                it(testCaseTitle, () => {
                    expect(add(testCase.Input)).to.equal(testCase.Expected);
                });
            }
        });
    });
});
