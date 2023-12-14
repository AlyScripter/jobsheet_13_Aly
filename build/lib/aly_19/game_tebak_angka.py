def guess_number():
    secret_number = 9
    guess = 0
    guess_limit = 3

    while guess < guess_limit:
        user = int(input("Masukkan Nomor Tebakan Anda :"))
        if user == secret_number:
            print("Tebakan Anda Benar")
            break
        else:
            print("Tebakan Anda Salah")
            guess += 1
    else:
        print(f"Anda tidak menemukan angkanya, angka rahasianya adalah {secret_number}")

# Call the function to run the game
guess_number()
