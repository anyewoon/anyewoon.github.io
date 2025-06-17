# bmi_calculator.py

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    print(f"당신의 BMI는 {bmi:.2f}입니다.")
    
    if bmi < 18.5:
        print("저체중입니다.")
    elif bmi < 23:
        print("정상입니다.")
    elif bmi < 25:
        print("과체중입니다.")
    else:
        print("비만입니다.")

if __name__ == "__main__":
    w = float(input("몸무게(kg): "))
    h = float(input("키(m): "))
    calculate_bmi(w, h)
