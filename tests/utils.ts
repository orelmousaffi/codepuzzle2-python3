export function formatTestName(step: number, testCaseIndex: number, testName: string, input: string, expected: number) {
    return `Step ${step}.${testCaseIndex + 1} - ${testName}. input: ${input}; expected: ${expected}.`;
}