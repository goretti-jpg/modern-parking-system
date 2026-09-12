"""Modern Parking System"""

class ParkingRecord:
    def __init__(self, plate_number, slot_number, entry_time):
        self.plate_number = plate_number
        self.slot_number = slot_number
        self.entry_time = entry_time
        self.exit_time = None
        self.duration = 0
        self.amount = 0


total_parking_slots = 100
parking_rate = 150  #rate per hour

parking_records = []

available_parking_slots = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None
}


while True:

    print("\n===== PARKING SYSTEM =====")
    print("Available slots:", total_parking_slots)

    print("\n1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. View available parking Slots")
    print("4. Exit System")

    choice = input("Choose an option: ")

    # VEHICLE ENTRY
    if choice == "1":

        if total_parking_slots == 0:
            print("Sorry, parking is full!")

        else:
            plate_number = input("Enter vehicle number plate: ")
            entry_time = int(input("Enter entry hour (0-23): "))


            for slot in available_parking_slots:
                if available_parking_slots[slot] is None:

                    available_parking_slots[slot] = plate_number

                    record = ParkingRecord(
                        plate_number,
                        slot,
                        entry_time
                    )

                    parking_records.append(record)

                    total_parking_slots = total_parking_slots - 1

                    print("Vehicle parked successfully!")
                    print("Your parking slot is:", slot)

                    break

    # VEHICLE EXIT
    elif choice == "2":

        plate_number = input("Enter vehicle number plate: ")
        exit_time = int(input("Enter exit hour (0-23): "))

        vehicle_found = False

        for record in parking_records:

            if record.plate_number == plate_number:

                vehicle_found = True

                record.exit_time = exit_time

                # Calculate parking duration
                record.duration = record.exit_time - record.entry_time

                if record.duration < 0:
                    record.duration = record.duration + 24

                # Calculate amount
                record.amount = (record.duration * parking_rate)

                print("\n===== PARKING BILL =====")
                print("Number plate:", record.plate_number)
                print("Parking slot:", record.slot_number)
                print("Entry hour:", record.entry_time)
                print("Exit hour:", record.exit_time)
                print("Duration:", record.duration, "hours")
                print("Amount to pay: KSh", record.amount)

                # Free the parking slot
                available_parking_slots[record.slot_number] = None

                total_parking_slots =total_parking_slots + 1

                # Remove vehicle from active parking records
                parking_records.remove(record)

                print("Vehicle has exited successfully.")
                print("Available slots:", total_parking_slots)

                break

        if vehicle_found == False:
            print("Vehicle not found.")

    # VIEW PARKING SLOTS
    elif choice == "3":

        print("\n===== PARKING SLOTS =====")

        for slot in available_parking_slots:

            if available_parking_slots[slot] is None:
                print("Slot", slot, ": Available")

            else:
                print("Slot", slot, ":",available_parking_slots[slot])

    # EXIT SYSTEM
    elif choice == "4":

        print("Thank you for using the parking system!")
        break

    else:
        print("Invalid choice. Please try again.")
