from peewee import *

# this database
db = SqliteDatabase('chainsawjugglingrecordholders.sqlite')
# fields that will become database columns
class Recordholders(Model):
    name = CharField()
    country = CharField()
    numberofcatches = IntegerField()
    # link the model to a particular database
    class Meta:
        database = db
    def __str__(self):
        return f'{self.name} from {self.country} achieved {self.numberofcatches}.'
# connect to DB, and create tables that map the model Recordholders
db.connect()
db.create_tables([Recordholders])
# create recordholders  objects and call save function to insert them into the database
Recordholders.delete().execute()
janna = Recordholders(name="Janna Mustonen", country='Finland', numberofcatches=98)
janna.save()
ian = Recordholders(name="Ian Steward", country='Canada', numberofcatches=94)
ian.save()
aaron = Recordholders(name="Aaron Gregg", country='Canada', numberofcatches=88)
aaron.save()
chad = Recordholders(name="Chad Taylor", country='USA', numberofcatches=78)
chad.save()
def main():
    while True:
        try:
            display_menu()
            choice = int(input('Enter choice: '))
            if choice == 1:
                add()
            elif choice == 2:
                search()
            elif choice == 3:
                update()
            elif choice == 4:
                delete()
            elif choice == 5:
                display_all_recordholders()
            elif choice == 6:
                print('Good bye!')
                break
            else:
                print('\nNot a valid choice.\n')
        except ValueError as e:
            print('\nPlease enter a numeric choice.\n')

def display_menu(): # Menu option for user
    print('1: Add new record')
    print('2: Search record')
    print('3: Update record')
    print('4: Delete record')
    print('5: Display record')
    print('6: Exit')

def add(): # Insert data from user into db.
    add_name = input('Enter a record holders name: ').title()
    add_country = input('Enter country: ').upper()
    add_numberofcatches = int(input('Enter number of catches: '))
    
    add_to_record = Recordholders(name = add_name, country = add_country, catches = add_numberofcatches)
    add_to_record.save()

def search(): # Searching for record by name.
    search_name = input('Enter full name to search: ').title()
    search_record = Recordholders.select().where(Recordholders.name == search_name).execute()
    # If name searched is found then display else print a message to user.
    for record in search_record:
        print(f'Record found - {record}.')
        break
        
    else:
        print(f'No record found under name: {search_name}')

def update(): # Updating record db by name then updating catches.
    update_by_name = input('Enter record holders name to update record: ').title()
    update_numberofcatches = int(input('Enter number of new catches: '))
    # If record holder is found in db then updates else print message to user.
    rows_updated = Recordholders.update(catches = update_numberofcatches).where(Recordholders.name == update_by_name).execute()
    if rows_updated == 0:
        print(f'No record was found under name: {update_by_name}.')
    else:
        print(f'Record under name {update_by_name} has been updated to {update_numberofcatches}.')

def delete(): # Delete record holders by name. 
    delete_name = input('Enter record holders full name to delete from record: ').title()
    # Search by name, if not found send user message else delete from db.
    rows_deleted = Recordholders.delete().where(Recordholders.name == delete_name).execute()
    if rows_deleted == 0:
        print(f'No record deleted under name: {delete_name}.')
    else:
        print(f'Record under name {delete_name} has been deleted.')

def display_all_recordholders(): # Displaying all contestants.
    print('Records of all contestants:')
    all_contestants = Recordholders.select()
    for contestants in contestants:
        print(contestants)

main()
