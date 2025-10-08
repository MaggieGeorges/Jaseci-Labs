walker init {
    can run {
        print("🧮 Welcome to the Jac Calculator!");
        print("You can perform +, -, *, or / operations.");

        let num1 = 10;
        let num2 = 5;
        let op = "+";

        if op == "+" {
            print("Result: " + str(num1 + num2));
        } elif op == "-" {
            print("Result: " + str(num1 - num2));
        } elif op == "*" {
            print("Result: " + str(num1 * num2));
        } elif op == "/" {
            print("Result: " + str(num1 / num2));
        } else {
            print("Invalid operation!");
        }
    }
}

test {
    init.run();
}
