# Note: in order to run this code you may have to
# pip install pillow
# and save this code in the same folder as your desired converted image file

from PIL import Image
def export(name, extension=""):
    img = Image.open(name + "." + extension)
    img = img.convert("RGB")
    img.save(name + ".pdf")

print("[ Conversion from Image File to PDF format locally ]")
while (True):
    line = input("Enter the file name (if no other conversions, just press enter): ")
    point = line.rfind(".")
    name, extension = line[:point], line[point+1:]
    if name != "":
        try:
            export(name, extension)
            print("Conversion for", name + "." + extension, "to",
                  name + ".pdf", "complete. You may now convert something else.\n")
        except:
            print("No such file '" + name + "." + extension + "' can be found.")
            print("Try moving the file into the same folder as this code or re-checking the name of your file.\n")
    else:
        print("\nNo more conversions can be done from this point onwards.")
        break

# Presumably, I can make a tool to make it convert stuff to ANY file format
# But that's for the future.
