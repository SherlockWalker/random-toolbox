import segno

while (True):
    line = input("Enter the string to generate QR code (if no other conversions, just press enter): ")
    if line:
        segno.make(line).save(line)
        print("QR code generated and complete. You may now convert something else.\n")
    else:
        print("\nNo more QR codes can be made from this point onwards.")
        break
