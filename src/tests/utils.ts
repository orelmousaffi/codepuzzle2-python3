export function formatTestName(
    step: number,
    testCaseIndex: number,
    testName: string,
    input: string,
    expected: number) {
    return `Step ${step}.${testCaseIndex + 1} - ${testName}.\n\tinput: "${escapeNewLines(input)}"; expected: ${expected}`;
}

export function escapeNewLines(text: string): string {
    return text.replace('\n', '\\n');
}

export interface ChallengeStep {
    Title: string;
    TestCases: TestCase[];
}

export interface TestCase {
    Input: string;
    Expected: number;
}