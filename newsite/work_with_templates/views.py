from django.shortcuts import render

names = ['Sophia', 'Jackson', 'Olivia', 'Liam', 'Emma', 'Noah', 'Ava', 'Elijah', 'Isabella', 'Lucas', 'Mia', 'Mason',
         'Amelia', 'Oliver', 'Charlotte', 'Ethan', 'Harper', 'Aiden', 'Evelyn', 'Logan', 'Abigail', 'Levi', 'Emily',
         'Sebastian', 'Elizabeth', 'Caleb', 'Mila', 'Michael', 'Ella', 'Benjamin', 'Avery', 'William', 'Sofia',
         'Grayson', 'Camila', 'Daniel', 'Aria', 'Jacob', 'Scarlett', 'Henry', 'Victoria', 'Owen', 'Madison', 'Luke',
         'Luna', 'Jack', 'Chloe', 'Wyatt', 'Grace', 'Jayden', 'Penelope', 'Ezra', 'Lily', 'Isaac', 'Riley', 'Landon',
         'Zoey', 'Nicholas', 'Nora', 'Aaron', 'Aurora', 'Eleanor', 'Adam', 'Audrey', 'Leah', 'Samantha', 'Nathan',
         'Bella', 'Ryan', 'Liliana', 'David', 'Maya', 'Isabelle', 'Caroline', 'Carter', 'Nova', 'Gabriel', 'Hazel',
         'Natalie', 'Nolan', 'Genesis', 'Eli', 'Elena', 'Olivia', 'Hannah', 'Christian', 'Ellie', 'Joshua', 'Aaliyah',
         'Julian', 'Savannah', 'Adrian', 'Aubrey', 'Leonardo', 'Stella', 'Miles', 'Jasmine', 'Anthony', 'Everly']


def show_users(request):
    data = {'names': names, 'dict': {'this is a': 'Dictionary'}}
    return render(request, 'usrs.html', context=data)
