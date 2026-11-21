DELIMITER = ";"

class TIMESTAMP:
    weekday = ""
    hour = ""
    consumption = 0.0
    price = 0.0

def readFile(PFilename: str, PTimestamps: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    with open(PFilename, "r", encoding="UTF-8") as Filehandle:
        Filehandle.readline()
        for line in Filehandle:
            # line.strip("\n")
            if line == "":
                continue
            Row = line.strip("\n").split(DELIMITER)
            Timestamp = TIMESTAMP()
            Timestamp.weekday = Row[0]
            Timestamp.hour = Row[1]
            Timestamp.consumption = int(Row[2])
            Timestamp.price = float(Row[3])
            PTimestamps.append(Timestamp)
            Row.clear()
    return None

def displayTimestamps(Timestamps):
    print("Electricity usage:")
    for Timestamp in Timestamps:
        total = Timestamp.consumption * Timestamp.price
        print(" - {} {}:00, price {:.2f}, consumption {:.2f} kWh, total {:.2f} €".format(Timestamp.weekday, Timestamp.hour, Timestamp.price, Timestamp.consumption, total ))

def main():
    filename = input("Enter filename: ")
    PTimestamps = []
    readFile(filename, PTimestamps)
    displayTimestamps(PTimestamps)
    print("Program ending.")

main()