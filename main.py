from repositories import UsersApiRepo


def main():
    user_api_repo = UsersApiRepo()
    users_from_internet = user_api_repo.get_users()
    if users_from_internet != None:
        print(*users_from_internet, sep='\n')
    else:
        print('Nema podataka o korisnicmia na internetu')

    print()
    user_5 = user_api_repo.get_user(5)
    if user_5 != None:
        print(user_5)
        print(user_5.email)
    print()


if __name__ == '__main__':
    main()
