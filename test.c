 #include <unity.h>

extern int _float_int(float num);


// Declarations of the setUp and tearDown functions, which will be executed before and after each test
void setUp(void)
{
     // You can initialize variables or perform any necessary configuration before each test
}

void tearDown(void)
{
     // You can clean resources or perform actions after each test
}

// Unit test declaration
void testFloatToIntConversion(void)
{
     float input = 14.29f;
     int expected = 15; // The expected result for 14.29 according to the _float_int function in your assembler
     int result = _float_int(input);
     TEST_ASSERT_EQUAL_INT(expected, result);
}

// Main function that will execute all the tests
int main(void)
{
     UNITY_BEGIN(); // Start the testing framework

     // Add each test to the framework
     RUN_TEST(testFloatToIntConversion);

     // Finish and run the tests, return the result
     return UNITY_END();
}