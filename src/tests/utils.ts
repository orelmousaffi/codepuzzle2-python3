export function EscapeNewLines(text: string): string {
    return text.replace(/\n/gi, '\\n');
}

export interface IChallengeStep {
    Title: string;
    TestCases: ITestCase[];
}

export interface ITestCase {
    Input: string;
    Expected: number;
}