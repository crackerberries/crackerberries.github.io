#include <iostream>

float getValue1()
{
    std::cout << "enter the first number: " << std::endl;
    float num1{};
    std::cin >> num1;
    return num1;
}

float getValue2()
{
    std::cout << "enter the second number: " << std::endl;
    float num2{};
    std::cin >> num2;
    return num2;
}

int main()
{
    std::cout << "hello!" << std::endl;

    int op{};

    system("pause");

    std::cout << "pick an operation" << std::endl;
    std::cout << "addition: 1" << std::endl;
    std::cout << "subtraction: 2" << std::endl;
    std::cout << "multiplication: 3" << std::endl;
    std::cout << "division: 4" << std::endl;

    std::cin >> op;

    float x = getValue1();
    float y = getValue2();

    //addition
    if (op == 1)
    {

        std::cout << "the answer is " << x + y << std::endl;
    }

    //subtraction
    if (op == 2)
    {
        std::cout << "the answer is " << x - y << std::endl;
    }

    //multiplication
    if (op == 3)
    {
        std::cout << "the answer is " << x * y << std::endl;
    }

    //division
    if (op == 4)
    {
        std::cout << "the answer is " << x / y << std::endl;
    }

    //end of program
    system("pause");
}