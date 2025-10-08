import py "calculator_ai";

walker Calculator {
    has expression: str;

    can start with `root entry {
        emit `Welcome to the AI Calculator!`;
        self.calculate();
    }

    can calculate with entry {
        let result = py_call("evaluate_expression", expression);
        emit `Expression: ${expression}`;
        emit `Result: ${result}`;
    }
}

with entry:__main__ {
    root spawn Calculator("2 + 2");
    root spawn Calculator("10 + 5");
}