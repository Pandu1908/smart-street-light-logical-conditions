motion = input("Is motion detected? (yes/no): ").lower()
dark = input("Is it dark? (yes/no): ").lower()

if dark == "yes" and motion == "yes":
    print("💡 Street light ON")
elif dark == "yes":
    print("🌙 Low brightness mode")
else:
    print("☀️ Street light OFF")
