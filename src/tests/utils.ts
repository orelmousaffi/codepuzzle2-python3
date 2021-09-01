export function EscapeNewLines(text: string): string {
    return text.replace(/\n/gi, '\\n');
}

export interface IChallengeStep {
    Title: string;
    TestCases: TestCase[];
}

export type TestCase = IErrorTestCase | IValueTestCase;

interface IBaseTestCase {
    Input: string;
}

export interface IErrorTestCase extends IBaseTestCase {
    Error: string;
}

export interface IValueTestCase extends IBaseTestCase {
    Expected: number;
}