# -*- coding: utf-8 -*-

"""
Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.
"""

guests = ["Raul", "Ramon", "Jose Luis"]

print(f"{guests[0]}, Te invito a mi cena")
print(f"{guests[1]}, Te invito a mi cena")
print(f"{guests[2]}, Te invito a mi cena")

"""
Changing Guest List: You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
  • Start with your program from Exercise 3-4. Add a print() call at the end of
    your program, stating the name of the guest who can’t make it.
  • Modify your list, replacing the name of the guest who can’t make it with the
    name of the new person you are inviting.
  • Print a second set of invitation messages, one for each person who is still in
    your list.
"""
print("\n")
print(f"{guests[0]} no puede asistir")

guests[0] = "Flor"

print("\n")
print(f"{guests[0]}, Te invito a mi cena")
print(f"{guests[1]}, Te invito a mi cena")
print(f"{guests[2]}, Te invito a mi cena")


"""
More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
  
  • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the
    end of your program, informing people that you found a bigger table.
  • Use insert() to add one new guest to the beginning of your list.
  • Use insert() to add one new guest to the middle of your list.
  • Use append() to add one new guest to the end of your list.
  • Print a new set of invitation messages, one for each person in your list
"""
print("\n")
print("Se ha encontrado una mesa mas grande. Por lo que se incluiran mas invitados")
print("\n")

guests.insert(0, "Luna")
guests.insert(2, "Copito")
guests.append("Ernesto")

print(f"{guests[0]}, Te invito a mi cena")
print(f"{guests[1]}, Te invito a mi cena")
print(f"{guests[2]}, Te invito a mi cena")
print(f"{guests[3]}, Te invito a mi cena")
print(f"{guests[4]}, Te invito a mi cena")
print(f"{guests[5]}, Te invito a mi cena")

"""
Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and now you have space for only two guests.

  • Start with your program from Exercise 3-6. Add a new line that prints a
    message saying that you can invite only two people for dinner.
  • Use pop() to remove guests from your list one at a time until only two
    names remain in your list. Each time you pop a name from your list, print a
    message to that person letting them know you’re sorry you can’t invite them
    to dinner.
  • Print a message to each of the two people still on your list, letting them
    know they’re still invited.
  • Use del to remove the last two names from your list, so you have an empty
    list. Print your list to make sure you actually have an empty list at the end of
    your program
"""
print("\n")
print("Lamentamos informar que solo será posible que asistan dos invitados")
print("\n")

guest = guests.pop()
print(f"{guest}, ya no podras asistir a la cena")
guest = guests.pop()
print(f"{guest}, ya no podras asistir a la cena")
guest = guests.pop()
print(f"{guest}, ya no podras asistir a la cena")
guest = guests.pop()
print(f"{guest}, ya no podras asistir a la cena")

print("\n")

print(f"{guests[0]}, aun sigues invitado a mi cena")
print(f"{guests[1]}, aun sigues invitado a mi cena")

print("\n")

del guests[0]
del guests[0]

print(guests)
