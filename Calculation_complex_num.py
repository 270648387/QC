real1 = float(input("Enter the real part of the first complex number: "))
imag1 = float(input("Enter the imaginary part of the first complex number: "))
c1 = complex(real1, imag1)


real2 = float(input("Enter the real part of the second complex number: "))
imag2 = float(input("Enter the imaginary part of the second complex number: "))
c2 = complex(real2, imag2)

sum_result = c1 + c2
minus_result = c1 - c2
product_result = c1 * c2
divide_result = c1 / c2

print("Sum:", sum_result)
print("Minus:", minus_result)
print("Product:", product_result)
print("Divide:", divide_result)
